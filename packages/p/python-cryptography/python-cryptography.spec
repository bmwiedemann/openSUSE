#
# spec file
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-cryptography%{psuffix}
Version:        39.0.0
Release:        0
Summary:        Python library which exposes cryptographic recipes and primitives
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://cryptography.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz
# use `osc service disabledrun` to regenerate
Source2:        vendor.tar.zst
# use `osc service disabledrun` to regenerate
Source3:        cargo_config
Source4:        python-cryptography.keyring
Patch2:         skip_openssl_memleak_test.patch
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
Patch3:         remove_python_3_6_deprecation_warning.patch
%endif
BuildRequires:  %{python_module cffi >= 1.12}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cargo >= 1.41.0
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.41.0
BuildRequires:  zstd
BuildRequires:  pkgconfig(libffi)
# python-base is not enough, we need the _ssl module
Requires:       python
%requires_eq    python-cffi
%if %{with test}
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
cryptography is a package designed to expose cryptographic
recipes and primitives to Python developers.  Our goal is
for it to be your "cryptographic standard library". It
supports Python 2.7, Python 3.4+, and PyPy-5.3+.

cryptography includes both high level recipes, and low
level interfaces to common cryptographic algorithms such as
symmetric ciphers, message digests and key derivation
functions.

%prep
%autosetup -a2 -p1 -n cryptography-%{version}
mkdir .cargo
cp %{SOURCE3} .cargo/config
rm -v src/rust/Cargo.lock

%build
export RUSTFLAGS=%{rustflags}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%if !%{with test}
export RUSTFLAGS=%{rustflags}
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete

%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# won't work for cryptography
%pytest_arch -n auto --ignore-glob=vendor/*
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc CONTRIBUTING.rst CHANGELOG.rst README.rst
%{python_sitearch}/cryptography
%{python_sitearch}/cryptography-%{version}*-info
%endif

%changelog
