#
# spec file for package python-finance_enums
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-finance_enums
Version:        0.1.0
Release:        0
License:        Apache-2.0
Summary:        Standard finance enums
Url:            https://github.com/timkpaine/finance_enums
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/finance_enums/finance_enums-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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
