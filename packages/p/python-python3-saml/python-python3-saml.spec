#
# spec file for package python-python3-saml
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
Name:           python-python3-saml
Version:        1.7.0
Release:        0
Summary:        Python SAML support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/onelogin/python3-saml
Source:         https://github.com/onelogin/python3-saml/archive/v.%{version}.tar.gz#/python3-saml-%{version}.tar.gz
Patch0:         bug-testDecryptElement.patch
BuildRequires:  %{python_module defusedxml >= 0.5.0}
BuildRequires:  %{python_module freezegun >= 0.3.11}
BuildRequires:  %{python_module isodate >= 0.5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xmlsec >= 0.6.0}
BuildRequires:  fdupes
BuildRequires:  libxmlsec1-openssl1
BuildRequires:  python-rpm-macros
# Select the libxmlsec backend known to work
# pkgconfig doesnt auto-require it.
Requires:       libxmlsec1-openssl1
Requires:       python-defusedxml >= 0.5.0
Requires:       python-isodate >= 0.5.0
Requires:       python-xmlsec >= 0.6.0
BuildArch:      noarch
%python_subpackages

%description
Python SAML support for your Python 2 or 3 software.

SAML is an XML-based standard for web browser single sign-on and is
defined by the OASIS Security Services Technical Committee.

%prep
%setup -q -n python3-saml-v.%{version}
%patch0 -p1
sed -i 's/==/>=/;/dependency_links/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/onelogin

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
