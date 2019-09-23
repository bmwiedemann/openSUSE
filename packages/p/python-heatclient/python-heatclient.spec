#
# spec file for package python-heatclient
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


Name:           python-heatclient
Version:        1.17.0
Release:        0
Summary:        Python API and CLI for OpenStack Heat
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-heatclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-heatclient/python-heatclient-1.17.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-cliff >= 2.8.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-mox3
BuildRequires:  python2-osc-lib >= 1.8.0
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-swiftclient >= 3.2.0
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-mox3
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-swiftclient >= 3.2.0
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.12
Requires:       python-cliff >= 2.8.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-swiftclient >= 3.2.0
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
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.

%package -n python-heatclient-doc
Summary:        Documentation for OpenStack Heat API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-heatclient-doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-heatclient-1.17.0
%py_req_cleanup

%build
%{python_build}

%{__python2} setup.py build_sphinx --builder=html,man
PBR_VERSION=1.17.0 sphinx-build -b html doc/source doc/build/html
PBR_VERSION=1.17.0 sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
# man page
install -p -D -m 644 doc/build/man/heat.1 %{buildroot}%{_mandir}/man1/heat.1
# bash completion
install -p -D -m 644 tools/heat.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/heat.bash_completion
%python_clone -a %{buildroot}%{_bindir}/heat
%python_clone -a %{buildroot}%{_mandir}/man1/heat.1
%python_clone -a %{buildroot}%{_sysconfdir}/bash_completion.d/heat.bash_completion

%post
%{python_install_alternative heat heat.1 %{_sysconfdir}/bash_completion.d/heat.bash_completion}

%postun
%python_uninstall_alternative heat

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%{python_sitelib}/heatclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/heat
%python_alternative %{_mandir}/man1/heat.1
%python_alternative %{_sysconfdir}/bash_completion.d/heat.bash_completion

%files -n python-heatclient-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
