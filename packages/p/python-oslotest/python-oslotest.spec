#
# spec file for package python-oslotest
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.4.1
Release:        0
Summary:        OpenStack test framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslotest
Source0:        https://files.pythonhosted.org/packages/source/o/oslotest/oslotest-4.4.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-debtcollector
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-mock
BuildRequires:  python3-pbr
BuildRequires:  python3-python-subunit >= 1.0.0
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools >= 2.2.0
BuildArch:      noarch

%description
The Oslo Test framework provides common fixtures, support for debugging, and
better support for mocking results.

%package -n python3-oslotest
Summary:        OpenStack test framework
Group:          Development/Languages/Python
Requires:       python3-debtcollector
Requires:       python3-fixtures >= 3.0.0
Requires:       python3-mock
# NOTE: python-os-client-config is only needed for functional testing
# Requires:       python3-os-client-config
Requires:       python3-python-subunit >= 1.0.0
Requires:       python3-six >= 1.10.0
Requires:       python3-stestr
Requires:       python3-testtools >= 2.2.0

%description -n python3-oslotest
The Oslo Test framework provides common fixtures, support for debugging, and
better support for mocking results.

This package contains the Python 3.x module.

%prep
%autosetup -p1 -n oslotest-%{version}
%py_req_cleanup

%build
%py3_build

%install
%py3_install

%check
python3 -m stestr.cli run

%files -n python3-oslotest
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/oslo_debug_helper
%{_bindir}/oslo_run_cross_tests
%{_bindir}/oslo_run_pre_release_tests
%{python3_sitelib}/oslotest
%{python3_sitelib}/oslotest*egg-info

%changelog
