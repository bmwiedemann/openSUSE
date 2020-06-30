#
# spec file for package python-apns2
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
Name:           python-apns2
Version:        0.7.1
Release:        0
Summary:        Python library for the HTTP/2 Apple Push Notification Service
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Pr0Ger/PyAPNs2
Source0:        https://files.pythonhosted.org/packages/source/a/apns2/apns2-%{version}.tar.gz
# LICENSE gh#Pr0Ger/PyAPNs2#110 mcepl@suse.com
# Missing LICENSE file
Source1:        https://raw.githubusercontent.com/Pr0Ger/PyAPNs2/master/LICENSE
# eckey.pem gh#Pr0Ger/PyAPNs2#111 mcepl@suse.com
# Unpackaged file breaks test_token_expiration test
Source2:        https://raw.githubusercontent.com/Pr0Ger/PyAPNs2/master/test/eckey.pem
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 1.4.0
Requires:       python-cryptography >= 1.7.2
Requires:       python-hyper >= 0.7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyJWT >= 1.4.0}
BuildRequires:  %{python_module cryptography >= 1.7.2}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module hyper >= 0.7}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A python library for interacting with the Apple Push Notification Service
via HTTP/2 protocol.

%prep
%setup -q -n apns2-%{version}
cp %{SOURCE1} .
cp %{SOURCE2} test/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
