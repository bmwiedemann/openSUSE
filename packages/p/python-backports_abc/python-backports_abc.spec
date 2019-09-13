#
# spec file for package python-backports_abc
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
Name:           python-backports_abc
Version:        0.5
Release:        0
Summary:        A backport of recent additions to the 'collections.abc' module
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/cython/backports_abc
Source:         https://files.pythonhosted.org/packages/source/b/backports_abc/backports_abc-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Currently, patch() provides the following names if missing:

collections.abc.Generator
collections.abc.Awaitable
collections.abc.Coroutine
inspect.isawaitable(obj)

All of them are also available directly from the backports_abc module
namespace.

In Python 2.x and Python 3.2, it patches the collections module
instead of the collections.abc module. Any names that are already
available when importing this module will not be overwritten.

The names that were previously patched by patch() can be queried
through the mapping in backports_abc.PATCHED.

%prep
%setup -q -n backports_abc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst CHANGES.rst
%{python_sitelib}/backports_abc-%{version}-py*.egg-info
%{python_sitelib}/backports_abc.py*
%pycache_only %{python_sitelib}/__pycache__/backports_abc*

%changelog
