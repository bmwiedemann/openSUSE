#
# spec file for package python-oslo.privsep
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


Name:           python-oslo.privsep
Version:        3.8.0
Release:        0
Summary:        OpenStack library for privilege separation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.privsep
Source0:        https://files.pythonhosted.org/packages/source/o/oslo-privsep/oslo_privsep-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.14.0}
BuildRequires:  %{python_module eventlet >= 0.21.0}
BuildRequires:  %{python_module greenlet >= 0.4.14}
BuildRequires:  %{python_module msgpack >= 0.6.0}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.log >= 5.0.2}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildArch:      noarch
Requires:       python-cffi >= 1.14.0
Requires:       python-eventlet >= 0.21.0
Requires:       python-greenlet >= 0.4.14
Requires:       python-msgpack >= 0.6.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 5.0.2
Requires:       python-oslo.utils >= 3.33.0
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.privsep < %{version}
%else
Conflicts:      python3-oslo.privsep < %{version}
%endif
%python_subpackages

%description
OpenStack library for privilege separation

%package -n python-oslo.privsep-doc
Summary:        oslo.privsep documentation
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.privsep-doc
Documentation for oslo.privsep

%prep
%autosetup -p1 -n oslo_privsep-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/privsep-helper

%pre
%python_libalternatives_reset_alternative privsep-helper

%post
%python_install_alternative privsep-helper

%postun
%python_uninstall_alternative privsep-helper

%check
export PYTHONPATH=.
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/privsep-helper
%{python_sitelib}/oslo_privsep
%{python_sitelib}/oslo_privsep-%{version}.dist-info

%files -n python-oslo.privsep-doc
%doc doc/build/html

%changelog
