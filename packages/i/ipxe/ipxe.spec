#
# spec file for package ipxe
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


%ifnarch %{ix86} x86_64
%define buildtargets dsk,usb,lkrn
%else
%define buildtargets dsk,iso,usb,lkrn
%endif

Name:           ipxe
Version:        1.21.1+git20230120.a99e435c
Release:        0
Summary:        A Network Boot Firmware
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://ipxe.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  binutils-devel
%ifnarch %{ix86} x86_64
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 159999
BuildRequires:  cross-x86_64-gcc7
%else
BuildRequires:  cross-x86_64-gcc%{gcc_version}
%endif
%endif
%ifnarch aarch64
%if 0%{?sle_version} >= 150000 && 0%{?sle_version} < 159999
BuildRequires:  cross-aarch64-gcc7
%else
BuildRequires:  cross-aarch64-gcc%{gcc_version}
%endif
%endif
BuildRequires:  perl
%ifarch %{ix86} x86_64
BuildRequires:  syslinux
BuildRequires:  xorriso
%endif
BuildRequires:  xz-devel
# Does not build on bigendian
ExcludeArch:    s390 s390x ppc ppc64
# ix86 does not have a cross-x86_64 gcc available so it can't build
# the x86_64 ipxe code. As a result of which, the support for ix86
# is more limited.

%description
iPXE is a network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

%package bootimgs
Summary:        Network boot loader images in bootable USB, CD, floppy and GRUB formats
Group:          Development/Tools/Other

%description bootimgs
iPXE is a network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE boot images in USB, CD, floppy, and PXE
UNDI formats. EFI is supported, too.

%prep
%setup -q

%build
cd src

# enable compressed images
sed -i.bak \
    -e 's,//\(#define.*IMAGE_ZLIB.*\),\1,' \
    -e 's,//\(#define.*IMAGE_GZIP.*\),\1,' \
    config/general.h

make_ipxe() {
    # https://github.com/ipxe/ipxe/issues/620
    [ `gcc -dumpversion` -ge 12 ] && TAG="NO_WERROR=1" || TAG=""
    make -O %{?_smp_mflags} V=1 \
        VERSION=%{version} $TAG "$@"
}

%ifarch %{ix86} x86_64
make_ipxe bin-i386-efi/ipxe.efi
make_ipxe bin-i386-efi/snp.efi
%else
make_ipxe CROSS="x86_64-suse-linux-" bin-i386-efi/ipxe.efi
make_ipxe CROSS="x86_64-suse-linux-" bin-i386-efi/snp.efi
%endif

%ifarch x86_64
make_ipxe bin-x86_64-efi/ipxe.efi
make_ipxe bin-x86_64-efi/snp.efi
%else
# ix86 can't cross-compile
%ifnarch %{ix86}
make_ipxe CROSS="x86_64-suse-linux-" bin-x86_64-efi/ipxe.efi
make_ipxe CROSS="x86_64-suse-linux-" bin-x86_64-efi/snp.efi
%endif
%endif # x86_64

%ifarch aarch64
make_ipxe bin-arm64-efi/snp.efi
%else
make_ipxe CROSS="aarch64-suse-linux-" bin-arm64-efi/snp.efi
%endif

make_ipxe \
%ifnarch %{ix86} x86_64
  CROSS="x86_64-suse-linux-" \
%endif
  bin/undionly.kpxe bin/ipxe.{%{buildtargets}}

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
mkdir -p %{buildroot}/%{_datadir}/%{name}.efi/

install -D -m0644 src/bin/undionly.kpxe %{buildroot}/%{_datadir}/%{name}/
install -D -m0644 src/bin/ipxe.{%{buildtargets}} %{buildroot}/%{_datadir}/%{name}/
install -D -m0644 src/bin-i386-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-i386.efi
install -D -m0644 src/bin-i386-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-i386.efi
%ifnarch %{ix86}
install -D -m0644 src/bin-x86_64-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-x86_64.efi
install -D -m0644 src/bin-x86_64-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-x86_64.efi
%endif
install -D -m0644 src/bin-arm64-efi/snp.efi %{buildroot}/%{_datadir}/%{name}/snp-arm64.efi

%files bootimgs
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ipxe.{%{buildtargets}}
%{_datadir}/%{name}/ipxe-i386.efi
%{_datadir}/%{name}/snp-i386.efi
%ifnarch %{ix86}
%{_datadir}/%{name}/ipxe-x86_64.efi
%{_datadir}/%{name}/snp-x86_64.efi
%endif
%{_datadir}/%{name}/snp-arm64.efi
%{_datadir}/%{name}/undionly.kpxe
%license COPYING COPYING.GPLv2 COPYING.UBDL

%changelog
