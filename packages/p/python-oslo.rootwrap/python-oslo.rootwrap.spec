#
# spec file for package python-oslo.rootwrap
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


Name:           python-oslo.rootwrap
Version:        5.15.2
Release:        0
Summary:        Filtering shell commands to run as root from OpenStack services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.rootwrap
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.rootwrap/oslo.rootwrap-5.15.2.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-eventlet
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testtools
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  iproute2
%else
BuildRequires:  iproute
%endif
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
oslo.rootwrap allows fine-grained filtering of shell commands to run as root
from OpenStack services.

%package -n python-oslo.rootwrap-doc
Summary:        Documentation for OpenStack oslo.rootwrap
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.rootwrap-doc
Documentation for the OpenStack oslo.rootwrap library.

%prep
%autosetup -p1 -n oslo.rootwrap-5.15.2
%py_req_cleanup

%build
%{python_build}

# generate html docs
PBR_VERSION=5.15.2 sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/oslo-rootwrap
%python_clone -a %{buildroot}%{_bindir}/oslo-rootwrap-daemon

%post
%python_install_alternative oslo-rootwrap
%python_install_alternative oslo-rootwrap-daemon

%postun
%python_uninstall_alternative oslo-rootwrap
%python_uninstall_alternative oslo-daemon

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/oslo_rootwrap
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/oslo-rootwrap
%python_alternative %{_bindir}/oslo-rootwrap-daemon

%files -n python-oslo.rootwrap-doc
%license LICENSE
%doc doc/build/html

%changelog
