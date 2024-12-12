#
# spec file for package fde-tools
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


%if %{undefined _rpmmacrodir}
  %define _rpmmacrodir %{_sysconfdir}/rpm
%endif

Name:           fde-tools
Version:        0.7.2
Release:        0
Summary:        Tools required for Full Disk Encryption
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://github.com/openSUSE/fde-tools
Source:         https://github.com/openSUSE/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source1:        fde-tools.service
Patch0:         fde-tools-firstboot-alp-snapshot.patch
Patch1:         fde-tools-bsc1213945-set-rsa-key-size.patch
Patch2:         fde-tools-change-rpm-macro-dir.patch
Patch3:         fde-tools-bsc1220160-conditional-requires.patch
Patch4:         fde-tools-bsc1222970-firstboot-replace-ALP.patch
Patch5:         fde-tools-bsc1223002-firstboot-disable-ccid.patch
Patch6:         fde-tools-bsc1218390-Switch-to-target-platform-when-available.patch
Patch7:         fde-tools-bsc1218390-fix-tpm-present-with-the-newer-pcr-oracle.patch
Patch8:         fde-tools-bsc1223771-firstboot-make-Pass-phrase-mandatory.patch
Patch9:         fde-tools-bsc1218181-replace-crypttab-key-path.patch
BuildRequires:  help2man
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(libfido2)
Requires:       cryptsetup
Requires:       mokutil
Requires:       pcr-oracle >= 0.4.5
Requires:       util-linux-systemd
ExclusiveArch:  aarch64 x86_64 riscv64 loongarch64

%description
This package provides several components required to support Full Disk
Encryption.

%package -n fde-firstboot
Summary:        Full Disk Encryption for images
Group:          System/Boot
Requires:       fde-tools
Requires:       jeos-firstboot
BuildArch:      noarch

%description -n fde-firstboot
This package contains the scripts necessary to plug Full Disk Encryption
into the JeOS Firstboot framework used for image based delivery of ALP.

%package bash-completion
Summary:        Bash completion for fde-tools
Group:          Productivity/File utilities
Requires:       bash-completion
Requires:       fde-tools
Supplements:    (fde-tools and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash shell completions for fde-tools

%package -n fde-tpm-helper
Summary:        TPM helper for fde-tools
Group:          System/Boot
BuildArch:      noarch

%description -n fde-tpm-helper
This package contains the TPM helper script for the bootloader packages
to update the signature in the sealed key.

%package -n fde-tpm-helper-rpm-macros
Summary:        RPM macros for fde-tools
Group:          Development/Tools/Building
BuildArch:      noarch

%description -n fde-tpm-helper-rpm-macros
This package contains the RPM macros for the bootloader packages to
update the signature in the sealed key.

%prep
%autosetup -p1

%build
%make_build \
	CCFLAGS="%optflags" \
	LIBDIR="%{_libdir}" \
	LIBEXECDIR="%{_libexecdir}" \
	SBINDIR="%{_sbindir}" \
	DATADIR="%{_datadir}" \
	SYSCONFDIR="%{_sysconfdir}" \
	RPM_MACRO_DIR="%{_rpmmacrodir}"

%install
%make_install \
	LIBDIR="%{_libdir}" \
	LIBEXECDIR="%{_libexecdir}" \
	SBINDIR="%{_sbindir}" \
	DATADIR="%{_datadir}" \
	SYSCONFDIR="%{_sysconfdir}" \
	RPM_MACRO_DIR="%{_rpmmacrodir}"

mkdir -p %{buildroot}%{_fillupdir}
mv %{buildroot}/etc/sysconfig/fde-tools %{buildroot}%{_fillupdir}/sysconfig.fde-tools

mkdir -p %{buildroot}%{_unitdir}
cp %{S:1} %{buildroot}%{_unitdir}/fde-tpm-enroll.service

%pre
%service_add_pre fde-tpm-enroll.service

%post
%service_add_post fde-tpm-enroll.service
%fillup_and_insserv

%preun
%service_del_preun fde-tpm-enroll.service

%postun
%service_del_postun fde-tpm-enroll.service

%files
%{_sbindir}/fdectl
%{_sbindir}/fde-token
%{_sbindir}/fdectl-grub-tpm2
%dir %{_sysconfdir}/fde
%{_fillupdir}/sysconfig.*
%{_datadir}/fde
%{_unitdir}/fde-tpm-enroll.service
%{_mandir}/man8/fdectl.8.gz
%dir %{_libdir}/cryptsetup/
%{_libdir}/cryptsetup/libcryptsetup-token-*.so

%files bash-completion
%{_datadir}/bash-completion/completions/fdectl

%files -n fde-firstboot
%dir %{_datadir}/jeos-firstboot
%dir %{_datadir}/jeos-firstboot/modules
%{_datadir}/jeos-firstboot/modules/fde

%files -n fde-tpm-helper
%dir %{_libexecdir}/fde
%{_libexecdir}/fde/fde-tpm-helper

%files -n fde-tpm-helper-rpm-macros
%{_rpmmacrodir}/macros.fde-tpm-helper

%changelog
