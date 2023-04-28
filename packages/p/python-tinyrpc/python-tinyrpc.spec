#
# spec file for package python-tinyrpc
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


%define skip_python2 1
Name:           python-tinyrpc
Version:        1.1.6
Release:        0
Summary:        A modular transport and protocol neutral RPC library
License:        MIT
URL:            https://github.com/mbr/tinyrpc
Source:         https://github.com/mbr/tinyrpc/archive/%{version}.tar.gz
# https://github.com/mbr/tinyrpc/issues/103
Patch0:         python-tinyrpc-no-six.patch
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pika >= 1.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
There are a number of jsonrpc libraries already out there on PyPI,
most of them handling one specific use case (e.g. JSON via WSGI,
using Twisted, or TCP sockets).

None of the libraries, however, made it easy for the author of
TinyRPC to reuse the jsonrpc-parsing bits and substitute a different
transport (i.e. going from json via TCP to an implementation using
WebSockets or ZeroMQ).

%prep
%autosetup -p1 -n tinyrpc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand find %{buildroot}%{$python_sitelib}/tinyrpc -name "*.py" | xargs sed -i '1 {/^#!/ d}'

%check
# test_batch_dispatch - needs old pytest syntax, skip
%pytest -k 'not test_batch_dispatch'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tinyrpc*

%changelog
