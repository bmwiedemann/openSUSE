#
# spec file for package python-geventhttpclient
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
Name:           python-geventhttpclient
Version:        1.3.1
Release:        0
Summary:        HTTP client library for gevent
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/gwik/geventhttpclient
Source:         https://files.pythonhosted.org/packages/source/g/geventhttpclient/geventhttpclient-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/gwik/geventhttpclient/master/LICENSE-MIT
Patch0:         gevent-mark-tests.patch
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-gevent
Requires:       python-six
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
%setup -q -n geventhttpclient-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitearch}/geventhttpclient/tests/
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=$PYTHONPATH:%{buildroot}%{$python_sitearch} $python -mpytest src/geventhttpclient/tests -m 'not online'

%files %{python_files}
%license LICENSE-MIT
%{python_sitearch}/*

%changelog
