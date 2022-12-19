#
# spec file for package python-cachy
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-cachy
Version:        0.3.0
Release:        0
Summary:        A caching library for Python
License:        MIT
URL:            https://github.com/sdispater/cachy
Source:         https://files.pythonhosted.org/packages/source/c/cachy/cachy-%{version}.tar.gz
Patch0:         support-pymemcache.patch
BuildRequires:  %{python_module fakeredis >= 0.10.2}
BuildRequires:  %{python_module flexmock >= 0.10.2}
BuildRequires:  %{python_module msgpack-python >= 0.5}
BuildRequires:  %{python_module pymemcache >= 4.0}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module pytest-mock >= 1.9}
BuildRequires:  %{python_module redis >= 2.10}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-msgpack-python >= 0.5
Recommends:     python-pymemcache >= 4.0
Recommends:     python-redis >= 2.10
BuildArch:      noarch
%python_subpackages

%description
Cachy provides a caching library.

%prep
%autosetup -p1 -n cachy-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# RedisStoreTestCase requires unreleased version of fakeredis
%pytest -k 'not RedisStoreTestCase'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
