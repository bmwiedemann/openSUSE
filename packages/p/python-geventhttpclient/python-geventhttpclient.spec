#
# spec file for package python-geventhttpclient
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-geventhttpclient
Version:        2.3.7
Release:        0
Summary:        HTTP client library for gevent
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/gwik/geventhttpclient
Source:         https://files.pythonhosted.org/packages/source/g/geventhttpclient/geventhttpclient-%{version}.tar.gz
# Needed for tests
Source1:        https://github.com/gwik/geventhttpclient/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module dpkt}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
%if 0%{?suse_version} <= 1500
BuildRequires:  python-mock
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli
Requires:       python-certifi
Requires:       python-gevent
Requires:       python-urllib3
%python_subpackages

%description
A concurrent HTTP client library for Python using gevent.

geventhttpclient uses a HTTP parser, written in C, originating from
nginx, extracted and modified by Joyent.

geventhttpclient has been designed for high concurrency and
streaming, and supports HTTP/1.1 persistent connections. More
generally, it is designed for pulling from REST APIs and streaming
APIs like Twitter's.

%prep
%autosetup -p1 -n geventhttpclient-%{version}
tar -xvf %{SOURCE1} geventhttpclient-%{version}/tests/
%if 0%{?suse_version} >= 1600
cp geventhttpclient-%{version}/tests/{common.py,conftest.py,__init__.py,oncert.pem,server.crt,server.key} %{builddir}/geventhttpclient-%{version}/tests
rm -rf geventhttpclient-%{version}/tests/
%else
cp geventhttpclient-%{version}/tests/{common.py,conftest.py,__init__.py,oncert.pem,server.crt,server.key} /home/abuild/rpmbuild/BUILD/geventhttpclient-%{version}/tests
rm -rf geventhttpclient-%{version}/tests/
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if 0%{?suse_version} > 1600
%pytest_arch -m 'not network'
%else
%pytest_arch -m 'not network'
%endif

%files %{python_files}
%doc README.md
%license LICENSE-MIT
%{python_sitearch}/geventhttpclient
%{python_sitearch}/geventhttpclient-%{version}*-info

%changelog
