#
# spec file for package python-opengl
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define tarname PyOpenGL
%{?sle15_python_module_pythons}
Name:           python-opengl%{psuffix}
Version:        3.1.7
Release:        0
Summary:        OpenGL bindings for Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/mcfletch/pyopengl
Source0:        https://files.pythonhosted.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM PyOpenGL-pr100-py312.patch gh#mcfletch/pyopengl#100
Patch0:         PyOpenGL-pr100-py312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       Mesa-dri
Recommends:     python-numpy
Recommends:     python-opengl-accelerate
Recommends:     python-tk
Recommends:     tk >= 8.1
Provides:       python-PyOpenGL = %{version}-%{release}
Provides:       python-pyopengl = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opengl-accelerate}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pygame}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  Mesa-dri
BuildRequires:  freeglut-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgle-devel
BuildRequires:  swig
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-glx)
%endif
%python_subpackages

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%prep
%autosetup -p1 -n %{tarname}-%{version}
# remove shebang
sed -e '1{/^#/d}' -i OpenGL/arrays/_buffers.py OpenGL/arrays/buffers.py

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest tests
%endif

%if !%{with test}
%files %{python_files}
%license license.txt
%{python_sitelib}/OpenGL/
%{python_sitelib}/PyOpenGL-%{version}.dist-info
%endif

%changelog
