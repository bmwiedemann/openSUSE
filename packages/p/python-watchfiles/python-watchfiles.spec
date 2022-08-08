#
# spec file for package python-watchfiles
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


Name:           python-watchfiles
Version:        0.15.0
Release:        0
Summary:        File watching and code reload in python
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source0:        https://files.pythonhosted.org/packages/source/w/watchfiles/watchfiles-%{version}.tar.gz
Source1:        vendor.tar.xz
# PATCH-FEATURE-OPENSUSE cargo_config.patch code@bnavigator.de -- replace cargo config
Patch0:         cargo_config.patch
BuildRequires:  %{python_module anyio >= 3.0.0 with %python-anyio < 4}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-maturin >= 0.13
Requires:       (python-anyio >= 3.0.0 with python-anyio < 4)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-sugar}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A package for file watching and code reload in python.

This package was previously named "watchgod".

%prep
%autosetup -p1 -n watchfiles-%{version} -a1
rm docs/requirements.txt docs/CNAME
dos2unix README.md docs/* docs/api/*

%build
# one universal abi3 wheel for all flavors
maturin build -r --compatibility linux -o wheels

%install
%pyproject_install wheels/watchfiles-%{version}*.whl
%python_clone -a %{buildroot}%{_bindir}/watchfiles
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv watchfiles watchfiles.movedaway
%pytest_arch

%post
%python_install_alternative watchfiles

%postun
%python_uninstall_alternative watchfiles

%files %{python_files}
%license LICENSE
%doc README.md docs/*
%python_alternative %{_bindir}/watchfiles
%{python_sitearch}/watchfiles
%{python_sitearch}/watchfiles-%{version}*-info

%changelog
