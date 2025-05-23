#
# spec file for package python-UkPostcodeParser
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-UkPostcodeParser
Version:        1.1.2
Release:        0
Summary:        UK Postcode parser
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hamstah/ukpostcodeparser
Source:         https://files.pythonhosted.org/packages/source/U/UkPostcodeParser/UkPostcodeParser-%{version}.tar.gz
Patch1:         python312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
BuildArch:      noarch
%python_subpackages

%description
United Kingdom Postcode parser.

%prep
%autosetup -p1 -n UkPostcodeParser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/ukpostcodeparser/test/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests as it is ko for 2 years https://github.com/hamstah/ukpostcodeparser/issues/8
sed -i 's/test_\(091\|097\|098\|125\|131\)/_test_\1/' ukpostcodeparser/test/parser.py
%pyunittest ukpostcodeparser.test.parser

%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/ukpostcodeparser
%{python_sitelib}/[Uu]k[Pp]ostcode[Pp]arser-%{version}*-info

%changelog
