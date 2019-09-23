#
# spec file for package python-UkPostcodeParser
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-UkPostcodeParser
Version:        1.1.2
Release:        0
Summary:        UK Postcode parser
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hamstah/ukpostcodeparser
Source:         https://files.pythonhosted.org/packages/source/U/UkPostcodeParser/UkPostcodeParser-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
BuildArch:      noarch
%python_subpackages

%description
United Kingdom Postcode parser.

%prep
%setup -q -n UkPostcodeParser-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/ukpostcodeparser/test/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests as it is ko for 2 years https://github.com/hamstah/ukpostcodeparser/issues/8
sed -i 's/test_\(091\|097\|098\|125\|131\)/_test_\1/' ukpostcodeparser/test/parser.py
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/*

%changelog
