#
# spec file for package printer-driver-brlaser
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020 Xu Zhao (i@xuzhao.net)
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


Name:           printer-driver-brlaser
Version:        6.2.7
Release:        0
Summary:        Driver for (some) Brother laster printers
License:        GPL-2.0-or-later
Group:          Hardware/Printing
URL:            https://github.com/Owl-Maintain/brlaser
Source:         https://github.com/Owl-Maintain/brlaser/archive/refs/tags/v%{version}.tar.gz#/brlaser-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cups-ddk
BuildRequires:  cups-devel
BuildRequires:  cups-rpm-helper
BuildRequires:  gcc-c++

%description
Most Brother printers support a standard printer language such as
PCL or PostScript, but not all do. If you have a monochrome Brother
laser printer (or multi-function device) and the other open source
drivers don't work, this one might help.

The following printers have been reported to work with this driver:

    Brother DCP-1510 series
    Brother DCP-1600 series
    Brother DCP-1610W series
    Brother DCP-7010
    Brother DCP-7020
    Brother DCP-7030
    Brother DCP-7040
    Brother DCP-7055
    Brother DCP-7055W
    Brother DCP-7060D
    Brother DCP-7065DN
    Brother DCP-7070DW
    Brother DCP-7080
    Brother DCP-7080D
    Brother DCP-8065DN
    Brother DCP-B7500D series
    Brother DCP-L2500D series
    Brother DCP-L2510D series
    Brother DCP-L2520D series
    Brother DCP-L2520DW series
    Brother DCP-L2537DW
    Brother DCP-L2540DW series
    Brother DCP-L2550DW series
    Brother DCP-L2560DW series
    Brother FAX-2820
    Brother FAX-2840
    Brother HL-1110 series
    Brother HL-1200 series
    Brother HL-2030 series
    Brother HL-2130 series
    Brother HL-2140 series
    Brother HL-2150N
    Brother HL-2220 series
    Brother HL-2230 series
    Brother HL-2240 series
    Brother HL-2240D series
    Brother HL-2250DN series
    Brother HL-2260
    Brother HL-2260D
    Brother HL-2270DW series
    Brother HL-2280DW
    Brother HL-5030 series
    Brother HL-5040 series
    Brother HL-5140 series
    Brother HL-5370DW series
    Brother HL-5450DN series
    Brother HL-L2300D series
    Brother HL-L2305 series
    Brother HL-L2310D series
    Brother HL-L2320D series
    Brother HL-L2335D series
    Brother HL-L2340D series
    Brother HL-L2350DW series
    Brother HL-L2360D series
    Brother HL-L2370DN series
    Brother HL-L2375DW series
    Brother HL-L2380DW series
    Brother HL-L2390DW
    Brother HL-L2400DW
    Brother HL-L2402D
    Brother HL-L2405W
    Brother HL-L5000D series
    Brother MFC-1810 series
    Brother MFC-1910W series
    Brother MFC-7240
    Brother MFC-7320
    Brother MFC-7340
    Brother MFC-7360N
    Brother MFC-7365DN
    Brother MFC-7420
    Brother MFC-7440N
    Brother MFC-7460DN
    Brother MFC-7860DW
    Brother MFC-8440
    Brother MFC-8710DW
    Brother MFC-8860DN
    Brother MFC-9160
    Brother MFC-L2690DW
    Brother MFC-L2700DN series
    Brother MFC-L2700DW series
    Brother MFC-L2710DN series
    Brother MFC-L2710DW series
    Brother MFC-L2750DW series
    Fuji Xerox DocuPrint P265 dw
    Lenovo LJ2650DN

%prep
%setup -q -n brlaser-%{version}

%build
%cmake
%cmake_build
ppdc brlaser.drv

%check
%ctest

%install
%cmake_install
# we use compiled ppds instead
rm %{buildroot}%{_datadir}/cups/drv/brlaser.drv
# install compiled ppds
install -Dm644 build/ppd/* -t %{buildroot}%{_datadir}/cups/model/brlaser

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%dir %{_prefix}/lib/cups
%dir %{_prefix}/lib/cups/filter
%{_prefix}/lib/cups/filter/rastertobrlaser
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%{_datadir}/cups/model/brlaser

%changelog
