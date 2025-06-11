#
# spec file for package python-pylru
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


Name:           python-pylru
Version:        1.2.1
Release:        0
Summary:        A least recently used (LRU) cache implementation
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jlhutch/pylru
Source:         https://files.pythonhosted.org/packages/source/p/pylru/pylru-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pylru implements a true LRU cache along with several support classes. The cache is efficient and written in pure Python. It works with Python 2.6+ including the 3.x series. Basic operations (lookup, insert, delete) all run in a constant amount of time. Pylru provides a cache class with a simple dict interface. It also provides classes to wrap any object that has a dict interface with a cache. Both write-through and write-back semantics are supported. Pylru also provides classes to wrap functions in a similar way, including a function decorator.

%prep
%setup -q -n pylru-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/pylru.py
%pycache_only %{python_sitelib}/__pycache__/pylru*
%{python_sitelib}/pylru-%{version}*-info

%changelog
