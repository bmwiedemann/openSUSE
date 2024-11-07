#
# spec file for package python-publicsuffixlist
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


%{?sle15_python_module_pythons}
Name:           python-publicsuffixlist
Version:        1.0.2.20241107
Release:        0
Summary:        Public suffix list implementaion in Python
License:        MPL-2.0
URL:            https://github.com/ko-zu/psl
Source:         https://files.pythonhosted.org/packages/source/p/publicsuffixlist/publicsuffixlist-%{version}.tar.gz
# PATCH-FIX-OPENSUSE change_psl_location.patch -- use list from publicsuffix package
Patch0:         change_psl_location.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n publicsuffixlist-%{version}
sed -i '/public_suffix_list\.dat/ d' setup.py
rm publicsuffixlist/update.py

%build
%pyproject_wheel

%install
%pyproject_install
rm %{buildroot}%{_bindir}/publicsuffixlist-download
%{python_expand rm -f %{buildroot}%{$python_sitelib}/publicsuffixlist/test* %{buildroot}%{$python_sitelib}/publicsuffixlist/__pycache__/test*
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/publicsuffixlist
%{python_sitelib}/publicsuffixlist-%{version}.dist-info

%changelog
