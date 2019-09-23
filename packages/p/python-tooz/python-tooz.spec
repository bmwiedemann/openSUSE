#
# spec file for package python-tooz
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


%if 0%{?rhel} || 0%{?fedora}
%global rdo 1
%endif
Name:           python-tooz
Version:        1.64.2
Release:        0
Summary:        Coordination library for distributed systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/tooz/
Source0:        https://files.pythonhosted.org/packages/source/t/tooz/tooz-1.64.2.tar.gz
# https://review.openstack.org/#/c/640695/
Patch1:         0001-Remove-grpcio-from-requirements.txt.patch
BuildRequires:  memcached
BuildRequires:  openstack-macros
BuildRequires:  python2-enum34 >= 1.0.4
BuildRequires:  python2-fasteners >= 0.7
BuildRequires:  python2-fixtures
BuildRequires:  python2-futures >= 3.0
BuildRequires:  python2-futurist >= 1.2.0
BuildRequires:  python2-iso8601
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.serialization >= 1.10.0
BuildRequires:  python2-oslo.utils >= 3.15.0
BuildRequires:  python2-pbr >= 1.6
BuildRequires:  python2-pifpaf
BuildRequires:  python2-pymemcache
BuildRequires:  python2-setuptools
BuildRequires:  python2-stevedore >= 1.16.0
BuildRequires:  python2-tenacity >= 3.2.1
BuildRequires:  python2-testtools
BuildRequires:  python2-voluptuous >= 0.8.9
BuildRequires:  python3-fasteners >= 0.7
BuildRequires:  python3-fixtures
BuildRequires:  python3-futurist >= 1.2.0
BuildRequires:  python3-iso8601
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.serialization >= 1.10.0
BuildRequires:  python3-oslo.utils >= 3.15.0
BuildRequires:  python3-pbr >= 1.6
BuildRequires:  python3-pifpaf
BuildRequires:  python3-pymemcache
BuildRequires:  python3-setuptools
BuildRequires:  python3-stevedore >= 1.16.0
BuildRequires:  python3-tenacity >= 3.2.1
BuildRequires:  python3-testtools
BuildRequires:  python3-voluptuous >= 0.8.9
Requires:       python-Babel
Requires:       python-fasteners >= 0.7
Requires:       python-futurist >= 1.2.0
Requires:       python-iso8601
Requires:       python-msgpack >= 0.4.0
Requires:       python-oslo.serialization >= 1.10.0
Requires:       python-oslo.utils >= 3.15.0
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.16.0
Requires:       python-tenacity >= 3.2.1
Requires:       python-voluptuous >= 0.8.9
BuildArch:      noarch
%ifpython2
Requires:       python-enum34 >= 1.0.4
Requires:       python-futures >= 3.0
%endif
%python_subpackages

%description
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

%package -n python-tooz-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description  -n python-tooz-doc
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n tooz-1.64.2
%py_req_cleanup

%build
%{python_build}

# generate html docs
PYTHONPATH=. \
    sphinx-build -b html doc/source doc/build/html
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
%{python_install}

%files %{python_files}
%license LICENSE
%{python_sitelib}/tooz
%{python_sitelib}/tooz-*.egg-info

%files -n python-tooz-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
