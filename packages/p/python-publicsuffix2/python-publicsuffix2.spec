#
# spec file for package python-publicsuffix2
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
Name:           python-publicsuffix2
Version:        2.20191221
Release:        0
Summary:        Get a public suffix for a domain name using the Public Suffix List
License:        MIT AND MPL-2.0
URL:            https://github.com/nexb/python-publicsuffix2
Source:         https://files.pythonhosted.org/packages/source/p/publicsuffix2/publicsuffix2-%{version}.tar.gz
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Get a public suffix for a domain name using the Public Suffix List.
Forked from and using the same API as the publicsuffix package.

%prep
%setup -q -n publicsuffix2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license publicsuffix2.LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
