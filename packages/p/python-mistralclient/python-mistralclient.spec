#
# spec file for package python-mistralclient
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


Name:           python-mistralclient
Version:        3.8.1
Release:        0
Summary:        Python API and CLI for OpenStack Mistral
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PyYAML >= 3.12
BuildRequires:  python-fixtures
BuildRequires:  python-mock
BuildRequires:  python-nose
BuildRequires:  python-openstackclient
BuildRequires:  python-oslotest
BuildRequires:  python-osprofiler
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-testrepository
BuildRequires:  python-testtools
Requires:       python-PyYAML >= 3.12
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneclient
Requires:       python-os-client-config
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-osprofiler
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch

%description
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).

%package doc
Summary:        Documentation for OpenStack Mistral API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-sphinxcontrib-apidoc

%description doc
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).
This package contains the documentation.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%py2_build

# Build HTML docs and man page
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
PBR_VERSION=%{version} sphinx-build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%py2_install
#man pages
install -p -D -m 644 doc/build/man/mistral_client.1 %{buildroot}%{_mandir}/man1/mistral_client.1

%check
find . -type f -name *.pyc -delete
PYTHONPATH=. nosetests mistralclient/tests/unit

%files
%license LICENSE
%{python2_sitelib}/mistralclient
%{python2_sitelib}/*.egg-info
%{_bindir}/mistral
%{_mandir}/man1/mistral_client.1.*

%files doc
%license LICENSE

%changelog
