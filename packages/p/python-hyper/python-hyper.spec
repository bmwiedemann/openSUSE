#
# spec file for package python-hyper
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
Name:           python-hyper
Version:        0.7.0+git88.18b629b
Release:        0
Summary:        HTTP/2 Client for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Lukasa/hyper
Source0:        hyper-%{version}.tar.xz
Patch0:         fix-dependencies.patch
Patch1:         fix-test.patch
Patch2:         pr-402-h2-settings-fix.patch
Patch3:         tests-mark-rpmfail_getaddrinfo.patch
Patch4:         fix-j1-tests.patch
BuildRequires:  %{python_module brotlipy >= 0.7.0}
BuildRequires:  %{python_module h2 > 2.5.0}
BuildRequires:  %{python_module hyperframe >= 3.2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rfc3986 >= 1.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv >= 14.0.0}
BuildRequires:  fdupes
BuildRequires:  python-enum34 >= 1.0.4
BuildRequires:  python-futures
BuildRequires:  python-rpm-macros
Requires:       python-brotlipy >= 0.7.0
Requires:       python-h2 > 2.5.0
Requires:       python-hyperframe >= 3.2
Requires:       python-rfc3986 >= 1.1.0
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
hyper supports the final draft of the HTTP/2 specification: additionally,
it provides support for drafts 14, 15, and 16 of the HTTP/2 specification.
It also supports the final draft of the HPACK specification.

hyper is intended to be a drop-in replacement for http.client, with a
similar API. However, hyper intentionally does not name its classes the
same way http.client does. This is because most servers do not support
HTTP/2 at this time: I don't want you accidentally using hyper when you
wanted http.client.

%prep
%setup -q -n hyper-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_HTTPConnection_with_custom_context - TLS 1.3 does not support h2
%python_exec setup.py pytest --addopts="test/ -k 'not rpmfail_getaddrinfo and not test_HTTPConnection_with_custom_context'"

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/hyper
%{python_sitelib}/hyper*

%changelog
