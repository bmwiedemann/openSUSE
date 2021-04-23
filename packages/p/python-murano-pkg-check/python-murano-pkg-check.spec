#
# spec file for package python-murano-pkg-check
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


Name:           python-murano-pkg-check
Version:        0.3.0
Release:        0
Summary:        Murano package validator tool
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/murano/
Source0:        https://files.pythonhosted.org/packages/source/m/murano-pkg-check/murano-pkg-check-0.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 3.10.0
BuildRequires:  python3-oslo.i18n >= 2.1.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 1.8
BuildRequires:  python3-python-subunit
BuildRequires:  python3-semantic_version
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.17.1
BuildRequires:  python3-testscenarios
BuildRequires:  python3-yaql >= 1.1.0
BuildArch:      noarch

%description
Murano package validator tool

%package -n python3-murano-pkg-check
Summary:        Murano package validator tool
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.10.0
Requires:       python3-oslo.i18n >= 2.1.0
Requires:       python3-semantic_version
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.17.1
Requires:       python3-yaql >= 1.1.0
%if 0%{?suse_version}
Obsoletes:      python2-murano-pkg-check < 0.3.1
%endif

%description -n python3-murano-pkg-check
Murano package validator tool

%prep
%autosetup -n murano-pkg-check-%{version}
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} -m stestr.cli --test-path=./muranopkgcheck/tests/ \
  run \
  --black-regex=muranopkgcheck.tests.test_manager.ManagerTest.test_validate

%files -n python3-murano-pkg-check
%doc README.rst
%license LICENSE
%{_bindir}/murano-pkg-check
%{python3_sitelib}/muranopkgcheck
%{python3_sitelib}/*.egg-info

%changelog
