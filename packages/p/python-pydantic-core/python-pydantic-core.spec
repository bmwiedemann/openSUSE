#
# spec file for package python-pydantic-core
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-pydantic-core
Version:        2.16.3
Release:        0
Summary:        Core functionality for pydantic validation and serialization
License:        MIT
URL:            https://github.com/pydantic/pydantic-core
Source0:        https://files.pythonhosted.org/packages/source/p/pydantic-core/pydantic_core-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing-extensions >= 4.6.0}
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing-extensions >= 4.6.0
%python_subpackages

%description
This package provides the core functionality for [pydantic](https://docs.pydantic.dev) validation and serialization.

Pydantic-core is currently around 17x faster than pydantic V1.

%prep
%autosetup -p1 -n pydantic_core-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%{python_sitearch}/pydantic_core
%{python_sitearch}/pydantic_core-%{version}.dist-info

%changelog
