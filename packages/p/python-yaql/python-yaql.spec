#
# spec file for package python-yaql
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


Name:           python-yaql
Version:        3.2.0
Release:        0
Summary:        YAQL - Yet Another Query Language
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/yaql
Source0:        https://files.pythonhosted.org/packages/source/y/yaql/yaql-%{version}.tar.gz
BuildRequires:  openstack-macros
# for testing
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
Requires:       python-python-dateutil
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-yaql < %{version}
%else
Conflicts:      python3-yaql < %{version}
%endif
%python_subpackages

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query
language, that allows performing complex queries against arbitrary objects. It
has a vast and comprehensive standard library of frequently used querying
functions and can be extend even further with user-specified functions. YAQL is
written in python and is distributed via PyPI.

%prep
%autosetup -p1 -n yaql-%{version}
%py_req_cleanup

%build
%pyproject_wheel

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/yaql

%pre
%python_libalternatives_reset_alternative yaql

%post
%python_install_alternative yaql

%postun
%python_uninstall_alternative yaql

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/yaql
%{python_sitelib}/yaql
%{python_sitelib}/yaql-%{version}.dist-info

%changelog
