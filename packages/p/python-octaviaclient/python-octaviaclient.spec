#
# spec file for package python-octaviaclient
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


Name:           python-octaviaclient
Version:        1.8.1
Release:        0
Summary:        Octavia Plugin for the OpenStack Command-line Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-octaviaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-octaviaclient/python-octaviaclient-1.8.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-mock
BuildRequires:  python2-openstackclient >= 3.12.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient >= 3.12.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
Requires:       python-Babel >= 2.3.4
Requires:       python-appdirs >= 1.3.0
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-neutronclient >= 6.7.0
Requires:       python-openstackclient >= 3.12.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.

%package -n python-octaviaclient-doc
Summary:        Documentation for OpenStack Octavia API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description -n python-octaviaclient-doc
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-octaviaclient-1.8.1
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=1.8.1 sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/octaviaclient
%{python_sitelib}/*.egg-info

%files -n python-octaviaclient-doc
%license LICENSE
%doc doc/build/html

%changelog
