#
# spec file for package python-oslo.policy
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


Name:           python-oslo.policy
Version:        2.1.1
Release:        0
Summary:        OpenStack Oslo Policy library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.policy
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.policy/oslo.policy-2.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.context >= 2.22.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-devel
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.22.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
Requires:       python-PyYAML >= 3.12
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.22.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
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
The OpenStack Oslo Policy library.
RBAC policy enforcement library for OpenStack.

%package -n python-oslo.policy-doc
Summary:        Documentation for the Oslo Policy library
Group:          Documentation/HTML
BuildRequires:  python2-Sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.policy-doc
Documentation for the Oslo Policy library.

%prep
%autosetup -p1 -n oslo.policy-2.1.1
%py_req_cleanup

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-checker
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-list-redundant
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-policy-generator
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-sample-generator
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-policy-upgrade

%post
%{python_install_alternative oslopolicy-checker oslopolicy-list-redundant oslopolicy-policy-generator oslopolicy-sample-generator}

%postun
%python_uninstall_alternative oslopolicy-checker

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/oslopolicy-checker
%python_alternative %{_bindir}/oslopolicy-list-redundant
%python_alternative %{_bindir}/oslopolicy-policy-generator
%python_alternative %{_bindir}/oslopolicy-sample-generator
%python_alternative %{_bindir}/oslopolicy-policy-upgrade
%{python_sitelib}/oslo_policy
%{python_sitelib}/*.egg-info

%files -n python-oslo.policy-doc
%license LICENSE
%doc doc/build/html

%changelog
