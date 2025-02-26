#
# spec file for package python-thriftpy2
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-thriftpy2
Version:        0.5.2
Release:        0
Summary:        Pure python implementation of Apache Thrift
License:        MIT
URL:            https://github.com/Thriftpy/thriftpy2
Source0:        https://github.com/Thriftpy/thriftpy2/archive/v%{version}.tar.gz
Source1:        new_certs.tar.xz
# PATCH-FIX-UPSTREAM 0001-Use-SO_REUSEPORT-only-for-AF_INET-sockets.patch gh#Thriftpy/thriftpy2#303
Patch1:         0001-Use-SO_REUSEPORT-only-for-AF_INET-sockets.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tornado >= 5.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply >= 3.4
Requires:       python-six
Recommends:     python-tornado >= 5.0
Recommends:     python-toro >= 0.6
%python_subpackages

%description
ThriftPy is a pure python implementation of Apache Thrift in a
pythonic way.

%prep
%autosetup -p1 -n thriftpy2-%{version}

tar xv -C tests/ssl -f %{SOURCE1}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%{python_expand # remove devel files
find %{buildroot}%{$python_sitearch} -name '*.h' -exec rm {} \;
find %{buildroot}%{$python_sitearch} -name '*.c' -exec rm {} \;
}

%check
# the two tests fail in OBS on timeout
# test_asynchronous_exception/test_asynchronous_result - needs old tornado to work
donttest="test_able_to_communicate or test_zero_length_string or test_asynchronous_exception or test_asynchronous_result or test_api_ipv6"
# Requires python-pytest-reraise
donttest+=" or test_load_in_sub_thread or test_load_fp_in_sub_thread"

cd tests
%pytest_arch -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitearch}/thriftpy2
%{python_sitearch}/thriftpy2-%{version}.dist-info

%changelog
