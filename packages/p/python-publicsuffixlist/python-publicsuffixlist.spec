#
# spec file for package python-publicsuffixlist
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
Name:           python-publicsuffixlist
Version:        0.7.2
Release:        0
Summary:        Public suffix list implementaion in Python
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ko-zu/psl
Source:         https://files.pythonhosted.org/packages/source/p/publicsuffixlist/publicsuffixlist-%{version}.tar.gz
# PATCH-FIX-OPENSUSE change_psl_location.patch -- use list from publicsuffix package
Patch0:         change_psl_location.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  publicsuffix
# /SECTION
Requires:       publicsuffix
Recommends:     python-requests
BuildArch:      noarch

%python_subpackages

%description
Parser implementation for the Public Suffix List <https://publicsuffix.org/> in Python.

Support for IDN (unicode or punycoded).

%prep
%setup -q -n publicsuffixlist-%{version}
%patch0 -p1
sed -i '/public_suffix_list\.dat/ d' setup.py
rm publicsuffixlist/update.py

%build
%python_build

%install
%python_install
rm %{buildroot}%{_bindir}/publicsuffixlist-download
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
