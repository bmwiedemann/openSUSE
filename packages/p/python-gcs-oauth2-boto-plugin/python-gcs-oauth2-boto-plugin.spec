#
# spec file for package python-gcs-oauth2-boto-plugin
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-gcs-oauth2-boto-plugin
Version:        1.14
Release:        0
Url:            https://github.com/GoogleCloudPlatform/gcs-oauth2-boto-plugin
Summary:        GCE Storage plugin for OAuth2
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         gcs-oauth2-boto-plugin-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python
BuildRequires:  python-setuptools
Requires:       python-SocksiPy        >= 1.01
Requires:       python-boto            >= 2.29.1
Requires:       python-httplib2        >= 0.8
Requires:       python-oauth2client    > 2.1.0
Requires:       python-pyOpenSSL       >= 0.13
Requires:       python-retry_decorator >= 1.0.0
Requires:       python-six             >= 1.6.1

%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
gcs-oauth2-boto-plugin is a Python application whose purpose is to behave
as an auth plugin for the boto auth plugin framework for use with OAuth 2.0
credentials for the Google Cloud Platform. This plugin is compatible with
both user accounts and service accounts, and its functionality is essentially
a wrapper around the oauth2client package of google-api-python-client with
the addition of automatically caching tokens for the machine in a thread-
and process-safe fashion.

%prep
%setup -q -n gcs-oauth2-boto-plugin-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{python_sitelib}/*

%changelog
