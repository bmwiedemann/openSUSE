#
# spec file for package tpm2-tss-engine
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


%define _bashcompletionsdir %{_datadir}/bash-completion/completions
# The directory where crypto engines are located is owned by the libcrypto package.
# Find out where that is.
%define _ENGINE_DIR %(pkg-config --variable=enginesdir libcrypto)
Name:           tpm2-tss-engine
Version:        1.2.0
Release:        0
Summary:        OpenSSL Engine for TPM2 devices
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software
Source0:        %{url}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  pkgconfig(libcrypto)

%description
The tpm2-tss-engine project implements a cryptographic engine for OpenSSL for
Trusted Platform Module (TPM 2.0) using the tpm2-tss software stack that follows
the Trusted Computing Groups (TCG) TPM Software Stack (TSS 2.0). It uses the
Enhanced System API (ESAPI) interface of the TSS 2.0 for downwards communication.
It supports RSA decryption and signatures as well as ECDSA signatures.

%package bash-completion
Summary:        Bash completion for tpm2-tss-engine
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(bash-completion:%{name})
BuildArch:      noarch

%description bash-completion
Optional dependency offering bash completion for the tpm2-tss-engine project.

%package devel
Summary:        Devel files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for tpm2-tss-engine, an OpenSSL engine for TPM2 devices.

The tpm2-tss-engine project implements a cryptographic engine for OpenSSL for
Trusted Platform Module (TPM 2.0) using the tpm2-tss software stack that follows
the Trusted Computing Groups (TCG) TPM Software Stack (TSS 2.0). It uses the
Enhanced System API (ESAPI) interface of the TSS 2.0 for downwards communication.
It supports RSA decryption and signatures as well as ECDSA signatures.

%prep
%setup -q

%build

autoreconf -fvi
%configure --with-enginesdir=%{_ENGINE_DIR} --disable-static --disable-defaultflags
make V=1 %{?_smp_mflags}

%install
%make_install bash_completiondir=%{_bashcompletionsdir}
rm %{buildroot}/%{_ENGINE_DIR}/libtpm2tss.la

%files
%doc CHANGELOG.md CONTRIBUTING.md INSTALL.md README.md
%license LICENSE
%{_bindir}/tpm2tss-genkey
%{_mandir}/man1/tpm2tss-genkey.1%{?ext_man}
%{_mandir}/man3/tpm2tss_ecc_genkey.3%{?ext_man}
%{_mandir}/man3/tpm2tss_ecc_getappdata.3%{?ext_man}
%{_mandir}/man3/tpm2tss_ecc_makekey.3%{?ext_man}
%{_mandir}/man3/tpm2tss_ecc_setappdata.3%{?ext_man}
%{_mandir}/man3/tpm2tss_rsa_genkey.3%{?ext_man}
%{_mandir}/man3/tpm2tss_rsa_makekey.3%{?ext_man}
%{_mandir}/man3/tpm2tss_tpm2data_read.3%{?ext_man}
%{_mandir}/man3/tpm2tss_tpm2data_write.3%{?ext_man}
%{_ENGINE_DIR}/libtpm2tss.so
%{_ENGINE_DIR}/tpm2tss.so

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_bashcompletionsdir}/tpm2tss-genkey

%files devel
%{_includedir}/tpm2-tss-engine.h

%changelog
