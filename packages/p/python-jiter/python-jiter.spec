#
# spec file for package python-jiter
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-jiter
Version:        0.11.1
Release:        0
Summary:        Fast iterable JSON parser
License:        MIT
URL:            https://github.com/pydantic/jiter/
Source0:        https://files.pythonhosted.org/packages/source/j/jiter/jiter-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module maturin >= 1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This is a standalone version of the JSON parser used in `pydantic-core`. The recommendation is to only use this package directly if you do not use `pydantic`.

%prep
%autosetup -p1 -n jiter-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd crates/jiter-python/tests
%pytest_arch test_jiter.py
popd

%files %{python_files}
%doc README.md
%{python_sitearch}/jiter
%{python_sitearch}/jiter-%{version}.dist-info

%changelog
