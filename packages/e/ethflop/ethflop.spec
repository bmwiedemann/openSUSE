#
# spec file for package ethflop
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define tsrversion 20240920
%define daemonversion 20240916
Name:           ethflop
Version:        0~%{tsrversion}
Release:        0
Summary:        A network-backed floppy emulator for DOS
License:        MIT
URL:            https://ethflop.sourceforge.net
Source0:        https://ethflop.sourceforge.net/ethflopd-%{daemonversion}-src.tar.gz
Source1:        https://ethflop.sourceforge.net/ethflop-%{tsrversion}.zip
Source2:        ethflopd.8
BuildRequires:  unzip
Provides:       ethflopd

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
%setup -q -c -n %{name} -T
tar xzf %{SOURCE0}
unzip -q %{SOURCE1}
sed -i 's/\r$//' ETHFLOP.TXT HISTORY.TXT ethflopd.txt

%build
%make_build -f Makefile.linux CFLAGS="%{optflags} -std=gnu89"

%install
install -Dpm 0755 ethflopd %{buildroot}/%{_sbindir}/ethflopd
install -Dpm 0644 ETHFLOP.COM %{buildroot}/%{_datadir}/%{name}/ethflop.com
install -Dpm 0644 %{SOURCE2} %{buildroot}/%{_mandir}/man8/ethflopd.8

%files
%license ETHFLOP.TXT
%doc ETHFLOP.TXT HISTORY.TXT ethflopd.txt
%{_sbindir}/ethflopd
%{_mandir}/man8/ethflopd.8%{?ext_man}
%{_datadir}/ethflop

%changelog
