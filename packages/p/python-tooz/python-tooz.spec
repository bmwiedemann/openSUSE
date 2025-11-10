#
# spec file for package python-tooz
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-tooz
Version:        7.0.0
Release:        0
Summary:        Coordination library for distributed systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/tooz/latest/
Source0:        https://files.pythonhosted.org/packages/source/t/tooz/tooz-%{version}.tar.gz
BuildRequires:  %{python_module fasteners >= 0.7}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module futurist >= 1.2.0}
BuildRequires:  %{python_module oslo.serialization >= 1.10.0}
BuildRequires:  %{python_module oslo.utils >= 4.7.0}
BuildRequires:  %{python_module pifpaf}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pymemcache}
BuildRequires:  %{python_module stevedore >= 1.16.0}
BuildRequires:  %{python_module tenacity >= 5.0.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module voluptuous >= 0.8.9}
BuildRequires:  %{python_module wheel}
BuildRequires:  memcached
BuildRequires:  openstack-macros
BuildArch:      noarch
Requires:       python-fasteners >= 0.7
Requires:       python-futurist >= 1.2.0
Requires:       python-msgpack >= 0.4.0
Requires:       python-oslo.serialization >= 1.10.0
Requires:       python-oslo.utils >= 4.7.0
Requires:       python-stevedore >= 1.16.0
Requires:       python-tenacity >= 5.0.0
Requires:       python-voluptuous >= 0.8.9
%python_subpackages

%description
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

%package -n python3-tooz-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description  -n python3-tooz-doc
The Tooz project aims at centralizing the most common distributed primitives
like group membership protocol, lock service and leader election by providing
a coordination API helping developers to build distributed applications.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n tooz-%{version}

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=. \
    sphinx-build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
export TOOZ_TEST_DRIVERS="memcached"
export PATH=%{_prefix}/sbin:$PATH
export LC_ALL=en_US.UTF-8
bash run-tests.sh

%install
%pyproject_install

%files %{python_files}
%license LICENSE
%{python_sitelib}/tooz
%{python_sitelib}/tooz-%{version}.dist-info

%files -n python3-tooz-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
