#
# spec file for package python-ucsmsdk
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
Name:           python-ucsmsdk
Version:        0.9.12
Release:        0
Summary:        Python SDK for Cisco UCS Manager
License:        Apache-2.0
URL:            https://github.com/CiscoUcs/ucsmsdk
Source:         https://github.com/CiscoUcs/ucsmsdk/archive/v%{version}.tar.gz#/ucsmsdk-%{version}.tar.gz
Patch0:         remove-nose.patch
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyOpenSSL
Requires:       python-pyparsing
Requires:       python-setuptools
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python Software Developer Kit for Cisco Unified Computing System (UCS) Manager.

%prep
%setup -q -n ucsmsdk-%{version}
chmod -x ucsmsdk/utils/*.py
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip tests that do string comparison on xml https://github.com/CiscoUcs/ucsmsdk/issues/188
%pytest -k 'not (TestUCStoXML or TestUnknownProps or create_gmo_using)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ucsmsdk
%{python_sitelib}/ucsmsdk-*.egg-info

%changelog
