#
# spec file for package python-ciso8601
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
Name:           python-ciso8601
Version:        2.3.2
Release:        0
Summary:        Fast ISO8601 date time parser for Python written in C
License:        MIT
URL:            https://github.com/closeio/ciso8601
Source:         https://files.pythonhosted.org/packages/source/c/ciso8601/ciso8601-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
%python_subpackages

%description
Fast ISO8601 date time parser for Python written in C

%prep
%autosetup -p1 -n ciso8601-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitearch}/ciso8601
%{python_sitearch}/ciso8601-%{version}.dist-info
%{python_sitearch}/ciso8601.cpython*so

%changelog
