#
# spec file for package python-oslo.cache
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


Name:           python-oslo.cache
Version:        2.6.1
Release:        0
Summary:        Cache storage for Openstack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.cache/oslo.cache-2.6.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-dogpile.cache >= 1.0.2
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 8.1.0
BuildRequires:  python3-oslo.i18n >= 5.0.0
BuildRequires:  python3-oslo.log >= 4.2.1
BuildRequires:  python3-oslo.utils >= 4.2.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-pymongo
BuildRequires:  python3-python-memcached
BuildRequires:  python3-six
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
oslo.cache aims to provide a generic caching mechanism for OpenStack projects
by wrapping the dogpile.cache library. The dogpile.cache library provides
support memoization, key value storage and interfaces to common caching
backends such as Memcached.

%package -n python3-oslo.cache
Summary:        Cache storage for Openstack projects
Group:          Development/Languages/Python
Requires:       python3-dogpile.cache >= 1.0.2
Requires:       python3-oslo.config >= 8.1.0
Requires:       python3-oslo.i18n >= 5.0.0
Requires:       python3-oslo.log >= 4.2.1
Requires:       python3-oslo.utils >= 4.2.0
Requires:       python3-python-memcached
Requires:       python3-six

%description -n python3-oslo.cache
oslo.cache aims to provide a generic caching mechanism for OpenStack projects
by wrapping the dogpile.cache library. The dogpile.cache library provides
support memoization, key value storage and interfaces to common caching
backends such as Memcached.

%package -n python-oslo.cache-doc
Summary:        Documentation for the OpenStack Oslo Cache library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.cache-doc
Documentation for the OpenStack Oslo cache library.

%prep
%autosetup -p1 -n oslo.cache-2.6.1
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# generate html docs
PBR_VERSION=2.6.1 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
python3 -m stestr.cli run

%files -n python3-oslo.cache
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/oslo_cache
%{python3_sitelib}/*.egg-info

%files -n python-oslo.cache-doc
%license LICENSE
%doc doc/build/html

%changelog
