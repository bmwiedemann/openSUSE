#
# spec file for package python-repoze.lru
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-repoze.lru
Version:        0.7
Release:        0
Summary:        A tiny LRU cache implementation and decorator
License:        SUSE-Repoze
Group:          Development/Languages/Python
URL:            http://www.repoze.org
Source:         https://files.pythonhosted.org/packages/source/r/repoze.lru/repoze.lru-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE.txt
%dir %{python_sitelib}/repoze
%{python_sitelib}/repoze/lru
%{python_sitelib}/repoze[._]lru-%{version}*-info
%{python_sitelib}/repoze[._]lru-%{version}*nspkg.pth

%changelog
