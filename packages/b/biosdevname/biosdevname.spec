#
# spec file for package biosdevname
#
# Copyright (c) 2020 SUSE LLC
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


%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
Name:           biosdevname
Version:        0.7.3
Release:        0
Summary:        Udev helper for naming devices per BIOS names
License:        GPL-2.0-only
Group:          System/Base
URL:            https://github.com/dell/biosdevname
Source0:        %{name}-%{version}.tar.xz
Patch1:         ignore-broken-BIOSes
Patch2:         whitelist-dell
Patch3:         udev-rule-path.patch
Patch4:         biosdevname-pic.patch
Patch5:         biosdevname-dom0.patch
Patch6:         dmidecode-prevent-infinite-recursion.patch
Patch7:         biosdevname-Add-buffer-read-helper-using-read-explicitly.patch
Patch8:         biosdevname-Read-DMI-entries-from-sys-firmware-dmi-tables-DMI.patch
Patch9:         biosdevname-Add-SMBIOS-3.x-support.patch
BuildRequires:  automake
BuildRequires:  pciutils-devel
BuildRequires:  pkg-config
BuildRequires:  sed
BuildRequires:  suse-module-tools
BuildRequires:  zlib-devel
# to figure out how to name/location of the rules file
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
Requires(post): coreutils
Requires(postun): coreutils
# for ownership of /usr/lib/udev/rules.d
Requires:       udev
BuildRequires:  pkgconfig(udev)
Supplements:    modalias(dmi:*svnDell*)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# SMBIOS and PCI IRQ Routing Tables only exist on these arches.  It's
# also likely that other arches don't expect the PCI bus to be sorted
# breadth-first, or of so, there haven't been any comments about that
# on LKML.
ExclusiveArch:  %ix86 x86_64

%description
biosdevname in its simplest form takes a kernel name as an
argument, and returns the BIOS-given name it "should" be.  This is
necessary on systems where the BIOS name for a given device (e.g. the
label on the chassis is "Gb1") doesn't map directly and obviously to
the kernel name (e.g. eth0).

You can enable/disable usage of biosdevname with boot option
"biosdevname=[0|1]"

%prep
%setup -q
%autopatch -p1

%build
sed -i -e 's#@@BIOSDEVNAME_RULEDEST@@#'%{_udevrulesdir}'/71-biosdevname.rules#' configure.ac
autoreconf -fi
%configure \
	--disable-rpath \
	--prefix=/ \
	--bindir=/bin \
	--sbindir=/sbin
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}/sbin/%{name}S || :

%files
%defattr(-,root,root,-)
%license COPYING
%doc README
/sbin/%{name}
%{_udevrulesdir}/71-biosdevname.rules

%{_mandir}/man1/*

%post
/sbin/ldconfig
%{?regenerate_initrd_post}

%postun
/sbin/ldconfig
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%changelog
