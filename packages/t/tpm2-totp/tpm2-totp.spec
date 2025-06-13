#
# spec file for package tpm2-totp
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


Name:           tpm2-totp
Version:        20240326.33e1986
Release:        0
Summary:        Create TOTP tokens using a TPM2
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://tpm2-software.github.io
Source0:        tpm2-totp-%{version}.tar.gz
Patch0:         append_newline.patch
Patch1:         allow_specify_custom_secret.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  qrencode-devel
BuildRequires:  tpm2-0-tss-devel

%description
This is a reimplementation of Matthew Garrett's tpmtotp software for TPM 2.0 using the tpm2-tss software stack.
Its purpose is to attest the trustworthiness of a device against a human using time-based one-time passwords (TOTP),
facilitating the Trusted Platform Module (TPM) to bind the TOTP secret to the known trustworthy system state.
In addition to the original tpmtotp, given the new capabilities of in-TPM HMAC calculation,
the tpm2-totp's secret HMAC keys do not have to be exported from the TPM to the CPU's RAM on boot anymore.
Another addition is the ability to rebind an old secret to the current PCRs in case a software component was changed on purpose,
using a user-defined password.

%package -n libtpm2-totp0
Summary:        TOTP library for TPM 2.0 chips
Group:          System/Libraries

%description -n libtpm2-totp0
This package provides the tpm2-totp library.

%package -n libtpm2-totp0-devel
Summary:        Development headers for the TOTP library for TPM 2.0 chips
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description -n libtpm2-totp0-devel
This package provides the development files for the tpm2-totp lib.

%prep
%autosetup -p1

%build
echo %{version} > VERSION
autoreconf --install --sym
%configure
%make_build

%install
%make_install
rm %{buildroot}/%{_libdir}/libtpm2-*.*a

%ldconfig_scriptlets -n libtpm2-totp0

%check
make check

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%license LICENSE
%doc README.md CHANGELOG.md

%files -n libtpm2-totp0
%{_libdir}/libtpm2-*.so.*

%files -n libtpm2-totp0-devel
%{_libdir}/libtpm2-*.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3%{?ext_man}

%changelog
