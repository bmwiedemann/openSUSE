#
# spec file for package python-locket
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
Name:           python-locket
Version:        0.2.0
Release:        0
Summary:        File-based locks for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://github.com/mwilliamson/locket.py
Source:         https://files.pythonhosted.org/packages/source/l/locket/locket-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Locket implements a lock that can be used by multiple processes provided
they use the same path.

Locks largely behave as (non-reentrant) `Lock` instances from the `threading`
module in the standard library. Specifically, their behaviour is:

* Locks are uniquely identified by the file being locked,
  both in the same process and across different processes.
* Locks are either in a locked or unlocked state.
* When the lock is unlocked, calling `acquire()` returns immediately and changes
  the lock state to locked.
* When the lock is locked, calling `acquire()` will block until the lock state
  changes to unlocked, or until the timeout expires.
* If a process holds a lock, any thread in that process can call `release()` to
  change the state to unlocked.
* Behaviour of locks after `fork` is undefined.

%prep
%setup -q -n locket-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
