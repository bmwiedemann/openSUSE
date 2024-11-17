#
# spec file for package pappl
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


Name:           pappl
%define lname   libpappl1
Version:        1.4.8
Release:        0
Summary:        A printer application framework
License:        Apache-2.0
Group:          Hardware/Printing
URL:            https://www.msweet.org/pappl/
Source:         https://github.com/michaelrsweet/pappl/releases/download/v%version/pappl-%version.tar.gz
Source2:        https://github.com/michaelrsweet/pappl/releases/download/v%version/pappl-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  cups-devel > 2.2.6
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)

%description
PAPPL is a C-based framework/library for developing CUPS Printer
Applications, which are the recommended replacement for printer
drivers. PAPPL supports LPrint and a Gutenprint Printer Application,
but it is sufficiently general purpose to support any kind of printer
or driver that can be used on desktops, servers and in embedded
environments.

PAPPL supports JPEG, PNG, PWG Raster, Apple Raster, and "raw"
printing to printers connected via USB and network
(AppSocket/JetDirect) connections. PAPPL provides access to the
printer via its embedded IPP Everywhere service, either local to the
computer or on your whole network, which can then be discovered and
used by any application.

%package -n %lname
Summary:        A printer application framework
Group:          System/Libraries

%description -n %lname
PAPPL is a framework/library for developing CUPS Printer
Applications, which are the recommended replacement for printer
drivers.

PAPPL supports JPEG, PNG, PWG Raster, Apple Raster, and "raw"
printing to printers connected via USB and network
(AppSocket/JetDirect) connections.

%package devel
Summary:        Development files for PAPPL
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
PAPPL is a C-based framework/library for developing CUPS Printer
Applications, which are the recommended replacement for printer
drivers.

This subpackage contains the headers for the library.

%prep
%autosetup -p1

%build
perl -i -lpe 's{^\.SILENT:.*}{}g' Makedefs.in
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --disable-static --includedir="%_includedir/%name"
%make_build

%install
# quite dumb to concatenate RPM_BUILD_ROOT and DESTDIR
%make_install RPM_BUILD_ROOT=""
rm -f "%buildroot/%_libdir"/*.a

%ldconfig_scriptlets -n %lname

%files
%_bindir/pappl-*
%_mandir/man1/*.1*
%_datadir/%name/
%license LICENSE

%files -n %lname
%_libdir/libpappl.so.1*

%files devel
%_includedir/%name/
%_libdir/libpappl.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/pappl-*
%_datadir/doc/%name/

%changelog
