#
# spec file for package fwts
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


Name:           fwts
Version:        26.07.00
Release:        0
Summary:        Firmware Test Suite
License:        GPL-2.0-or-later
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
BuildRequires:  gcc
BuildRequires:  libfdt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(zlib)
Requires:       bash-completion
Recommends:     acpica
Recommends:     dmidecode
Recommends:     pciutils
ExclusiveArch:  %{ix86} x86_64 aarch64 riscv64

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
autoreconf -fiv
%configure \
	--disable-static \
	--disable-werror
%make_build

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
%{_bindir}/%{name}
%{_bindir}/kernelscan
%{_libdir}/%{name}
%{_mandir}/man1/fwts-collect.1%{?ext_man}
%{_mandir}/man1/fwts-frontend-text.1%{?ext_man}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/clog.json
%{_datadir}/%{name}/klog.json
%{_datadir}/%{name}/syntaxcheck.json
%{_datadir}/%{name}/olog.json

%changelog
