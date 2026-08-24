# python-comfy-angle (openSUSE)

Distro implementation of the [comfy-angle](https://github.com/Comfy-Org/comfy-angle)
0.1.1 Python API used by ComfyUI's GLSL Shader node (`comfy-angle` optional extra).

This package does **not** ship Chromium ANGLE `libEGL` / `libGLESv2` binaries.
At runtime it locates the system's libglvnd dispatch libraries
(`libEGL.so.1`, `libGLESv2.so.2`) and Mesa (`Mesa-libEGL1`, `Mesa-dri`).
Headless rendering is provided by Mesa's surfaceless EGL platform, so no X11,
Wayland or GBM session is required.

```python
import comfy_angle

comfy_angle.get_lib_dir()
comfy_angle.get_egl_path()
comfy_angle.get_glesv2_path()
```
