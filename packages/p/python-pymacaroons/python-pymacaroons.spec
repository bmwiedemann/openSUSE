#
# spec file for package python-pymacaroons
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

Name:           python-pymacaroons
Version:        0.13.0
Release:        0
Summary:        Macaroon library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ecordell/pymacaroons
Source:         https://github.com/ecordell/pymacaroons/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/ecordell/pymacaroons/pull/54/
Patch0:         python-pymacaroons-remove-nose.patch
BuildRequires:  %{python_module PyNaCl < 2.0}
BuildRequires:  %{python_module PyNaCl >= 1.1.2}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl < 2.0
Requires:       python-PyNaCl >= 1.1.2
Requires:       python-cffi
Requires:       python-six >= 1.8.0
Conflicts:      python-pymacaroons-pynacl
BuildArch:      noarch
%python_subpackages

%description
Macaroons, like cookies, are a form of bearer credential.
Unlike opaque tokens, macaroons embed caveats that define
specific authorization requirements for the target service,
the service that issued the root macaroon and which is
capable of verifying the integrity of macaroons it recieves.

Macaroons allow for delegation and attenuation of authorization.
They are simple and fast to verify, and decouple authorization policy
from the enforcement of that policy.

This is a Python implementation of Macaroons.

%prep
%setup -q -n pymacaroons-%{version}
%patch0 -p1
# requires too old hypothesis
rm -f tests/property_tests/macaroon_property_tests.py

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
