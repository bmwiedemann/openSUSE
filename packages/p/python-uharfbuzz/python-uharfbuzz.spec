#
# spec file for package python-uharfbuzz
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


%{?sle15_python_module_pythons}
Name:           python-uharfbuzz
Version:        0.45.0
Release:        0
Summary:        Streamlined Cython bindings for the harfbuzz shaping engine
License:        Apache-2.0
URL:            https://github.com/trufont/uharfbuzz
Source:         https://files.pythonhosted.org/packages/source/u/uharfbuzz/uharfbuzz-%{version}.tar.gz
BuildRequires:  %{python_module cython >= 0.28.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 36.4}
BuildRequires:  %{python_module setuptools_scm >= 2.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Streamlined Cython bindings for the harfbuzz shaping engine

%prep
%autosetup -p1 -n uharfbuzz-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/uharfbuzz
%{python_sitearch}/uharfbuzz-%{version}.dist-info

%changelog
