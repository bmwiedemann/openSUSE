#
# spec file for package python-socketpool
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
%bcond_without  test
Name:           python-socketpool
Version:        0.5.3
Release:        0
Summary:        Python socket pool
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/benoitc/socketpool
Source:         https://files.pythonhosted.org/packages/source/s/socketpool/socketpool-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 37-python39.patch gh#benoitc/socketpool#37 mcepl@suse.com
# Thread.is_alive as isAlive removed in Python 3.9
Patch0:         37-python39.patch
# PATCH-FIX-UPSTREAM port_to_py3k.patch gh#benoitc/socketpool#38 mcepl@suse.com
# port tests to py3k
Patch1:         port_to_py3k.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-eventlet
Recommends:     python-gevent
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Socket pool is a socket pool that supports multiple factories and
backends. It can be used by gevent, eventlet or any other library.

%prep
%autosetup -p1 -n socketpool-%{version}

# Don't generate bytecode files for examples
rm -rf examples/__pycache__

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
# Remove wrongly installed docs
rm -r %{buildroot}%{_prefix}/socketpool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest
%endif

%files %{python_files}
%license *LICENSE
%doc README.rst
%doc examples/
%{python_sitelib}/socketpool-%{version}*-info/
%{python_sitelib}/socketpool/

%changelog
