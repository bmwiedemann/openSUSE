#
# spec file for package python-opengl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-opengl%{psuffix}
Version:        3.1.3b2
Release:        0
Summary:        OpenGL bindings for Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pyopengl.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
Recommends:     python-opengl-accelerate
Recommends:     python-tk
Recommends:     tk >= 8.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module opengl-accelerate}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pygame}
BuildRequires:  %{python_module pytest}
BuildRequires:  Mesa-dri
BuildRequires:  freeglut-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgle-devel
BuildRequires:  python3-numpy
BuildRequires:  swig
BuildRequires:  tk-devel
BuildRequires:  xvfb-run
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
# test_buffer_api_basic is a test specific to opengl-accelerate, failing on i586 and armv7l
# https://github.com/mcfletch/pyopengl/issues/29
%{python_expand #
xvfb-run -s "-screen 0 1400x900x24 +iglx" $python -m pytest -v tests -k "not test_buffer_api_basic"
}
%endif

%if !%{with test}
%files %{python_files}
%license license.txt
%{python_sitelib}/OpenGL/
%{python_sitelib}/PyOpenGL-%{version}-py%{python_version}.egg-info
%endif

%changelog
