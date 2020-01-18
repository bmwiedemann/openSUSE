#
# spec file for package python-publicsuffix
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
%define skip_python2 1
Name:           python-publicsuffix
Version:        1.1.0
Release:        0
Summary:        Public Suffix List
License:        MIT
URL:            https://publicsuffix.org
Source:         https://files.pythonhosted.org/packages/source/p/publicsuffix/publicsuffix-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Get a public suffix for a domain name using the Public Suffix List.

%prep
%setup -q -n publicsuffix-%{version}

%build
LANG=en_US.UTF-8
%python_build

%install
LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
LANG=en_US.UTF-8
%pytest tests.py -k 'not test_fetch'

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
