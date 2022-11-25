#
# spec file for package fwts
#
# Copyright (c) 2022 SUSE LLC
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


Name:           fwts
Version:        22.11.00
Release:        0
Summary:        Firmware Test Suite
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.ubuntu.com/Kernel/Reference/fwts
Source0:        %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fwts-no-compiletime.patch
Patch1:         fwts-no-compiletime.patch
# PATCH-FIX-OPENSUSE fwts-fix-non-acpi.patch
Patch2:         fwts-fix-non-acpi.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libfdt-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(zlib)
Requires:       bash-completion
Recommends:     acpica
Recommends:     dmidecode
Recommends:     pciutils

%description
The FirmWare Test Suite (fwts) is a tool to do automatic testing of a PC's
firmware. There can be a lot of subtle or vexing Linux Kernel/firmware issues
caused when firmware is buggy, so it's useful to have a tool that can
automatically check for common BIOS and ACPI errors. Where possible the tool
will give some form of advice on how to fix issues or workaround firmware
issues.

%prep
%autosetup -p1

%build
find . -name Makefile.am -exec sed -i "s|-Werror||g"  {} +
autoreconf -fiv
%configure \
	--disable-static
# parallel build fails on Factory
%make_build --jobs=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -D -p -m 0644 data/klog.json %{buildroot}%{_datadir}/%{name}/klog.json
install -D -p -m 0644 data/syntaxcheck.json %{buildroot}%{_datadir}/%{name}/syntaxcheck.json
# There are no headers, so drop remaining development files
rm -f "%{buildroot}/%{_libdir}/%{name}"/*.so

%files
%doc README README_ACPICA.txt README_SOURCE.txt ./data/README_JSON.txt
%doc debian/changelog
%{_bindir}/fwts
%{_bindir}/kernelscan
%{_libdir}/fwts
%{_mandir}/man1/fwts-collect.1%{?ext_man}
%{_mandir}/man1/fwts-frontend-text.1%{?ext_man}
%{_mandir}/man1/fwts.1%{?ext_man}
%{_datadir}/bash-completion/completions/fwts
%dir %{_datadir}/%{name}
%{_datadir}/fwts/clog.json
%{_datadir}/fwts/klog.json
%{_datadir}/fwts/syntaxcheck.json
%{_datadir}/fwts/olog.json

%changelog
