#
# spec file for package qatengine
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


Name:           qatengine
Version:        2.3.0
Release:        0
Summary:        Intel QuickAssist Technology (QAT) QATengine Library
License:        BSD-3-Clause
URL:            https://github.com/intel/QAT_Engine
Source:         https://github.com/intel/QAT_Engine/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc >= 4.8.5
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  qatlib-devel >= 21.08.0
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(zlib) >= 1.2.7
# This package can be built on all archs, but is useful only on enterprise-class intel.
ExclusiveArch:  x86_64

%description
Intel® QuickAssist Technology OpenSSL* Engine (QAT_Engine) supports
acceleration for both hardware as well as optimized software based
on vectorized instructions. This package contains an OpenSSL engine
module that utilises QAT.

%prep
%autosetup -n QAT_Engine-%{version}

%build
%{set_build_flags}
autoreconf -fiv
# Upstream builds the qatprovider by default since 2.2.0; keep the engine.
# configure.ac never runs AC_PROG_CPP, so its engine-support check executes an
# empty $CPP and always fails unless a preprocessor is passed in.
%configure CPP="gcc -E" --enable-qat_engine --enable-qat_insecure_algorithms
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# No QAT device in the build environment: only verify that the engine loads.
export OPENSSL_ENGINES=%{buildroot}$(pkg-config --variable=enginesdir libcrypto)
openssl engine -v %{name} | tee engine.out
grep -q '^(%{name})' engine.out

%files
%license LICENSE*
%{_libdir}/engines-*/%{name}.so

%changelog
