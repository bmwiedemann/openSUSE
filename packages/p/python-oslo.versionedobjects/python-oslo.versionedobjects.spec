#
# spec file for package python-oslo.versionedobjects
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


Name:           python-oslo.versionedobjects
Version:        3.8.0
Release:        0
Summary:        Oslo Versioned Objects library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.versionedobjects
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_versionedobjects/oslo_versionedobjects-%{version}.tar.gz
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module oslo.concurrency >= 3.26.0}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.context >= 2.19.2}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.log >= 3.36.0}
BuildRequires:  %{python_module oslo.messaging >= 5.29.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 7.4.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-WebOb >= 1.7.1
Requires:       python-iso8601
Requires:       python-netaddr >= 0.7.18
Requires:       python-oslo.concurrency >= 3.26.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.messaging >= 5.29.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 7.4.0
BuildArch:      noarch
%python_subpackages

%description
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

%package -n python3-oslo.versionedobjects
Summary:        Oslo Versioned Objects library

%description -n python3-oslo.versionedobjects
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

This package contains the Python 3.x module.

%package -n python-oslo.versionedobjects-doc
Summary:        osloversionedobjects library - Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.versionedobjects-doc
This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n oslo_versionedobjects-%{version}

%build
%pyproject_wheel

PYTHONPATH=. PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/oslo_versionedobjects
%{python_sitelib}/oslo_versionedobjects-%{version}.dist-info

%files -n python-oslo.versionedobjects-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
