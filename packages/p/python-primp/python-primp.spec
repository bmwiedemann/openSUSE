#
# spec file for package python-primp
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-primp
Version:        0.7.0
Release:        0
Summary:        HTTP client that can impersonate web browsers
License:        MIT
URL:            https://github.com/deedy5/primp
Source0:        https://files.pythonhosted.org/packages/source/p/primp/primp-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
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

%build
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
export C_INCLUDE_PATH=/usr/lib64/gcc/%_arch-suse-linux/%gcc_version/include
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=full
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# NOTE: don't run the tests as they required access to internet by trying to
# connect to "https://httpbin.org/anything".

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/primp
%{python_sitearch}/primp-%{version}*-info

%changelog
