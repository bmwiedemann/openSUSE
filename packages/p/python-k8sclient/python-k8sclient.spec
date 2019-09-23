#
# spec file for package python-k8sclient
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


Name:           python-k8sclient
Version:        0.4.0
Release:        0
Summary:        Python API and CLI for OpenStack K8s
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-oslotest
BuildRequires:  python-pbr >= 1.6
BuildRequires:  python-python-dateutil >= 2.4.2
BuildRequires:  python-python-subunit
BuildRequires:  python-setuptools
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-urllib3 >= 1.8.3
Requires:       python-pbr >= 1.6
Requires:       python-python-dateutil >= 2.4.2
Requires:       python-six >= 1.9.0
Requires:       python-urllib3 >= 1.8.3
BuildArch:      noarch

%description
Client library for K8s built on the K8s API. It provides a Python API
(the k8sclient module) and a command-line tool (k8s).

%package doc
Summary:        Documentation for OpenStack K8s API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-oslosphinx

%description doc
Client library for K8s built on the K8s API. It provides a Python API
(the k8sclient module) and a command-line tool (k8s).
This package contains the documentation.

%prep
%autosetup -n %{name}-%{version}
%py_req_cleanup

%build
%py2_build

# Build HTML docs and man page
%{__python2} setup.py build_sphinx
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install

%check
%{__python2} setup.py testr

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/k8sclient
%{python2_sitelib}/*.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
