﻿using System;

using fin.function;

using OpenTK.Input;

namespace fin.input.impl.opentk {

  public class EndTickPhase { }

  public static class OpenTkKeyToKeyIdConverter {
    public static KeyId Convert(Key key) =>
      key switch
      {
        Key.A => KeyId.A,
        Key.B => KeyId.B,
        Key.C => KeyId.C,
        Key.D => KeyId.D,
        Key.E => KeyId.E,
        Key.F => KeyId.F,
        Key.G => KeyId.G,
        Key.H => KeyId.H,
        Key.I => KeyId.I,

        Key.Space => KeyId.SPACEBAR,
        Key.Enter => KeyId.ENTER,
        Key.Escape => KeyId.ESC,

        // TODO: Add rest.
        _ => KeyId.UNKNOWN,
      };
  }

  public interface IKeyButtonDictionary {
    IButton this[KeyId keyId] { get; }
  }

  public class OpenTkKeyButtonDictionary : IKeyButtonDictionary {
    public OpenTkKeyButtonDictionary(IKeyStateDictionary ksd) {
      this.GetButtonImpl_ = Memoization.Memoize((KeyId keyId) => new OpenTkKeyButton(keyId, ksd));
    }

    public IButton this[KeyId keyId] => this.GetButtonImpl_(keyId);

    private Func<KeyId, IButton> GetButtonImpl_ { get; }

    private class OpenTkKeyButton : IButton {
      private readonly KeyId keyId_;
      private readonly IKeyStateDictionary ksd_;

      public OpenTkKeyButton(KeyId keyId, IKeyStateDictionary ksd) {
        this.keyId_ = keyId;
        this.ksd_ = ksd;
      }

      public ButtonState State => this.ksd_[this.keyId_];
    }
  }
}