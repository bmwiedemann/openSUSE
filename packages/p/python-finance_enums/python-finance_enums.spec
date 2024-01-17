#
# spec file for package python-finance_enums
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python36 1
Name:           python-finance_enums
Version:        0.1.0
Release:        0
License:        Apache-2.0
Summary:        Standard finance enums
URL:            https://github.com/timkpaine/finance_enums
Source:         https://files.pythonhosted.org/packages/source/f/finance_enums/finance_enums-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pandas >= 0.23.4
BuildArch:      noarch

%python_subpackages

%description
Standard financial enumerations.

%prep
%setup -q -n finance_enums-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
