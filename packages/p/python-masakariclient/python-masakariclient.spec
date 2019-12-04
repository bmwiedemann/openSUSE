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


%global oldpython python
Name:           python-masakariclient
Version:        5.5.0
Release:        0
Summary:        Python API and CLI for OpenStack Masakari
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-masakariclient/python-masakariclient-5.5.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PrettyTable
BuildRequires:  python2-ddt
BuildRequires:  python2-nose
BuildRequires:  python2-openstacksdk >= 0.13.0
BuildRequires:  python2-osc-lib >= 1.8.0
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils
BuildRequires:  python2-oslotest
BuildRequires:  python2-python-subunit
BuildRequires:  python2-requests-mock
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PrettyTable
BuildRequires:  python3-ddt
BuildRequires:  python3-nose
BuildRequires:  python3-openstacksdk >= 0.13.0
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils
BuildRequires:  python3-oslotest
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests-mock
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-openstacksdk >= 0.13.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils
Requires:       python-pbr >= 2.0.0
Conflicts:      %oldpython-masakariclient < %version
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
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).

%package -n python-masakariclient-doc
Summary:        Documentation for OpenStack Masakari API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
%if 0%{?suse_version}
Obsoletes:      %oldpython-masakariclient < %version
%endif

%description -n python-masakariclient-doc
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).
This package contains the documentation.

%prep
%autosetup -p1 -n python-masakariclient-%{version}
%py_req_cleanup

%build
%{python_build}

# Build HTML docs and man page
PBR_VERSION=5.5.0 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=5.5.0 %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/masakari
# man pages
install -p -D -m 644 doc/build/man/python-masakariclient.1 %{buildroot}%{_mandir}/man1/python-masakariclient.1

%check
find . -type f -name *.pyc -delete
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_version} masakariclient/tests/unit

%post
%python_install_alternative masakari

%postun
%python_uninstall_alternative masakari

%files %python_files
%license LICENSE
%{python_sitelib}/masakariclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/masakari

%files -n python-masakariclient-doc
%license LICENSE
%doc doc/build/html
%{_mandir}/man1/python-masakariclient.1.*

%changelog
