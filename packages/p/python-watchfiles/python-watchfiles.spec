#
# spec file for package python-watchfiles
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


Name:           python-watchfiles
Version:        0.22.0
Release:        0
Summary:        File watching and code reload in python
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source0:        https://github.com/samuelcolvin/watchfiles/archive/refs/tags/v%{version}.tar.gz#/watchfiles-%{version}-gh.tar.gz
Source1:        vendor.tar.xz
# gh#samuelcolvin/watchfiles#254
BuildRequires:  %{python_module anyio >= 3.0.0 with %python-anyio < 4}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module maturin >= 0.14.16}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-anyio >= 3.0.0 with python-anyio < 4)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-pretty}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A package for file watching and code reload in python.

This package was previously named "watchgod".

%prep
%autosetup -p1 -n watchfiles-%{version} -a1
# Need to replace version because we build from github archive
sed -i 's/version = "0.0.0"/version = "%{version}"/' Cargo.toml

%build
%pyproject_wheel

%install
%pyproject_install
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
