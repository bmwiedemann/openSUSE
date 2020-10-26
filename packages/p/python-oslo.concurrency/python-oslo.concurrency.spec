#
# spec file for package python-oslo.concurrency
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


Name:           python-oslo.concurrency
Version:        4.3.0
Release:        0
Summary:        OpenStack oslo.concurrency library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.concurrency
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.concurrency/oslo.concurrency-4.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-eventlet
BuildRequires:  python3-fasteners >= 0.7.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package -n python3-oslo.concurrency
Summary:        OpenStack oslo.concurrency library
Group:          Development/Languages/Python
Requires:       python3-fasteners >= 0.7.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-six
%if 0%{?suse_version}
Obsoletes:      python2-oslo.concurrency < 4.0.0
%endif

%description -n python3-oslo.concurrency
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

This package contains the Python 3.x module.

%package -n python-oslo.concurrency-doc
Summary:        Documentation for OpenStack concurrency library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.concurrency-doc
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.concurrency-4.3.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-oslo.concurrency
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/lockutils-wrapper
%{python3_sitelib}/oslo_concurrency
%{python3_sitelib}/*.egg-info

%files -n python-oslo.concurrency-doc
%license LICENSE
%doc doc/build/html

%changelog
