#
# spec file for package ethflop
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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

%define realversion 20191003
%bcond_with     dos_tsr
Name:           ethflop
Version:        0~%{realversion}
Release:        0
Summary:        A network-backed floppy emulator for DOS
License:        ISC
Group:          System/Filesystems
URL:            https://ethflop.sourceforge.net
Source:         https://ethflop.sourceforge.net/%{name}-%{realversion}.zip
Source1:        ethflopd.8
BuildRequires:  unzip
Provides:       ethflopd
%if %{with dos_tsr}
BuildRequires:  nasm
%endif

%description
ethflop is a network-backed floppy emulator for DOS, mapping a DOS
floppy drive to a remote disk image. This package contains the server
and the DOS TSR.

Features
 - emulates many types of virt. floppies (from 360K up to 31M)
 - requires only a working packet driver for connectivity
 - presents a block device to DOS, almost undistinguishable from a real FDD
 - fits in 2K of memory (and can be loaded high)

%prep
%setup -q -c %{name}
sed -i 's/\r$//' ethflop.txt

%build
%make_build CFLAGS="%{optflags} -std=gnu89" ethflopd
%if %{with dos_tsr}
%make_build tsr
%endif

%install
install -Dpm 0755 ethflopd %{buildroot}/%{_sbindir}/ethflopd
install -Dpm 0644 ethflop.com %{buildroot}/%{_datadir}/%{name}/ethflop.com
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man8/ethflopd.8

%files
%license ethflop.txt
%doc ethflop.txt
%{_sbindir}/ethflopd
%{_mandir}/man8/ethflopd.8%{?ext_man}
%{_datadir}/ethflop

%changelog
