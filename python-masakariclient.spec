#
# spec file for package python-masakariclient
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


%global sname python-masakariclient
Name:           python-masakariclient
Version:        5.4.0
Release:        0
Summary:        Python API and CLI for OpenStack Masakari
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PrettyTable
BuildRequires:  python-ddt
BuildRequires:  python-nose
BuildRequires:  python-openstacksdk >= 0.13.0
BuildRequires:  python-osc-lib >= 1.8.0
BuildRequires:  python-oslo.serialization >= 2.18.0
BuildRequires:  python-oslo.utils
BuildRequires:  python-oslotest
BuildRequires:  python-python-subunit
BuildRequires:  python-reno
BuildRequires:  python-requests-mock
BuildRequires:  python-sphinx
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
Requires:       python-openstacksdk >= 0.13.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch

%description
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).

%package doc
Summary:        Documentation for OpenStack Masakari API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-oslosphinx
BuildRequires:  python-sphinxcontrib-apidoc

%description doc
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).
This package contains the documentation.

%prep
%autosetup -p1 -n %{sname}-%{version}
%py_req_cleanup

%build
%py2_build

# Build HTML docs and man page
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
PBR_VERSION=%{version} sphinx-build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%py2_install
# man pages
install -p -D -m 644 doc/build/man/python-masakariclient.1 %{buildroot}%{_mandir}/man1/python-masakariclient.1

%check
find . -type f -name *.pyc -delete
PYTHONPATH=. nosetests masakariclient/tests/unit

%files
%license LICENSE
%{python2_sitelib}/masakariclient
%{python2_sitelib}/*.egg-info
%{_mandir}/man1/python-masakariclient.1.*
%{_bindir}/masakari

%files doc
%license LICENSE
%doc doc/build/html

%changelog
