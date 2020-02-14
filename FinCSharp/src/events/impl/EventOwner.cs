﻿// TODO: This whole damn file is a war crime.
// TODO: How much overhead does this all introduce?

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using fin.data.collections.set;
using fin.pointer.contract;

namespace fin.events.impl {

  public sealed partial class EventFactory : IEventFactory {

    private abstract class EventOwner {

      private class EventContractDictionary : IContractPointerSet<IEventSubscription> {

        // TODO: Higher overhead than should be necessary.
        private readonly OrderedSet<IContractPointer<IEventSubscription>> contracts_ = new OrderedSet<IContractPointer<IEventSubscription>>();

        private readonly ConcurrentDictionary<IEventType, ISet<IContractPointer<IEventSubscription>>> sets_ =
          new ConcurrentDictionary<IEventType, ISet<IContractPointer<IEventSubscription>>>();

        public IEnumerable<IContractPointer<IEventSubscription>> Contracts => this.contracts_;

        public int Count => this.contracts_.Count;

        public IEnumerable<IContractPointer<IEventSubscription>>? Get(IEventType eventType) {
          this.sets_.TryGetValue(eventType, out ISet<IContractPointer<IEventSubscription>>? set);
          return set;
        }

        public bool Add(IContractPointer<IEventSubscription> contract) {
          if (this.contracts_.Add(contract)) {
            var genericEventType = contract.Value.IEventType;
            var set = this.sets_.GetOrAdd(genericEventType, genericEventType => new HashSet<IContractPointer<IEventSubscription>>());
            set.Add(contract);
            return true;
          }
          return false;
        }

        public bool Remove(IContractPointer<IEventSubscription> contract) {
          var genericEventType = contract.Value.IEventType;
          if (this.sets_.TryGetValue(genericEventType, out ISet<IContractPointer<IEventSubscription>>? set)) {
            if (set!.Remove(contract)) {
              if (set.Count() == 0) {
                this.sets_.TryRemove(genericEventType, out ISet<IContractPointer<IEventSubscription>>? _);
                this.contracts_.Remove(contract);
              }
              return true;
            }
          }
          return false;
        }

        public void ClearAndBreak(Action<IContractPointer<IEventSubscription>> breakHandler) {
          while (this.contracts_.Count > 0) {
            breakHandler(this.contracts_.First);
          }
          this.sets_.Clear();
        }
      }

      private EventContractDictionary set_ = new EventContractDictionary();
      protected IWeakContractPointerOwner<IEventSubscription> owner_;

      public EventOwner() {
        this.owner_ = IContractFactory.Instance.NewWeakOwner(this.set_);
      }

      public IEnumerable<IContractPointer<IEventSubscription>>? Get(IEventType eventType) => this.set_.Get(eventType);

      protected EventSubscription CreateSubscription(IEventSource source, IEventListener listener, EventType eventType, Action<EventType> action) {
        var subscription = this.HasSubscription_(source, listener, eventType, action);
        if (subscription != null) {
          return subscription;
        }

        subscription = new EventSubscription(source, listener, eventType, action);
        var contract = (source as EventSource)!.owner_.FormClosedWith(subscription, (listener as EventListener)!.owner_);
        subscription.Contract = contract;
        return subscription;
      }

      protected EventSubscription<T> CreateSubscription<T>(IEventSource source, IEventListener listener, EventType<T> eventType, Action<EventType<T>, T> action) {
        var subscription = this.HasSubscription_(source, listener, eventType, action);
        if (subscription != null) {
          return subscription;
        }

        subscription = new EventSubscription<T>(source, listener, eventType, action);
        var contract = (source as EventSource)!.owner_.FormClosedWith(subscription, (listener as EventListener)!.owner_);
        subscription.Contract = contract;
        return subscription;
      }

      // TODO: Find a faster way to do this.
      private EventSubscription? HasSubscription_(IEventSource source, IEventListener listener, EventType eventType, Action<EventType> action) {
        var contracts = this.set_.Contracts;
        foreach (var contract in contracts) {
          if (contract.Value is EventSubscription subscription) {
            if (subscription.Source == source && subscription.Listener == listener && subscription.EventType == eventType && subscription.Handler == action) {
              return subscription;
            }
          }
        }
        return null;
      }

      private EventSubscription<T>? HasSubscription_<T>(IEventSource source, IEventListener listener, EventType<T> eventType, Action<EventType<T>, T> action) {
        var contracts = this.set_.Contracts;
        foreach (var contract in contracts) {
          if (contract.Value is EventSubscription<T> subscription) {
            if (subscription.Source == source && subscription.Listener == listener && subscription.EventType == eventType && subscription.Handler == action) {
              return subscription;
            }
          }
        }
        return null;
      }
    }
  }
}