#
# spec file for package python-reconfigure
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


%define ver_hash 099e3a561f78be45c4cd4798f61b762b59f2dcbf
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-reconfigure
Version:        0.1.82
Release:        0
Summary:        Python ORM for config files
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Eugeny/reconfigure
# Lack of tags https://github.com/Eugeny/reconfigure/issues/11
Source:         https://github.com/Eugeny/reconfigure/archive/%{ver_hash}.tar.gz#/reconfigure-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module chardet}
# /SECTION
%python_subpackages

%description
Python ORM for config files.

%prep
%setup -q -n reconfigure-%{ver_hash}
printf '[pytest]\npython_files = *_test*.py' > pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# crontab_tests: https://github.com/Eugeny/reconfigure/issues/26
%pytest reconfigure/tests/ -k 'not crontab_tests'

%files %{python_files}
%doc README.rst
%license docs/LICENSE
%{python_sitelib}/*

%changelog
