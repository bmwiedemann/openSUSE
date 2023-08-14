#
# spec file for package python-Logbook
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-Logbook
Version:        1.5.3
Release:        0
Summary:        A logging replacement for Python
License:        BSD-3-Clause
URL:            https://github.com/getlogbook/logbook
Source:         https://files.pythonhosted.org/packages/source/L/Logbook/Logbook-%{version}.tar.gz
# PATCH-FIX-UPSTREAM logbook-pr316-sqlalchemy-count.patch -- gh#getlogbook/logbook#316
Patch1:         https://github.com/getlogbook/logbook/pull/316.patch#/logbook-pr316-sqlalchemy-count.patch
Patch2:         deal-with-missing-socket.patch
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Cython with %python-Cython < 3}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module SQLAlchemy < 2}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module execnet >= 1.0.9}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  redis
BuildRequires:  util-linux
Recommends:     python-Jinja2
Recommends:     python-SQLAlchemy < 2
Recommends:     python-execnet >= 1.0.9
Recommends:     python-gevent
Recommends:     python-pyzmq
Recommends:     python-redis
%python_subpackages

%description
An alternative logging implementation for python.

%prep
%autosetup -p1 -n Logbook-%{version}
dos2unix LICENSE

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%{python_expand cython-%{$python_version} logbook/_speedups.pyx
%{$python_build}
rm logbook/_speedups.c
}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CFLAGS="%{optflags}"
%{_sbindir}/redis-server &
# test_asyncio_context_management seems to fail in OBS
%pytest -k 'not test_asyncio_context_management'
kill %%1

%files %{python_files}
%license LICENSE
%doc CHANGES
%{python_sitearch}/logbook
%{python_sitearch}/Logbook-%{version}-*-info

%changelog
