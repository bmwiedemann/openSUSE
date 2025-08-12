#
# spec file for package python-Authlib
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define modname authlib
%{?sle15_python_module_pythons}
Name:           python-Authlib
Version:        1.6.1
Release:        0
Summary:        Python library for building OAuth and OpenID Connect servers
License:        BSD-3-Clause
URL:            https://authlib.org/
Source:         https://github.com/lepture/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Flask-SQLAlchemy}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module cachelib}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography
Suggests:       python-requests
BuildArch:      noarch
%python_subpackages

%description
A Python library for building OAuth and OpenID Connect servers.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Remove the file containing the commercial license so licensedigger
# doesn't complain about the dual license
rm COMMERCIAL-LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib} PYTHONDONTWRITEBYTECODE=1
$python -mpytest tests/core
$python -mpytest tests/flask
# gh#lepture/authlib#456
# $python -mpytest tests/jose -k 'not (test_dir_alg_xc20p or test_xc20p_content_encryption_decryption)'
$python -mpytest tests/jose
export DJANGO_SETTINGS_MODULE=tests.clients.test_django.settings
$python -mpytest tests/clients
# export DJANGO_SETTINGS_MODULE=tests.django.settings
# $python -mpytest tests/django
}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/[Aa]uthlib-%{version}.dist-info

%changelog
