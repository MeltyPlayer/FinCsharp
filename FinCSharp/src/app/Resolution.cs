﻿namespace fin.app {

  public struct Resolution {
    public int Width { get; }
    public int Height { get; }

    public Resolution(int width, int height) {
      this.Width = width;
      this.Height = height;
    }
  }
}