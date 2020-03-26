#
# spec file for package python-oauth2client
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
%bcond_with django
Name:           python-oauth2client
Version:        4.1.3
Release:        0
Summary:        Pythob OAuth2 Client
License:        Apache-2.0
URL:            https://github.com/google/oauth2client
Source0:        https://files.pythonhosted.org/packages/source/o/oauth2client/oauth2client-%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.9}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module fasteners}
BuildRequires:  %{python_module httplib2 >= 0.9.1}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pyasn1-modules >= 0.0.5}
BuildRequires:  %{python_module pycrypto}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rsa >= 3.1.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-fasteners
Requires:       python-httplib2 >= 0.9.1
Requires:       python-pyasn1 >= 0.1.7
Requires:       python-pyasn1-modules >= 0.0.5
Requires:       python-pycrypto
Requires:       python-rsa >= 3.1.4
Requires:       python-six >= 1.6.1
Conflicts:      google-api-python-client < 1.3.0
Conflicts:      python-google-api-python-client < 1.3.0
BuildArch:      noarch
%if %{with django}
BuildRequires:  %{python_module Django >= 1.8}
%endif
%python_subpackages

%description
This is a Python library for accessing resources protected by OAuth 2.0.

%package django
Summary:        Django extension
Requires:       python-Django >= 1.8
Requires:       python-jsonpickle
Requires:       python-oauth2client = %{version}

%description django
OAuth 2.0 utilities for Django.

Utilities for using OAuth 2.0 in conjunction with
the Django datastore.

%package flask
Summary:        Flask extension
Requires:       python-Flask >= 0.9
Requires:       python-oauth2client = %{version}

%description flask
Provides a Flask extension that makes using OAuth2 web server flow easier.
The extension includes views that handle the entire auth flow and a
``@required`` decorator to automatically ensure that user credentials are
available.

%package gce
Summary:        GCE extension
Requires:       python-oauth2client = %{version}

%description gce
Utilities for Google Compute Engine

Utilities for making it easier to use OAuth 2.0 on Google Compute Engine.

%prep
%setup -q -n oauth2client-%{version}
%if !%{with django}
rm -rf oauth2client/contrib/django*
rm -rf tests/contrib/django_util/
%endif

# Remove keyring support
rm oauth2client/contrib/keyring_storage.py tests/contrib/test_keyring_storage.py
# XsrfUtilTests.testGenerateAndValidateToken - broken parameters with py 3.8 and newer
rm tests/contrib/test_xsrfutil.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.contrib.django_util.settings
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%dir %{python_sitelib}/oauth2client
%dir %{python_sitelib}/oauth2client-%{version}-py*.egg-info
%exclude %{python_sitelib}/oauth2client/contrib/django*
%exclude %{python_sitelib}/oauth2client/contrib/flask*
%exclude %{python_sitelib}/oauth2client/contrib/__pycache__/flask*
%exclude %{python_sitelib}/oauth2client/contrib/gce*
%exclude %{python_sitelib}/oauth2client/contrib/__pycache__/gce*
%{python_sitelib}/oauth2client/*
%{python_sitelib}/oauth2client-%{version}-py*.egg-info/*

%files %{python_files flask}
%{python_sitelib}/oauth2client/contrib/flask*
%pycache_only %{python_sitelib}/oauth2client/contrib/__pycache__/flask*

%if %{with django}
%files %{python_files django}
%{python_sitelib}/oauth2client/contrib/django*
%pycache_only %{python_sitelib}/oauth2client/contrib/__pycache__/django*
%endif

%files %{python_files gce}
%{python_sitelib}/oauth2client/contrib/gce*
%pycache_only %{python_sitelib}/oauth2client/contrib/__pycache__/gce*

%changelog
