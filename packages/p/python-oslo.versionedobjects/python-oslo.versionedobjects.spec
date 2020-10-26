#
# spec file for package python-oslo.versionedobjects
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


Name:           python-oslo.versionedobjects
Version:        2.3.0
Release:        0
Summary:        Oslo Versioned Objects library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.versionedobjects
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.versionedobjects/oslo.versionedobjects-2.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-iso8601 >= 0.1.11
BuildRequires:  python3-jsonschema
BuildRequires:  python3-oslo.concurrency >= 3.26.0
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.19.2
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.messaging >= 5.29.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

%package -n python3-oslo.versionedobjects
Summary:        Oslo Versioned Objects library
Group:          Development/Languages/Python
Requires:       python3-WebOb >= 1.7.1
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-oslo.concurrency >= 3.26.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.context >= 2.19.2
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.messaging >= 5.29.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-six

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
%autosetup -p1 -n oslo.versionedobjects-2.3.0
%py_req_cleanup

%build
%py3_build

PYTHONPATH=. PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
python3 -m stestr.cli run

%files -n python3-oslo.versionedobjects
%license LICENSE
%{python3_sitelib}/oslo_versionedobjects
%{python3_sitelib}/*.egg-info

%files -n python-oslo.versionedobjects-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
