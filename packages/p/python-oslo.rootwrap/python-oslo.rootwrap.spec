#
# spec file for package python-oslo.rootwrap
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        7.7.0
Release:        0
Summary:        Filtering shell commands to run as root from OpenStack services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.rootwrap
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_rootwrap/oslo_rootwrap-%{version}.tar.gz
BuildRequires:  %{python_module debtcollector}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  iproute2
BuildRequires:  openstack-macros
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.rootwrap < %{version}
%else
Conflicts:      python3-oslo.rootwrap < %{version}
%endif
%python_subpackages

%description
oslo.rootwrap allows fine-grained filtering of shell commands to run as root
from OpenStack services.

%package -n python-oslo.rootwrap-doc
Summary:        Documentation for OpenStack oslo.rootwrap
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.rootwrap-doc
Documentation for the OpenStack oslo.rootwrap library.

%prep
%autosetup -p1 -n oslo_rootwrap-%{version}
%py_req_cleanup

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/oslo-rootwrap
%python_clone -a %{buildroot}%{_bindir}/oslo-rootwrap-daemon

%pre
%python_libalternatives_reset_alternative oslo-rootwrap
%python_libalternatives_reset_alternative oslo-rootwrap-daemon

%post
%python_install_alternative oslo-rootwrap
%python_install_alternative oslo-rootwrap-daemon

%postun
%python_uninstall_alternative oslo-rootwrap
%python_uninstall_alternative oslo-rootwrap-daemon

%check
export PYTHONPATH=.
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/oslo-rootwrap
%python_alternative %{_bindir}/oslo-rootwrap-daemon
%{python_sitelib}/oslo_rootwrap
%{python_sitelib}/oslo_rootwrap-%{version}.dist-info

%files -n python-oslo.rootwrap-doc
%license LICENSE
%doc doc/build/html

%changelog
