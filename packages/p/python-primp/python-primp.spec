#
# spec file for package python-primp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?sle_version} && 0%{?sle_version} == 150600
%define force_gcc_version 13
%endif

%{?sle15_python_module_pythons}
Name:           python-primp
Version:        1.2.3
Release:        0
Summary:        HTTP client that can impersonate web browsers
License:        Apache-2.0 AND MIT
URL:            https://github.com/deedy5/primp
Source0:        https://files.pythonhosted.org/packages/source/p/primp/primp-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  libstdc++6-gcc%{?force_gcc_version}
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  git
BuildRequires:  llvm
BuildRequires:  openssl
BuildRequires:  python-rpm-macros

%python_subpackages

%description
The fastest python HTTP client that can impersonate web browsers, mimicking
their headers and 'TLS/JA3/JA4/HTTP2' fingerprints

%prep
%autosetup -p1 -n primp-%{version} -a1
# No license files at top-level
cp crates/primp-tokio-rustls/LICENSE-* .

%build
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%if 0%{?force_gcc_version}
export C_INCLUDE_PATH=/usr/lib64/gcc/%_arch-suse-linux/%{force_gcc_version}/include
export CXX=g++-%{force_gcc_version}
export CC=gcc-%{force_gcc_version}
export DCMAKE_C_COMPILER=gcc-%{force_gcc_version}
export DCMAKE_CXX_COMPILER=g++-%{force_gcc_version}
%else
export C_INCLUDE_PATH=/usr/lib64/gcc/%_arch-suse-linux/%gcc_version/include
%endif
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd crates/primp-python
# Requires network
donttest="test_client_impersonate_chrome144 or test_get_impersonate_safari18_5"
%pytest_arch --ignore tests/test_header_order.py -k "not ($donttest)"
popd

%files %{python_files}
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%{python_sitearch}/primp
%{python_sitearch}/primp-%{version}.dist-info

%changelog
