#
# spec file for package python-cinderclient
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


Name:           python-cinderclient
Version:        7.2.0
Release:        0
Summary:        Python API and CLI for OpenStack Cinder
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-cinderclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-cinderclient/python-cinderclient-7.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable >= 0.7.1
BuildRequires:  python3-ddt
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.serialization
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.

%package -n python3-cinderclient
Summary:        Python API and CLI for OpenStack Cinder
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-PrettyTable >= 0.7.1
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-simplejson >= 3.5.1
Requires:       python3-six >= 1.10.0
%if 0%{?suse_version}
Obsoletes:      python2-cinderclient < 6.0.0
%endif

%description -n python3-cinderclient
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.

This package contains the Python 3.x module.

%package -n python-cinderclient-doc
Summary:        Documentation for OpenStack Cinder API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python-cinderclient-doc
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-cinderclient-7.2.0
%py_req_cleanup

%build
%{py3_build}

export PYTHONPATH=.
PBR_VERSION=7.2.0 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=7.2.0 %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# man page
install -p -D -m 644 doc/build/man/cinder.1 %{buildroot}%{_mandir}/man1/cinder.1
# bash completion
install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%check
rm cinderclient/tests/unit/test_shell.py
python3 -m stestr.cli run

%files -n python3-cinderclient
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/cinderclient
%{python3_sitelib}/*.egg-info
%{_bindir}/cinder
%{_mandir}/man1/cinder.1*
%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%files -n python-cinderclient-doc
%license LICENSE
%doc doc/build/html

%changelog
