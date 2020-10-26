#
# spec file for package python-oslo.policy
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


Name:           python-oslo.policy
Version:        3.5.0
Release:        0
Summary:        OpenStack Oslo Policy library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.policy
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.policy/oslo.policy-3.5.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 5.1
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.22.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.40.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
The OpenStack Oslo Policy library.
RBAC policy enforcement library for OpenStack.

%package -n python3-oslo.policy
Summary:        OpenStack Oslo Policy library
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 5.1
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.context >= 2.22.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.40.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
%if 0%{?suse_version}
Obsoletes:      python2-oslo.policy < 2.4.1
%endif

%description -n python3-oslo.policy
The OpenStack Oslo Policy library.
RBAC policy enforcement library for OpenStack.

This package contains the Python 3.x module.

%package -n python-oslo.policy-doc
Summary:        Documentation for the Oslo Policy library
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.policy-doc
Documentation for the Oslo Policy library.

%prep
%autosetup -p1 -n oslo.policy-3.5.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files  -n python3-oslo.policy
%license LICENSE
%doc README.rst
%{_bindir}/oslopolicy-checker
%{_bindir}/oslopolicy-convert-json-to-yaml
%{_bindir}/oslopolicy-list-redundant
%{_bindir}/oslopolicy-policy-generator
%{_bindir}/oslopolicy-sample-generator
%{_bindir}/oslopolicy-policy-upgrade
%{_bindir}/oslopolicy-validator
%{python3_sitelib}/oslo_policy
%{python3_sitelib}/*.egg-info

%files -n python-oslo.policy-doc
%license LICENSE
%doc doc/build/html

%changelog
