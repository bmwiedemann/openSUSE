#
# spec file for package python-oslo.metrics
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.6.0
Release:        0
Epoch:          0
Summary:        Collect metrics data from other Oslo libraries
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.metrics
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.metrics/oslo.metrics-0.6.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-oslo.config >= 6.9.0
BuildRequires:  python3-oslo.log >= 3.44.0
BuildRequires:  python3-oslo.utils >= 3.41.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 3.1.1
BuildRequires:  python3-prometheus-client >= 0.6.0
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
This Oslo metrics API supports collecting metrics data from other
Oslo libraries and exposing the metrics data to monitoring system.

%package -n python3-oslo.metrics
Summary:        Common code to collect metrics data from other Oslo libraries
Requires:       python3-oslo.config >= 6.9.0
Requires:       python3-oslo.log >= 3.44.0
Requires:       python3-oslo.utils >= 3.41.0
Requires:       python3-pbr >= 3.1.1
Requires:       python3-prometheus-client >= 0.6.0

%description -n python3-oslo.metrics
This Oslo metrics API supports collecting metrics data from other
Oslo libraries and exposing the metrics data to monitoring system.

This package contains the Python 3.x module.

%package -n python-oslo.metrics-doc
Summary:        Docs for oslo.metrics
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.metrics-doc
Documentation for the oslo.metrics library.

%prep
%autosetup -p1 -n oslo.metrics-0.6.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=0.6.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
export PYTHONPATH=`pwd`
%{openstack_stestr_run}

%files -n python3-oslo.metrics
%license LICENSE
%{_bindir}/oslo-metrics
%{python3_sitelib}/oslo_metrics
%{python3_sitelib}/*.egg-info

%files -n python-oslo.metrics-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
