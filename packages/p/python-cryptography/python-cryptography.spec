#
# spec file for package python-cryptography
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-cryptography%{psuffix}
# ALWAYS KEEP IN SYNC WITH python-cryptography-vectors!
Version:        44.0.0
Release:        0
Summary:        Python library which exposes cryptographic recipes and primitives
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://cryptography.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz
# use `osc service manualrun` to regenerate
Source2:        vendor.tar.zst
Source4:        python-cryptography.keyring
# PATCH-FEATURE-OPENSUSE no-pytest_benchmark.patch mcepl@suse.com
# We don't need no benchmarking and coverage measurement
Patch4:         no-pytest_benchmark.patch
BuildRequires:  %{python_module cffi >= 1.12}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-rust >= 1.7.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo >= 1.56.0
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.56.0
BuildRequires:  zstd
BuildRequires:  pkgconfig(libffi)
# python-base is not enough, we need the _ssl module
Requires:       python
Requires:       python-bcrypt
Requires:       python-cffi = %(rpm -q --whatprovides python-cffi --qf "%%{version}")
%if %{with test}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= %{version}}
BuildRequires:  %{python_module cryptography-vectors = %{version}}
BuildRequires:  %{python_module hypothesis >= 1.11.4}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest > 6.0}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytz}
%endif
%python_subpackages

%description
cryptography includes both high level recipes, and low
level interfaces to common cryptographic algorithms such as
symmetric ciphers, message digests and key derivation
functions.

%prep
%autosetup -a2 -p1 -n cryptography-%{version}

%build
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=true
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
# https://pyo3.rs/main/building-and-distribution#configuring-the-python-version
%python_expand export PYO3_PYTHON="%{_bindir}/$python"
%global _lto_cflags %{nil}
export RUSTFLAGS=%{rustflags}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%if !%{with test}
export RUSTFLAGS=%{rustflags}
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete

%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# won't work for cryptography
# fails with OverflowError on 32bit platform
%ifarch %ix86 %arm ppc
rm -v tests/hazmat/primitives/test_aead.py
rm -v tests/hazmat/primitives/test_ciphers.py
# imports test_aead so we need to remove also these
rm -v tests/wycheproof/test_aes.py
rm -v tests/wycheproof/test_chacha20poly1305.py
%endif
%pytest_arch -n auto --ignore-glob=vendor/*
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc CONTRIBUTING.rst CHANGELOG.rst README.rst
%{python_sitearch}/cryptography
%{python_sitearch}/rust
%{python_sitearch}/cryptography-%{version}.dist-info
%endif

%changelog
