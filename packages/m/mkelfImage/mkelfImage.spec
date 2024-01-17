#
# spec file for package mkelfImage
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mkelfImage
Version:        2.5
Release:        0
Summary:        Utility to Create ELF Boot Images from Linux Kernel Images
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://www.coreboot.org/Mkelfimage
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.dif
Patch1:         %{name}-optflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  zlib-devel

%description
mkelfImage is a program that makes an ELF boot image for Linux kernel
images. The image should work with any i386 multiboot compliant boot loader
as well as with an ELF boot loader that passes no options. It is compliant
with the LinuxBIOS ELF booting specification or with the Linux kexec kernel
patch.Its key feature is, that nothing relies on BIOS calls, but they are
made when necessary. This is useful for systems running LinuxBIOS.

%prep
%setup -q
%patch0
%patch1 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc News COPYING AUTHORS
%{_sbindir}/mkelfImage
%{_mandir}/man8/mkelfImage.8%{ext_man}
%{_datadir}/mkelfImage/

%changelog
