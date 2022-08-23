#
# spec file for package python-cachelib
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cachelib
Version:        0.9.0
Release:        0
Summary:        A collection of cache libraries in the same API interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pallets-eco/cachelib
Source:         https://files.pythonhosted.org/packages/source/c/cachelib/cachelib-%{version}.tar.gz
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pytest-xprocess}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  memcached
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Recommends:     python-pylibmc
Recommends:     python-redis
BuildArch:      noarch
%python_subpackages

%description
A collection of cache libraries in the same API interface.

%prep
%setup -q -n cachelib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Allow finding memcached
export PATH="%{_sbindir}/:$PATH"
%{_sbindir}/redis-server &
%pytest -rs

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/*cachelib*/

%changelog
