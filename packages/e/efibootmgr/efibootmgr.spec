#
# spec file for package efibootmgr
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


Name:           efibootmgr
Version:        18
Release:        0
Summary:        EFI Boot Manager
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            https://github.com/rhinstaller/efibootmgr
Source:         https://github.com/rhboot/efibootmgr/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.bz2
Patch0:         %{name}-delete-multiple.diff
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(efiboot) >= 31
BuildRequires:  pkgconfig(efivar) >= 31
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(zlib)

%description
The EFI Boot Manager allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about the EFI can be found at
<http://developer.intel.com/technology/efi/efi.htm>.

%prep
%autosetup -p1

%build
# removing hotfix function declaration:
# https://github.com/rhboot/efibootmgr/issues/128
sed -e '/extern int efi_set_verbose/d' -i "src/efibootmgr.c"

LOADER="grub.efi"  # default loader
[ "$RPM_ARCH" != ia64 ] || LOADER="elilo.efi"  # except Itanium

case "%{_repository}" in
(openSUSE*)   VENDOR="openSUSE";;
(SLE_11_SP*)  VENDOR="SuSE"     LOADER="elilo.efi";;
(SUSE*|SLE*)  VENDOR="SUSE";;
(*)           VENDOR="linux";;
esac
%make_build CFLAGS="%{optflags} -flto -fPIE -pie" \
	OS_VENDOR="$VENDOR" EFI_LOADER="$LOADER" EFIDIR="$VENDOR"

%install
case "%{_repository}" in
(openSUSE*)   VENDOR="openSUSE";;
(SLE_11_SP*)  VENDOR="SuSE"     LOADER="elilo.efi";;
(SUSE*|SLE*)  VENDOR="SUSE";;
(*)           VENDOR="linux";;
esac
make DESTDIR=%{buildroot} sbindir=%{_sbindir} EFIDIR="$VENDOR" install

%files
%license COPYING
%doc README
%{_sbindir}/efiboot*
%{_mandir}/man8/*.gz

%changelog
