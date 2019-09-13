#
# spec file for package python-socketpool
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_with     test
Name:           python-socketpool
Version:        0.5.3
Release:        0
Summary:        Python socket pool
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/benoitc/socketpool
Source:         https://files.pythonhosted.org/packages/source/s/socketpool/socketpool-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
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
%setup -q -n socketpool-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
rm -r %{buildroot}%{_prefix}/socketpool # Remove wrongly installed docs

%if %{with test}
%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix}
%endif

%files %{python_files}
%license *LICENSE
%doc README.rst
%doc examples/
%{python_sitelib}/*

%changelog
