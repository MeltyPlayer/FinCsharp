﻿using System;

namespace fin.assert {
  public class AssertionException : Exception {
    public AssertionException() { }

    public AssertionException(string message) : base(message) { }

    public AssertionException(string message, Exception inner) : base(message,
      inner) { }
  }
}