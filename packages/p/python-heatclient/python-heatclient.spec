#
# spec file for package python-heatclient
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-heatclient
Version:        3.1.0
Release:        0
Summary:        Python API and CLI for OpenStack Heat
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-heatclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-heatclient/python-heatclient-3.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-osc-lib >= 1.14.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-swiftclient >= 3.2.0
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python3-Babel >= 2.3.4
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-PyYAML >= 3.13
Requires:       python3-cliff >= 2.8.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-keystoneauth1 >= 3.8.0
Requires:       python3-osc-lib >= 1.14.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-swiftclient >= 3.2.0
BuildArch:      noarch

%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.

%package -n python3-heatclient
Summary:        Python API and CLI for OpenStack Heat
Requires:       python3-Babel >= 2.3.4
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-PyYAML >= 3.13
Requires:       python3-cliff >= 2.8.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-keystoneauth1 >= 3.8.0
Requires:       python3-osc-lib >= 1.14.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-swiftclient >= 3.2.0
%if 0%{?suse_version}
Obsoletes:      python2-heatclient < 2.0.0
%endif

%description -n python3-heatclient
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.

%package -n python-heatclient-doc
Summary:        Documentation for OpenStack Heat API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-heatclient-doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-heatclient-3.1.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=3.1.0 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=3.1.0 %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# man page
install -p -D -m 644 doc/build/man/heat.1 %{buildroot}%{_mandir}/man1/heat.1
# bash completion
install -p -D -m 644 tools/heat.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/heat.bash_completion

%check
python3 -m stestr.cli run

%files -n python3-heatclient
%license LICENSE
%{python3_sitelib}/heatclient
%{python3_sitelib}/*.egg-info
%{_bindir}/heat
%{_mandir}/man1/heat.1*
%{_sysconfdir}/bash_completion.d/heat.bash_completion

%files -n python-heatclient-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
