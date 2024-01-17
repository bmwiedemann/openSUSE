#
# spec file for package printer-driver-brlaser
#
# Copyright (c) 2023 SUSE LLC
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
Version:        6+git20230220.2a49e32
Release:        0
Summary:        Driver for (some) Brother laster printers
License:        GPL-2.0-or-later
Group:          Hardware/Printing
URL:            https://github.com/pdewacht/brlaser
Source:         brlaser-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cups-rpm-helper
%if 0%{?is_opensuse} || 0%{?suse_version} != 1315
BuildRequires:  cups-ddk
BuildRequires:  cups-devel
%else
# For SLE12 by default CUPS 1.7.5 is provided and alternatively CUPS 1.5.4 is provided in the "legacy" module.
# For SLE12 build it with traditional CUPS 1.5.4 to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4.
# Only in the Printing project for SLE12 use cups154-ddk (a sub package of the cups154-SLE12 source package):
BuildRequires:  cups154-ddk
BuildRequires:  cups154-devel
%endif
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Most Brother printers support a standard printer language such as
PCL or PostScript, but not all do. If you have a monochrome Brother
laser printer (or multi-function device) and the other open source
drivers don't work, this one might help.

It is known to support these printers:

    Brother DCP-1510 series
    Brother DCP-1600 series
    Brother DCP-7030
    Brother DCP-7040 Brother DCP-7055
    Brother DCP-7055W
    Brother DCP-7060D
    Brother DCP-7065DN
    Brother DCP-7080
    Brother DCP-L2500D series
    Brother DCP-L2520D series
    Brother DCP-L2540DW series
    Brother HL-1110 series
    Brother HL-1200 series
    Brother HL-2030 series
    Brother HL-2140 series
    Brother HL-2220 series
    Brother HL-2270DW series
    Brother HL-2375DW
    Brother HL-2390DW
    Brother HL-5030 series
    Brother HL-L2300D series
    Brother HL-L2320D series
    Brother HL-L2340D series
    Brother HL-L2360D series
    Brother MFC-1910W
    Brother MFC-7240
    Brother MFC-7360N
    Brother MFC-7365DN
    Brother MFC-7420
    Brother MFC-7460DN
    Brother MFC-7840W
    Brother MFC-L2710DW series
    Lenovo M7605D

%prep
%setup -q -n brlaser-%{version}

%build
mkdir build && cd build
cmake ..
%make_build
ppdc brlaser.drv

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
