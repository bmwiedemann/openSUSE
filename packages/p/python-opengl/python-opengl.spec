#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
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
Version:        3.1.6
Release:        0
Summary:        OpenGL bindings for Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pyopengl.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       Mesa-dri
Recommends:     python-numpy
Recommends:     python-opengl-accelerate
Recommends:     python-tk
Recommends:     tk >= 8.1
Provides:       python-PyOpenGL = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module opengl-accelerate}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  Mesa-dri
BuildRequires:  freeglut-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgle-devel
BuildRequires:  python3-numpy
BuildRequires:  swig
BuildRequires:  tk-devel
BuildRequires:  %{python_module pygame if (%python-base without python36-base)}
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
%setup -q -n %{tarname}-%{version}
# remove shebang
sed -e '1d' -i OpenGL/arrays/_buffers.py OpenGL/arrays/buffers.py
# avoid "python-bytecode-inconsistent-mtime" warning
FAKE_TIMESTAMP=$(LC_ALL=C date -u -r OpenGL/__init__.py +%%y%%m%%d%%H%%M)
find . -name '*.py' -exec touch -mat $FAKE_TIMESTAMP {} \;

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# don't test anything on python36: all tests need pygame, which is not available
python36_flags="--version"
%pytest ${$python_flags} tests
%endif

%if !%{with test}
%files %{python_files}
%license license.txt
%{python_sitelib}/OpenGL/
%{python_sitelib}/PyOpenGL-%{version}-py%{python_version}.egg-info
%endif

%changelog
