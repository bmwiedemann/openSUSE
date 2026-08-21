#
# spec file for package python-comfy-angle
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-comfy-angle
Version:        0.1.0
Release:        0
Summary:        Mesa/libglvnd backend for ComfyUI's comfy-angle API
# Legal-Review-Notice: this package does not ship ANGLE or Electron
# binaries; it locates system libEGL/libGLESv2 from libglvnd/Mesa. The
# name matches the ComfyUI optional extra comfy-angle.
License:        MIT
URL:            https://github.com/Comfy-Org/comfy-angle
# Distro wrapper implementing the PyPI comfy-angle 0.1.0 Python API
# against system Mesa/libglvnd. Bare filenames (no download URL) so
# factory-auto does not fetch Electron/GitHub wheels.
Source0:        pyproject.toml
Source1:        __init__.py
Source2:        LICENSE
Source3:        README.md
# ctypes-loaded libglvnd is not DT_NEEDED; filter explicit-lib-dependency.
Source4:        python-comfy-angle-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  Mesa-dri
BuildRequires:  Mesa-libEGL1
BuildRequires:  fdupes
BuildRequires:  libglvnd
BuildRequires:  python-rpm-macros
# Runtime libs the module locates via ctypes (also BR so %%check can CDLL).
Requires:       Mesa-dri
Requires:       Mesa-libEGL1
Requires:       libglvnd
BuildArch:      noarch
%python_subpackages

%description
Distro implementation of the comfy-angle 0.1.0 Python API used by
ComfyUI's GLSL Shader node. The module locates the system's libEGL
and libGLESv2 (libglvnd dispatch plus Mesa) at runtime. It does not
ship Chromium ANGLE or Electron-extracted binaries.

%prep
%setup -q -T -c -n comfy-angle-%{version}
install -d comfy_angle
cp %{SOURCE0} pyproject.toml
cp %{SOURCE1} comfy_angle/__init__.py
cp %{SOURCE2} LICENSE
cp %{SOURCE3} README.md

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/comfy_angle
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Import the 0.1.0 API and load system libEGL/libGLESv2 (fail if missing).
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import ctypes, comfy_angle as c; assert c.__all__ == ['get_lib_dir', 'get_egl_path', 'get_glesv2_path']; e, g = c.get_egl_path(), c.get_glesv2_path(); assert e and g; ctypes.CDLL(e); ctypes.CDLL(g); c.get_lib_dir()"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/comfy_angle
%{python_sitelib}/comfy_angle-%{version}.dist-info

%changelog
