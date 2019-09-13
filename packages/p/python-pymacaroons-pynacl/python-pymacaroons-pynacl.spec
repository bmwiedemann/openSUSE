#
# spec file for package python-pymacaroons-pynacl
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
%define         github_name pymacaroons
Name:           python-pymacaroons-pynacl
Version:        0.9.3
Release:        0
Summary:        Macaroon library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/pymacaroons
Source:         https://github.com/matrix-org/%{github_name}/archive/v%{version}/pymacaroons-%{version}.tar.gz
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module libnacl}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl
Requires:       python-cffi
Requires:       python-six
Conflicts:      python-pymacaroons
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
%setup -q -n %{github_name}-%{version}
# requires too old hypothesis
rm -f tests/property_tests/macaroon_property_tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand %{_bindir}/nosetests-%{$python_bin_suffix} -e test_inspect

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
