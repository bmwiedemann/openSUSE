#
# spec file for package python-glareclient
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


%global sname python-glareclient
Name:           python-glareclient
Version:        0.5.3
Release:        0
Summary:        Python API and CLI for OpenStack Glare
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PyYAML
BuildRequires:  python-coverage
BuildRequires:  python-devel
BuildRequires:  python-fixtures
BuildRequires:  python-mock
BuildRequires:  python-os-client-config
BuildRequires:  python-osc-lib >= 1.7.0
BuildRequires:  python-oslo.log >= 3.30.0
BuildRequires:  python-oslo.utils >= 3.31.0
BuildRequires:  python-reno
BuildRequires:  python-requests-mock
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-keystoneauth1 >= 3.2.0
Requires:       python-osc-lib >= 1.7.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.30.0
Requires:       python-oslo.utils >= 3.31.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.9.0
BuildArch:      noarch

%description
Python bindings to the Glare Artifact Repository

%package doc
Summary:        Documentation for OpenStack Glare API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-oslosphinx

%description      doc
Python bindings to the Glare Artifact Repository
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n %{sname}-%{version}
%py_req_cleanup

%build
%py2_build

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py2_install

%check
%{__python2} setup.py testr

%files
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/glare
%{python2_sitelib}/glareclient
%{python2_sitelib}/*.egg-info

%files doc
%license LICENSE
%doc doc/build/html

%changelog
