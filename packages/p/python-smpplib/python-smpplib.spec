#
# spec file for package python-smpplib
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016-2020, Martin Hauke <mardnh@gmx.de>
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
Name:           python-smpplib
Version:        2.1.0
Release:        0
Summary:        SMPP library for Python
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://pypi.org/project/smpplib/
#Git-Clone:     https://github.com/python-smpplib/python-smpplib.git
Source:         https://github.com/python-smpplib/python-smpplib/archive/%{version}.tar.gz#/smpplib-%{version}.tar.gz
Patch0:         python-smpplib-use-unittest-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
BuildArch:      noarch
%python_subpackages 

%description
SMPP is the Short Message Peer-to-Peer protocol for conveying SMS
operations.
Python-smpplib is a python based SMPP 3.4 client library that
allows you to send and receive SMS to an SMS gateway or SMSC.

%prep
%setup -q -n python-smpplib-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
# Remove tests from sitelib
%python_expand rm -R %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/smpplib*

%changelog
