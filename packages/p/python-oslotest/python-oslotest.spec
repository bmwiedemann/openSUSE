#
# spec file for package python-oslotest
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


Name:           python-oslotest
Version:        3.8.1
Release:        0
Summary:        OpenStack test framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslotest
Source0:        https://files.pythonhosted.org/packages/source/o/oslotest/oslotest-3.8.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-fixtures >= 3.0.0
BuildRequires:  python2-mock >= 2.0.0
BuildRequires:  python2-mox3 >= 0.20.0
BuildRequires:  python2-pbr
BuildRequires:  python2-python-subunit >= 1.0.0
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr >= 2.0.0
BuildRequires:  python2-testtools >= 2.2.0
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-mock >= 2.0.0
BuildRequires:  python3-mox3 >= 0.20.0
BuildRequires:  python3-pbr
BuildRequires:  python3-python-subunit >= 1.0.0
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr >= 2.0.0
BuildRequires:  python3-testtools >= 2.2.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-fixtures >= 3.0.0
Requires:       python-mock >= 2.0.0
Requires:       python-mox3 >= 0.20.0
# NOTE: python-os-client-config is only needed for functional testing
# Requires:       python-os-client-config >= 1.28.0
Requires:       python-python-subunit >= 1.0.0
Requires:       python-six >= 1.10.0
Requires:       python-stestr >= 2.0.0
Requires:       python-testtools >= 2.2.0
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
The Oslo Test framework provides common fixtures, support for debugging, and
better support for mocking results.

%prep
%autosetup -p1 -n oslotest-%{version}
%py_req_cleanup

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/oslo_debug_helper
%python_clone -a %{buildroot}%{_bindir}/oslo_run_cross_tests
%python_clone -a %{buildroot}%{_bindir}/oslo_run_pre_release_tests

%post
%python_install_alternative oslo_debug_helper
%python_install_alternative oslo_run_cross_tests
%python_install_alternative oslo_run_pre_release_tests

%postun
%python_uninstall_alternative oslo_debug_helper
%python_uninstall_alternative oslo_run_cross_tests
%python_uninstall_alternative oslo_run_pre_release_tests

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/oslo_debug_helper
%python_alternative %{_bindir}/oslo_run_cross_tests
%python_alternative %{_bindir}/oslo_run_pre_release_tests
%{python_sitelib}/oslotest
%{python_sitelib}/oslotest*egg-info

%changelog
