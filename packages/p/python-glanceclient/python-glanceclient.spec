#
# spec file for package python-glanceclient
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


Name:           python-glanceclient
Version:        2.16.0
Release:        0
Summary:        Python API and CLI for OpenStack Glance
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-glanceclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-glanceclient/python-glanceclient-2.16.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PrettyTable >= 0.7.1
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-mock
BuildRequires:  python2-os-client-config
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-pyOpenSSL >= 17.1.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-warlock >= 1.2.0
BuildRequires:  python3-PrettyTable >= 0.7.1
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mock
BuildRequires:  python3-os-client-config
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-pyOpenSSL >= 17.1.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-warlock >= 1.2.0
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-keystoneauth1 >= 3.6.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-pyOpenSSL >= 17.1.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-warlock >= 1.2.0
Requires:       python-wrapt >= 1.7.0
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
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%package -n python-glanceclient-doc
Summary:        Documentation for OpenStack Glance API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno
BuildRequires:  python-sphinxcontrib-apidoc

%description -n python-glanceclient-doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-glanceclient-2.16.0
%py_req_cleanup

%build
%python_build

# generate html docs
PBR_VERSION=2.16.0 sphinx-build -b html doc/source doc/build/html
PBR_VERSION=2.16.0 sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install
#man pages
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1
%python_clone -a %{buildroot}%{_bindir}/glance
%python_clone -a %{buildroot}%{_mandir}/man1/glance.1

%post
%{python_install_alternative glance glance.1}

%postun
%python_uninstall_alternative glance

%check
%if 0%{?rhel} || 0%{?fedora}
# disable tests until rdo updated to requests > 2.14
true
%else
%python_exec -m stestr.cli run

%endif

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%python_alternative %{_bindir}/glance
%python_alternative %{_mandir}/man1/glance.1
%{python_sitelib}/glanceclient
%{python_sitelib}/*.egg-info

%files -n python-glanceclient-doc
%license LICENSE
%doc doc/build/html

%changelog
