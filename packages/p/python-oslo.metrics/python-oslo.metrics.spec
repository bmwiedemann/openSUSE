#
# spec file for package python-oslo.metrics
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


Name:           python-oslo.metrics
Version:        0.13.0
Release:        0
Summary:        Collect metrics data from other Oslo libraries
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.metrics
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_metrics/oslo_metrics-%{version}.tar.gz
BuildRequires:  %{python_module oslo.config >= 6.9.0}
BuildRequires:  %{python_module oslo.log >= 3.44.0}
BuildRequires:  %{python_module oslo.utils >= 3.41.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr >= 3.1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module prometheus-client >= 0.6.0}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-oslo.config >= 6.9.0
Requires:       python-oslo.log >= 3.44.0
Requires:       python-oslo.utils >= 3.41.0
Requires:       python-pbr >= 3.1.1
Requires:       python-prometheus-client >= 0.6.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.metrics < %{version}
%else
Conflicts:      python3-oslo.metrics < %{version}
%endif
%python_subpackages

%description
This Oslo metrics API supports collecting metrics data from other
Oslo libraries and exposing the metrics data to monitoring system.

%package -n python-oslo.metrics-doc
Summary:        Docs for oslo.metrics
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.metrics-doc
Documentation for the oslo.metrics library.

%prep
%autosetup -p1 -n oslo_metrics-%{version}

%build
%pyproject_wheel

PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/oslo-metrics

%pre
%python_libalternatives_reset_alternative oslo-metrics

%post
%python_install_alternative oslo-metrics

%postun
%python_uninstall_alternative oslo-metrics

%check
export PYTHONPATH=`pwd`
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/oslo-metrics
%{python_sitelib}/oslo_metrics
%{python_sitelib}/oslo_metrics-%{version}.dist-info

%files -n python-oslo.metrics-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
