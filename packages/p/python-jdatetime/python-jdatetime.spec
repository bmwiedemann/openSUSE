#
# spec file for package python-jdatetime
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-jdatetime
Version:        3.6.2
Release:        0
Summary:        Jalali datetime binding for python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/slashmili/python-jalali
Source:         https://github.com/slashmili/python-jalali/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
jdatetime is the Jalali implementation of Python's datetime module.

%prep
%setup -q -n python-jalali-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec t/test.py

%files %{python_files}
%doc README.rst CHANGELOG.md
%license LICENSE
%{python_sitelib}/*

%changelog
