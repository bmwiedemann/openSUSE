#
# spec file for package python-opengl-accelerate
#
# Copyright (c) 2025 SUSE LLC
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


%define tarname PyOpenGL-accelerate
%define _version 3.1.9
%{?sle15_python_module_pythons}
Name:           python-opengl-accelerate
Version:        %{_version}
Release:        0
Summary:        Acceleration for python-opengl
License:        BSD-3-Clause
URL:            http://pyopengl.sourceforge.net
Source0:        %{tarname}-%{_version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module opengl >= %{version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n %{tarname}-%{_version}

# _service pulldown creates %%{tarname}-%%{_version}/accelerate/<required files>,
# move them to root of build area and remove 'accelerate' directory
# to continue as normal.
mv accelerate/* ./
rmdir accelerate

%build
export CFLAGS="%{optflags} -DGLX_GLXEXT_LEGACY"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license license.txt
%doc README.md
%{python_sitearch}/OpenGL_accelerate/
%{python_sitearch}/[Pp]y[Oo]pen[Gg][Ll]_accelerate-%{version}.dist-info

%changelog
