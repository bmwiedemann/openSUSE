#
# spec file for package efibootmgr
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           efibootmgr
Version:        14
Release:        0
Summary:        EFI Boot Manager
License:        GPL-2.0-or-later
Group:          System/Boot
Url:            https://github.com/rhinstaller/efibootmgr
Source:         https://github.com/rhinstaller/efibootmgr/releases/download/14/efibootmgr-14.tar.bz2
Patch1:         0001-Don-t-use-fshort-wchar-when-building-63.patch
Patch2:         0002-Remove-extra-const-keywords-gcc-7-gripes-about.patch
Patch3:         0003-Add-support-for-parsing-optional-data-as-ucs2.patch
Patch4:         %{name}-derhat.diff
Patch5:         MARM-sanitize-set_mirror.diff
Patch6:         %{name}-delete-multiple.diff
BuildRequires:  efivar-devel >= 31
BuildRequires:  pciutils-devel
BuildRequires:  pkg-config
BuildRequires:  popt-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The EFI Boot Manager allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables.  Additional
information about the EFI can be found at
<http://developer.intel.com/technology/efi/efi.htm>.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
LOADER="grub.efi"  # default loader
[ "$RPM_ARCH" != ia64 ] || LOADER="elilo.efi"  # except Itanium

case "%{_repository}" in
(openSUSE*)   VENDOR="openSUSE";;
(SLE_11_SP*)  VENDOR="SuSE"     LOADER="elilo.efi";;
(SUSE*|SLE*)  VENDOR="SUSE";;
(*)           VENDOR="linux";;
esac
make %{?_smp_mflags} CFLAGS="%{optflags} -flto -fPIE -pie" \
	OS_VENDOR="$VENDOR" EFI_LOADER="$LOADER"

%install
make DESTDIR=%{buildroot} sbindir=%{_sbindir} install

%files
%defattr(-, root, root)
%license COPYING
%doc README
%{_sbindir}/efiboot*
%{_mandir}/man8/*.gz

%changelog
