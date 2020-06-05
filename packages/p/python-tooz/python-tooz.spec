#
# spec file for package python-tooz
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


%if 0%{?rhel} || 0%{?fedora}
%global rdo 1
%endif
Name:           python-tooz
Version:        2.1.0
Release:        0
Summary:        Coordination library for distributed systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/tooz/
Source0:        https://files.pythonhosted.org/packages/source/t/tooz/tooz-2.1.0.tar.gz
BuildRequires:  memcached
BuildRequires:  openstack-macros
BuildRequires:  python3-fasteners >= 0.7
BuildRequires:  python3-fixtures
BuildRequires:  python3-futurist >= 1.2.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.serialization >= 1.10.0
BuildRequires:  python3-oslo.utils >= 3.15.0
BuildRequires:  python3-pbr >= 1.6
BuildRequires:  python3-pymemcache
BuildRequires:  python3-stevedore >= 1.16.0
BuildRequires:  python3-tenacity >= 3.2.1
BuildRequires:  python3-testtools
BuildRequires:  python3-voluptuous >= 0.8.9
BuildArch:      noarch
%if ! 0%{?rdo}
BuildRequires:  python3-pifpaf
%endif

%description
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

%package -n python3-tooz
Summary:        Coordination library for distributed systems
Group:          Development/Languages/Python
Requires:       python3-fasteners >= 0.7
Requires:       python3-futurist >= 1.2.0
Requires:       python3-msgpack >= 0.4.0
Requires:       python3-oslo.serialization >= 1.10.0
Requires:       python3-oslo.utils >= 3.15.0
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.16.0
Requires:       python3-tenacity >= 3.2.1
Requires:       python3-voluptuous >= 0.8.9

%description -n python3-tooz
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

This package contains the Python 3.x module.

%package -n python-tooz-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description  -n python-tooz-doc
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n tooz-2.1.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PYTHONPATH=. \
    %sphinx_build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%if ! 0%{?rdo}
export TOOZ_TEST_DRIVERS="memcached"
export PATH=%{_prefix}/sbin:$PATH
export LC_ALL=en_US.UTF-8
bash run-tests.sh
%endif

%install
%{py3_install}

%files -n python3-tooz
%license LICENSE
%{python3_sitelib}/tooz
%{python3_sitelib}/tooz-*.egg-info

%files -n python-tooz-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
