#
# spec file for package python-fvs
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


%define skip_python2 1
# FVS requires Python 3.9 or higher
%define skip_python37 1
%define skip_python38 1
%define modname FVS
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fvs
Version:        0.3.4
Release:        0
Summary:        File Versioning System with hash comparison
License:        MIT
URL:            https://github.com/mirkobrombin/FVS
Source:         https://github.com/mirkobrombin/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-orjson
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
File Versioning System with hash comparison and data storage to
create unlinked states that can be deleted

The main reason for this project is for the purpose of personal
knowledge and understanding of the versioning system. The second
reason is to make a simple and easy-to-implement versioning
system for Bottles.

There are plenty of other versioning systems out there, but all
of these provide features that I wouldn't need in my projects.
The purpose of FVS is to always remain as clear and simple as
possible, providing only the functionality of organizing file
versions into states, ie recovery points that take advantage of
deduplication to minimize space consumption

%prep
%autosetup -p1 -n FVS-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fvs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No tests available, even upstream

%post
%python_install_alternative fvs

%postun
%python_uninstall_alternative fvs

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/fvs
%{python_sitelib}/%{modname}-%{version}*-info
%{python_sitelib}/fvs

%changelog
