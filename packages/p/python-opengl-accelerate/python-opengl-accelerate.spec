#
# spec file for package python-opengl-accelerate
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
%define tarname PyOpenGL-accelerate
%define _version 3.1.3b1
Name:           python-opengl-accelerate
Version:        %{_version}.post1
Release:        0
Summary:        Acceleration for python-opengl
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pyopengl.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{tarname}/%{tarname}-%{_version}.tar.gz
# Missing pxd only needed to rebuild .c https://github.com/mcfletch/pyopengl/issues/12
Source2:        https://raw.githubusercontent.com/mcfletch/pyopengl/master/accelerate/OpenGL_accelerate/formathandler.pxd
Source3:        https://raw.githubusercontent.com/mcfletch/pyopengl/master/accelerate/OpenGL_accelerate/wrapper.pxd
# Newer numpy_formathandler.pyx needed to match opengl 3.1.3b2
# https://github.com/mcfletch/pyopengl/issues/28
# Patch is subset of https://bazaar.launchpad.net/~mcfletch/pyopengl/trunk/diff/1099
Patch0:         commit1080.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module opengl >= %{version}}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-opengl >= %{version}
%python_subpackages

%description
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x. For code which uses large
arrays extensively speed-up is around 10% compared to unaccelerated
code.

%prep
%setup -q -n %{tarname}-%{_version}
%patch0 -p1
sed -i 's/\t/    /g' src/numpy_formathandler.pyx

cp %{SOURCE2} %{SOURCE3} OpenGL_accelerate/

# Force Cython to rebuild .c files
rm src/*.c

%build
export CFLAGS="%{optflags} -DGLX_GLXEXT_LEGACY"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license license.txt
%doc README.txt
%{python_sitearch}/OpenGL_accelerate/
%{python_sitearch}/PyOpenGL_accelerate-*-py%{python_version}.egg-info

%changelog
