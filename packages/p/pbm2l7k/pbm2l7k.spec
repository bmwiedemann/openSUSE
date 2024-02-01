#
# spec file for package pbm2l7k
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


Name:           pbm2l7k
License:        GPL-2.0-or-later
Group:          Hardware/Printing
Provides:       lexmark7000linux
Version:        990321
Release:        0
Summary:        Driver for Lexmark Printers 7000, 7200, and 5700
Source:         lexmark7000linux-990321.tar.gz
Patch0:         lexmark7k.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A driver for Lexmark printers 7000, 7200, and 5700. This driver
translates PBM (Portable Bitmap) into the printer protocol for the
Lexmark printers 7000, 7200, and 5700.



Authors:
--------
    Henryk Paluch <paluch@bimbo.fjfi.cvut.cz>

%prep
%autosetup -n lexmark7k -c -T -a 0

%build
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc lexmark7000linux-990321.lsm lexmarkprotocol.txt
%doc README stairs.pbm stairsb.prn stairsc.prn
/usr/bin/pbm2l7k
/usr/share/pbm2l7k/

%changelog
