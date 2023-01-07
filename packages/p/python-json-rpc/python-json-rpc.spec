#
# spec file for package python-json-rpc
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-json-rpc
Version:        1.14.0
Release:        0
Summary:        JSON-RPC transport implementation
License:        MIT
URL:            https://github.com/pavlov99/json-rpc
Source:         https://files.pythonhosted.org/packages/source/j/json-rpc/json-rpc-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
JSON-RPC 2.0 and JSON-RPC 1.0 transport specification implementation.

This implementation does not have any transport functionality
realization, only protocol. Any client or server implementation is
easy based on current code, but requires transport libraries, such as
requests, gevent or zmq.

%prep
%setup -q -n json-rpc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
