﻿using fin.app.node;
using fin.graphics.camera;

using OpenTK.Graphics.OpenGL;

namespace fin.graphics.impl.opentk {
  internal class OrthographicCameraOpenTk : IOrthographicCamera {
    private readonly IAppNode entryPoint_;
    public float Left { get; set; }
    public float Right { get; set; }
    public float Top { get; set; }
    public float Bottom { get; set; }
    public float Near { get; set; }
    public float Far { get; set; }

    public OrthographicCameraOpenTk(IAppNode entryPoint) {
      this.entryPoint_ = entryPoint;
    }

    public void Render(IGraphics graphics) {
      GL.MatrixMode(MatrixMode.Projection);
      GL.LoadIdentity();
      GL.Ortho(this.Left,
               this.Right,
               this.Bottom,
               this.Top,
               this.Near,
               this.Far);
      GL.PushMatrix();

      this.entryPoint_.Emit(
        new RenderForOrthographicCameraTickEvent(graphics, this));

      GL.MatrixMode(MatrixMode.Projection);
      GL.PopMatrix();
    }
  }
}