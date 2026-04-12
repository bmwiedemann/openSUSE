#
# spec file for package python-oslotest
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-oslotest%{psuffix}
Version:        6.1.0
Release:        0
Summary:        OpenStack test framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslotest
Source0:        https://files.pythonhosted.org/packages/source/o/oslotest/oslotest-%{version}.tar.gz
BuildRequires:  %{python_module pbr >= 6.1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module python-subunit >= 1.0.0}
BuildRequires:  %{python_module stestr >= 2.0.0}
BuildRequires:  %{python_module testtools >= 2.2.0}
%endif
BuildRequires:  openstack-macros
Requires:       python-fixtures >= 3.0.0
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
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/oslo_debug_helper

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative oslo_debug_helper

%post
%python_install_alternative oslo_debug_helper

%postun
%python_uninstall_alternative oslo_debug_helper

%else

%check
%{openstack_stestr_run}
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/oslo_debug_helper
%{python_sitelib}/oslotest
%{python_sitelib}/oslotest-%{version}.dist-info
%endif

%changelog
