#
# spec file for package python-oslo.cache
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


Name:           python-oslo.cache
Version:        3.12.0
Release:        0
Summary:        Cache storage for Openstack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.cache
Source0:        https://files.pythonhosted.org/packages/source/o/oslo-cache/oslo_cache-%{version}.tar.gz
BuildRequires:  %{python_module dogpile.cache >= 1.3.3}
BuildRequires:  %{python_module oslo.config >= 8.1.0}
BuildRequires:  %{python_module oslo.i18n >= 5.0.0}
BuildRequires:  %{python_module oslo.log >= 4.2.1}
BuildRequires:  %{python_module oslo.utils >= 4.2.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pymemcache}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module python-binary-memcached}
BuildRequires:  %{python_module python-memcached}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-dogpile.cache >= 1.3.3
Requires:       python-oslo.config >= 8.1.0
Requires:       python-oslo.i18n >= 5.0.0
Requires:       python-oslo.log >= 4.2.1
Requires:       python-oslo.utils >= 4.2.0
Requires:       python-python-memcached
BuildArch:      noarch
%python_subpackages

%description
oslo.cache aims to provide a generic caching mechanism for OpenStack projects
by wrapping the dogpile.cache library. The dogpile.cache library provides
support memoization, key value storage and interfaces to common caching
backends such as Memcached.

%package -n python-oslo.cache-doc
Summary:        Documentation for the OpenStack Oslo Cache library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.cache-doc
Documentation for the OpenStack Oslo cache library.

%prep
%autosetup -p1 -n oslo_cache-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/oslo_cache
%{python_sitelib}/oslo_cache-%{version}.dist-info

%files -n python-oslo.cache-doc
%license LICENSE
%doc doc/build/html

%changelog
