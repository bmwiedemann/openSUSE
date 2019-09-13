#
# spec file for package printer-driver-brlaser
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           printer-driver-brlaser
Version:        3+git20160302.03bb366
Release:        0
Summary:        Driver for (some) Brother laster printers
License:        GPL-2.0+
Group:          Hardware/Printing
Url:            https://github.com/pdewacht/brlaser
Source:         brlaser-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/pdewacht/brlaser/pull/5
Patch0:         0001-mark-DCP-7055W-as-supported.diff
# PATCH-FIX-UPSTREAM -- https://github.com/pdewacht/brlaser/pull/7
Patch1:         0002-Add-Brother-DCP1510.diff
# PATCH-FIX-UPSTREAM -- https://github.com/pdewacht/brlaser/pull/9
Patch2:         0003-Add-missing-include-string.diff
BuildRequires:  autoconf
BuildRequires:  automake
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
BuildRequires:  python-cups
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Most Brother printers support a standard printer language such as
PCL or PostScript, but not all do. If you have a monochrome Brother
laser printer (or multi-function device) and the other open source
drivers don't work, this one might help.

It is known to support these printers:

    Brother DCP-1510 series
    Brother DCP-7030
    Brother DCP-7055
    Brother DCP-7055W
    Brother DCP-7065DN

%prep
%autosetup -p1 -n brlaser-%{version}

%build
autoreconf -fi
%configure
make %{?_smp_mflags}
ppdc brlaser.drv

%install
%make_install
# installed via doc
rm %{buildroot}%{_datadir}/doc/brlaser/README.md
# we use compiled ppds instead
rm %{buildroot}%{_datadir}/cups/drv/brlaser.drv
# install compiled ppds
mkdir -p %{buildroot}%{_datadir}/cups/model
cp -a ppd %{buildroot}%{_datadir}/cups/model/brlaser

%files
%defattr(-,root,root)
%doc README.md COPYING
%dir %{_libexecdir}/cups
%dir %{_libexecdir}/cups/filter
%{_libexecdir}/cups/filter/rastertobrlaser
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%{_datadir}/cups/model/brlaser

%changelog
