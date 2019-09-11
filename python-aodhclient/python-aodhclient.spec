#
# spec file for package python-aodhclient
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


%global sname aodhclient
Name:           python-aodhclient
Version:        1.2.0
Release:        0
Summary:        Python client library for Aodh
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/openstack/python-aodhclient
Source0:        https://files.pythonhosted.org/packages/source/a/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-cliff >= 1.14.0
BuildRequires:  python-keystoneauth1 >= 1.0.0
BuildRequires:  python-oslo.serialization >= 1.4.0
BuildRequires:  python-oslo.utils >= 2.0.0
BuildRequires:  python-oslotest
BuildRequires:  python-pbr >= 1.4
BuildRequires:  python-pyparsing
BuildRequires:  python-python-subunit
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  python-testrepository
BuildRequires:  python-testtools
Requires:       python-cliff >= 1.14.0
Requires:       python-debtcollector
Requires:       python-keystoneauth1 >= 1.0.0
Requires:       python-osc-lib >= 1.0.1
Requires:       python-oslo.i18n >= 1.5.0
Requires:       python-oslo.serialization >= 1.4.0
Requires:       python-oslo.utils >= 2.0.0
Requires:       python-pbr >= 1.4
Requires:       python-pyparsing
Requires:       python-six
BuildArch:      noarch

%description
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.

%package doc
Summary:        Documentation for OpenStack Aodh API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description      doc
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.

This package contains auto-generated documentation.

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup

%build
%py2_build

%install
%py2_install

PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -r doc/build/html/.{doctrees,buildinfo}

%check
# FIXME: only run unittests for now.
export OS_TEST_PATH=./aodhclient/tests/unit
PYTHONPATH=. %{__python2} setup.py testr

%files
%doc README.rst
%license LICENSE
%{_bindir}/aodh
%{python2_sitelib}/aodhclient
%{python2_sitelib}/*.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
