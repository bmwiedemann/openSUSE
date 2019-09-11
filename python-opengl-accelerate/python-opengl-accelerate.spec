#
# spec file for package python-opengl-accelerate
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
%define tarname PyOpenGL-accelerate
Name:           python-opengl-accelerate
Version:        3.1.3b1
Release:        0
Summary:        Acceleration for python-opengl
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pyopengl.sourceforge.net
Source0:        https://files.pythonhosted.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module opengl == %{version}}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-opengl = %{version}
%python_subpackages

%description
This set of C (Cython) extensions provides acceleration of common
operations for slow points in PyOpenGL 3.x. For code which uses large
arrays extensively speed-up is around 10% compared to unaccelerated
code.

%prep
%setup -q -n %{tarname}-%{version}

%build
export CFLAGS="%{optflags} -DGLX_GLXEXT_LEGACY"
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitearch}

%files %{python_files}
%license license.txt
%doc README.txt
%{python_sitearch}/OpenGL_accelerate/
%{python_sitearch}/PyOpenGL_accelerate-%{version}-py%{python_version}.egg-info

%changelog
