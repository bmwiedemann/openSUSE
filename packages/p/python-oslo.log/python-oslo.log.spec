#
# spec file for package python-oslo.log
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


Name:           python-oslo.log
Version:        7.2.1
Release:        0
Summary:        OpenStack log library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.log
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_log/oslo_log-%{version}.tar.gz
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.context >= 2.21.0}
BuildRequires:  %{python_module oslo.i18n >= 3.20.0}
BuildRequires:  %{python_module oslo.serialization >= 2.25.0}
BuildRequires:  %{python_module oslo.utils >= 3.36.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil >= 2.7.0}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  openstack-macros
Requires:       python-debtcollector >= 3.0.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.21.0
Requires:       python-oslo.i18n >= 3.20.0
Requires:       python-oslo.serialization >= 2.25.0
Requires:       python-oslo.utils >= 3.36.0
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-systemd
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.log < %{version}
%else
Conflicts:      python3-oslo.log < %{version}
%endif
%python_subpackages

%description
OpenStack logging configuration library provides standardized configuration
for all openstack projects.It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

%package -n python-oslo.log-doc
Summary:        Documentation for OpenStack log library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.log-doc
Documentation for the oslo.log library.

%prep
%autosetup -p1 -n oslo_log-%{version}

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=. PBR_VERSION=7.1.0 %{sphinx_build} -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%python_clone -a %{buildroot}%{_bindir}/convert-json

%pre
%python_libalternatives_reset_alternative convert-json

%post
%python_install_alternative convert-json

%postun
%python_uninstall_alternative convert-json

%if 0%{?suse_version} > 1600
%check
%{openstack_stestr_run}
%endif

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/convert-json
%{python_sitelib}/oslo_log
%{python_sitelib}/oslo_log-%{version}.dist-info

%files -n python-oslo.log-doc
%license LICENSE
%doc doc/build/html

%changelog
