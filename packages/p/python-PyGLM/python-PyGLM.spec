#
# spec file for package python-PyGLM
#
# Copyright (c) 2023 SUSE LLC
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


%define modname PyGLM
Name:           python-PyGLM
Version:        2.7.1
Release:        0
Summary:        OpenGL Mathematics library for Python
# Bundled GLM is MIT, everything else is Zlib
License:        Zlib AND MIT
URL:            https://github.com/Zuzu-Typ/PyGLM
# Tests missing from PyPI sources, use service file to include tests and glm submodule
Source:         %{modname}-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%python_subpackages

%description
PyGLM is an OpenGL Mathematics library for Python. It mostly compatible with
GLM and offers a variety of features for vector and matrix manipulation.

%prep
%autosetup -p1 -n PyGLM-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Failing tests: https://github.com/Zuzu-Typ/PyGLM/issues/227
%pytest_arch -k 'not (test_findMSB or test_bitCount)'

%files %{python_files}
%doc README.md
%license COPYING LICENSE
%{python_sitearch}/glm.*.so
%{python_sitearch}/glm-stubs/
%{python_sitearch}/PyGLM-%{version}.dist-info

%changelog
