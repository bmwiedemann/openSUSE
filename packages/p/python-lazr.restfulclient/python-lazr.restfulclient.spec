#
# spec file for package python-lazr.restfulclient
#
# Copyright (c) 2021 SUSE LLC
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


Name:           python-lazr.restfulclient
Version:        0.14.5
Release:        0
Summary:        Programmable client library to provide added functionality on top of wadllib
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/lazr.restfulclient
Source:         https://launchpad.net/lazr.restfulclient/trunk/%{version}/+download/lazr.restfulclient-%{version}.tar.gz
# PATCH-FIX-UPSTREAM replace obsolete readfp with read_file
Patch1:         fix_readfp.patch
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wadllib}
BuildRequires:  %{python_module wsgi_intercept}
BuildRequires:  %{python_module zope.testrunner}
Requires:       python-distro
Requires:       python-httplib2
Requires:       python-oauthlib
Requires:       python-setuptools
Requires:       python-six
Requires:       python-wadllib >= 1.1.4
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A programmable client library that takes advantage of the commonalities among lazr.restful
web services to provide added functionality on top of wadllib.

%prep
%autosetup -n lazr.restfulclient-%{version} -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests would additionally need packages lazr.restful and lazr.authenticate
#%#pytest

%files %{python_files}
%license COPYING.txt
%doc README.rst NEWS.rst
%dir %{python_sitelib}/lazr
%{python_sitelib}/lazr/restfulclient*
%{python_sitelib}/lazr.restfulclient*

%changelog
