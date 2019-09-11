#
# spec file for package python-opengl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define tarname PyOpenGL
Name:           python-opengl
Version:        3.1.3b1
Release:        0
Summary:        OpenGL bindings for Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pyopengl.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module numpy}
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgle-devel
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  tk-devel
BuildRequires:  xorg-x11
Requires:       python-numpy
Requires:       tk >= 8.1
Recommends:     python-opengl-accelerate
BuildArch:      noarch
%python_subpackages

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%prep
%setup -q -n %{tarname}-%{version}
# remove shebang
sed -e '1d' -i OpenGL/arrays/_buffers.py OpenGL/arrays/buffers.py
# avoid "python-bytecode-inconsistent-mtime" warning
FAKE_TIMESTAMP=$(LC_ALL=C date -u -r %{SOURCE1} +%%y%%m%%d%%H%%M)
find . -name '*.py' -exec touch -mat $FAKE_TIMESTAMP {} \;

%build
export CFLAGS="%{optflags} -DGLX_GLXEXT_LEGACY"
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}/OpenGL/

%files %{python_files}
%license license.txt
%{python_sitelib}/OpenGL/
%{python_sitelib}/PyOpenGL-%{version}-py%{python_version}.egg-info

%changelog
