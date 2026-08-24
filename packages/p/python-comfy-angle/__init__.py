"""Locate system libEGL/libGLESv2 (libglvnd/Mesa) for ComfyUI's ANGLE API.

This is a distro implementation of the PyPI comfy-angle 0.1.1 import API.
It does not ship Chromium ANGLE shared libraries; headless operation is
provided by Mesa's surfaceless EGL platform.
"""

import ctypes.util
import os

from importlib.metadata import PackageNotFoundError, version as _version

try:
    __version__ = _version("comfy-angle")
except PackageNotFoundError:
    __version__ = "0.1.1"

__all__ = ["get_lib_dir", "get_egl_path", "get_glesv2_path"]

# Well-known sonames (libglvnd dispatch) and directories used when
# ctypes.util.find_library returns nothing.
_LIBDIRS = ("/usr/lib64", "/usr/lib", "/lib64", "/lib")
_EGL_SONAMES = ("libEGL.so.1", "libEGL.so")
_GLESV2_SONAMES = ("libGLESv2.so.2", "libGLESv2.so")


def _locate(short_name, sonames, pretty):
    """Return a path ctypes.CDLL can load, or raise RuntimeError."""
    candidates = []
    found = ctypes.util.find_library(short_name)
    if found:
        candidates.append(found)
    candidates.extend(sonames)

    seen = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if os.path.isfile(candidate):
            return candidate
        base = os.path.basename(candidate)
        for libdir in _LIBDIRS:
            path = os.path.join(libdir, base)
            if os.path.isfile(path):
                return path
        # find_library often returns a soname (libEGL.so.1), which CDLL
        # can load via the dynamic linker even if it is not an abs path.
        if found and candidate == found:
            return candidate

    tried = ", ".join(candidates) if candidates else short_name
    raise RuntimeError(
        "Could not locate a loadable %s library (tried %s). "
        "Install libglvnd, Mesa-libEGL1 and Mesa-dri."
        % (pretty, tried)
    )


def get_egl_path() -> str:
    """Return the path to the system EGL library."""
    return _locate("EGL", _EGL_SONAMES, "EGL")


def get_glesv2_path() -> str:
    """Return the path to the system GLESv2 library."""
    return _locate("GLESv2", _GLESV2_SONAMES, "GLESv2")


def get_lib_dir() -> str:
    """Return the directory containing the EGL library, or '' if unknown."""
    path = get_egl_path()
    if os.path.isabs(path):
        return os.path.dirname(path)
    return ""
