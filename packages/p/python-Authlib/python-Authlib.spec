#
# spec file for package python-Authlib
#
# Copyright (c) 2022 SUSE LLC
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
%define modname authlib

Name:           python-Authlib
Version:        1.2.0
Release:        0
Summary:        Python library for building OAuth and OpenID Connect servers
License:        BSD-3-Clause
URL:            https://authlib.org/
Source:         https://github.com/lepture/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib} PYTHONDONTWRITEBYTECODE=1
$python -mpytest tests/core
$python -mpytest tests/flask
# gh#lepture/authlib#456
$python -mpytest tests/jose -k 'not (test_dir_alg_xc20p or test_xc20p_content_encryption_decryption)'
export DJANGO_SETTINGS_MODULE=tests.clients.test_django.settings
$python -mpytest tests/clients
# export DJANGO_SETTINGS_MODULE=tests.django.settings
# $python -mpytest tests/django
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/Authlib-%{version}*-info

%changelog
