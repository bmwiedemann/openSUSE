#
# spec file for package python-freezerclient
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


Name:           python-freezerclient
Version:        2.1.0
Release:        0
Summary:        Python API and CLI for OpenStack Freezer
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-freezerclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-freezerclient/python-freezerclient-2.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-cliff >= 2.8.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.i18n
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-setuptools >= 21.0.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testtools
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.i18n
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-setuptools >= 21.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneclient
Requires:       python-oslo.config
Requires:       python-oslo.i18n
Requires:       python-oslo.log
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-six
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
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).

%package -n python-freezerclient-doc
Summary:        Documentation for OpenStack Freezer API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-freezerclient-doc
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).
This package contains the documentation.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{python_build}

# Build HTML docs and man page
PBR_VERSION=2.1.0 sphinx-build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/freezer

%post
%python_install_alternative freezer

%postun
%python_uninstall_alternative freezer

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/freezerclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/freezer

%files -n python-freezerclient-doc
%doc doc/build/html
%license LICENSE

%changelog
