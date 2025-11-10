#
# spec file for package python-oslotest
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


Name:           python-oslotest
Version:        5.0.1
Release:        0
Summary:        OpenStack test framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslotest
Source0:        https://files.pythonhosted.org/packages/source/o/oslotest/oslotest-%{version}.tar.gz
BuildRequires:  %{python_module debtcollector}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit >= 1.0.0}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools >= 2.2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-fixtures
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslotest < %{version}
%else
Conflicts:      python3-oslotest < %{version}
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
The Oslo Test framework provides common fixtures, support for debugging, and
better support for mocking results.

%prep
%autosetup -p1 -n oslotest-%{version}
%py_req_cleanup

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/oslo_debug_helper
%python_clone -a %{buildroot}%{_bindir}/oslo_run_cross_tests
%python_clone -a %{buildroot}%{_bindir}/oslo_run_pre_release_tests

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative oslo_debug_helper
%python_libalternatives_reset_alternative oslo_run_cross_tests
%python_libalternatives_reset_alternative oslo_run_pre_release_tests

%post
%python_install_alternative oslo_debug_helper
%python_install_alternative oslo_run_cross_tests
%python_install_alternative oslo_run_pre_release_tests

%postun
%python_uninstall_alternative oslo_debug_helper
%python_uninstall_alternative oslo_run_cross_tests
%python_uninstall_alternative oslo_run_pre_release_tests

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/oslo_debug_helper
%python_alternative %{_bindir}/oslo_run_cross_tests
%python_alternative %{_bindir}/oslo_run_pre_release_tests
%{python_sitelib}/oslotest
%{python_sitelib}/oslotest-%{version}.dist-info

%changelog
