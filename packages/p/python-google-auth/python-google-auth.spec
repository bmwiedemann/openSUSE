#
# spec file for package python-google-auth
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
Name:           python-google-auth
Version:        2.31.0
Release:        0
Summary:        Google Authentication Library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-auth-library-python
Source:         https://files.pythonhosted.org/packages/source/g/google-auth/google-auth-%{version}.tar.gz
# https://github.com/googleapis/google-auth-library-python/issues/1055
Patch1:         python-google-auth-no-mock.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module aiohttp >= 3.6.2}
BuildRequires:  %{python_module cachetools >= 2.0.0}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pyOpenSSL >= 22.0.0}
BuildRequires:  %{python_module pyasn1-modules >= 0.2.1}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyu2f >= 0.1.5}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module rsa >= 3.1.4}
BuildRequires:  %{python_module setuptools >= 40.3.0}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cachetools >= 2.0.0
Requires:       python-pyasn1-modules >= 0.2.1
Requires:       python-rsa >= 3.1.4
Requires:       python-urllib3
Recommends:     python-aiohttp >= 3.6.2
Recommends:     python-cryptography >= 38.0.3
Recommends:     python-pyOpenSSL >= 22.0.0
Recommends:     python-pyu2f >= 0.1.5
Recommends:     python-requests >= 2.20.0
BuildArch:      noarch
%python_subpackages

%description
This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.

%prep
%autosetup -p1 -n google-auth-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# don't test deprecated oauth2client utilities if we don't have it anymore
%pytest --ignore tests/test__oauth2client.py

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/google
%{python_sitelib}/google/auth
%{python_sitelib}/google/oauth2
%{python_sitelib}/google_auth-%{version}*-info

%changelog
