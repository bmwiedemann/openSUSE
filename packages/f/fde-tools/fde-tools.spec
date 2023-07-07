#
# spec file for package fde-tools
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


Name:           fde-tools
Version:        0.6.5
Release:        0
Summary:        Tools required for Full Disk Encryption
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://github.com/openSUSE/fde-tools
Source:         https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        fde-tools.service
Patch:          fde-tools-firstboot-alp-snapshot.patch
Patch1:         fde-tools-avoid-cleaning-temp-dir.patch
Patch2:         fde-tools-fix-bootloader-func.patch
Patch3:         fde-tools-force-dracut.patch
BuildRequires:  help2man
BuildRequires:  openssl >= 0.9.8
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(libfido2)
Requires:       cryptsetup
Requires:       pcr-oracle >= 0.4.5
# Requires:	tpm2.0-tools
Requires:       mokutil
ExclusiveArch:  aarch64 s390x ppc64le x86_64 riscv64

%package -n fde-firstboot
Summary:        Full Disk Encryption for images
Group:          System/Boot
Requires:       fde-tools
Requires:       jeos-firstboot

%description
This package provides several components required to support Full Disk
Encryption.

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

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

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
%dir /etc/fde
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

%changelog
