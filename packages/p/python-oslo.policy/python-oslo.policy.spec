#
# spec file for package python-oslo.policy
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


Name:           python-oslo.policy
Version:        4.6.0
Release:        0
Summary:        OpenStack Oslo Policy library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.policy
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_policy/oslo_policy-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module oslo.config >= 6.0.0}
BuildRequires:  %{python_module oslo.context >= 2.22.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.40.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.14.2}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-defusedxml
Requires:       python-oslo.config >= 6.0.0
Requires:       python-oslo.context >= 2.22.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.40.0
Requires:       python-requests >= 2.14.2
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.policy < %{version}
%else
Conflicts:      python3-oslo.policy < %{version}
%endif
%python_subpackages

%description
The OpenStack Oslo Policy library.
RBAC policy enforcement library for OpenStack.

%package -n python-oslo.policy-doc
Summary:        Documentation for the Oslo Policy library
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.policy-doc
Documentation for the Oslo Policy library.

%prep
%autosetup -p1 -n oslo_policy-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/oslopolicy-checker
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-convert-json-to-yaml
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-list-redundant
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-policy-generator
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-sample-generator
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-policy-upgrade
%python_clone -a %{buildroot}%{_bindir}/oslopolicy-validator

%pre
%python_libalternatives_reset_alternative oslopolicy-checker
%python_libalternatives_reset_alternative oslopolicy-convert-json-to-yaml
%python_libalternatives_reset_alternative oslopolicy-list-redundant
%python_libalternatives_reset_alternative oslopolicy-policy-generator
%python_libalternatives_reset_alternative oslopolicy-sample-generator
%python_libalternatives_reset_alternative oslopolicy-policy-upgrade
%python_libalternatives_reset_alternative oslopolicy-validator

%post
%python_install_alternative oslopolicy-checker
%python_install_alternative oslopolicy-convert-json-to-yaml
%python_install_alternative oslopolicy-list-redundant
%python_install_alternative oslopolicy-policy-generator
%python_install_alternative oslopolicy-sample-generator
%python_install_alternative oslopolicy-policy-upgrade
%python_install_alternative oslopolicy-validator

%postun
%python_uninstall_alternative oslopolicy-checker
%python_uninstall_alternative oslopolicy-convert-json-to-yaml
%python_uninstall_alternative oslopolicy-list-redundant
%python_uninstall_alternative oslopolicy-policy-generator
%python_uninstall_alternative oslopolicy-sample-generator
%python_uninstall_alternative oslopolicy-policy-upgrade
%python_uninstall_alternative oslopolicy-validator

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/oslopolicy-checker
%python_alternative %{_bindir}/oslopolicy-convert-json-to-yaml
%python_alternative %{_bindir}/oslopolicy-list-redundant
%python_alternative %{_bindir}/oslopolicy-policy-generator
%python_alternative %{_bindir}/oslopolicy-sample-generator
%python_alternative %{_bindir}/oslopolicy-policy-upgrade
%python_alternative %{_bindir}/oslopolicy-validator
%{python_sitelib}/oslo_policy
%{python_sitelib}/oslo_policy-%{version}.dist-info

%files -n python-oslo.policy-doc
%license LICENSE
%doc doc/build/html

%changelog
