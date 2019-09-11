#
# spec file for package python-Logbook
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
Name:           python-Logbook
Version:        1.4.3
Release:        0
Summary:        A logging replacement for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getlogbook/logbook
Source:         https://files.pythonhosted.org/packages/source/L/Logbook/Logbook-%{version}.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module execnet >= 1.0.9}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-mock
BuildRequires:  python-rpm-macros
BuildRequires:  redis
BuildRequires:  util-linux
Recommends:     python-Jinja2
Recommends:     python-SQLAlchemy
Recommends:     python-execnet >= 1.0.9
Recommends:     python-gevent
Recommends:     python-pyzmq
Recommends:     python-redis
%python_subpackages

%description
An alternative logging implementation for python.

%prep
%setup -q -n Logbook-%{version}
sed -i 's/\r$//' LICENSE

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
cython-%{python2_version} logbook/_speedups.pyx
%python2_build
rm logbook/_speedups.c
cython-%{python3_version} logbook/_speedups.pyx
%python3_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CFLAGS="%{optflags}"
%{_sbindir}/redis-server &
%python_exec -m pytest
kill %1

%files %{python_files}
%license LICENSE
%doc CHANGES
%{python_sitearch}/*

%changelog
