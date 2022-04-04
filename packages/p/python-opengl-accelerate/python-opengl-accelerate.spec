#
# spec file for package python-opengl-accelerate
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
%define tarname PyOpenGL-accelerate
%define _version 3.1.6
Name:           python-opengl-accelerate
Version:        %{_version}
Release:        0
Summary:        Acceleration for python-opengl
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pyopengl.sourceforge.net
Source0:        %{tarname}-%{_version}.tar.gz
# test files: GitHub repo has no tags, use commit hash
Source1:        https://github.com/mcfletch/pyopengl/raw/c26398b91a/accelerate/tests/test_arraydatatypeaccel.py
Source2:        https://github.com/mcfletch/pyopengl/raw/c26398b91a/accelerate/tests/test_numpyaccel.py
#
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module opengl >= %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module numpy-devel if (%python-base without python36-base)}
Recommends:     python-numpy
Requires:       python-opengl >= %{version}
Provides:       python-PyOpenGL_accelerate = %{version}-%{release}
%python_subpackages

%description
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x. For code which uses large
arrays extensively speed-up is around 10% compared to unaccelerated
code.

%prep
%setup -q -n %{tarname}-%{_version}

# _service pulldown creates %%{tarname}-%%{_version}/accelerate/<required files>,
# move them to root of build area and remove 'accelerate' directory
# to continue as normal.
mv accelerate/* ./
rmdir accelerate

# Force Cython to rebuild .c files
rm src/*.c

%build
export CFLAGS="%{optflags} -DGLX_GLXEXT_LEGACY"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch %{SOURCE1} %{SOURCE2}

%files %{python_files}
%license license.txt
%doc README.txt
%{python_sitearch}/OpenGL_accelerate/
%{python_sitearch}/PyOpenGL_accelerate-*-py%{python_version}.egg-info

%changelog
