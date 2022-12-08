#
# spec file for package python-covdefaults
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-covdefaults
Version:        2.2.2
Release:        0
Summary:        Python coverage plugin to provide default settings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/asottile/covdefaults
Source:         https://github.com/asottile/covdefaults/archive/v%{version}.tar.gz#/covdefaults-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coverage
BuildArch:      noarch
%python_subpackages

%description
Python coverage plugin to provide default settings.

%prep
%setup -q -n covdefaults-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m coverage run -m pytest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
