#
# spec file for package python-repoze.lru
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-repoze.lru
Version:        0.7
Release:        0
Summary:        A tiny LRU cache implementation and decorator
License:        SUSE-Repoze
Group:          Development/Languages/Python
URL:            http://www.repoze.org
Source:         https://files.pythonhosted.org/packages/source/r/repoze.lru/repoze.lru-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
repoze.lru is a LRU (least recently used) cache implementation.  Keys and
values that are not used frequently will be evicted from the cache faster
than keys and values that are used frequently.  It works under Python 2.5,
Python 2.6, Python 2.7, and Python 3.2.

%prep
%setup -q -n repoze.lru-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
