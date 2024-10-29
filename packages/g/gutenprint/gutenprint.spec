#
# spec file for package gutenprint
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


Name:           gutenprint
URL:            http://gutenprint.sourceforge.net
Version:        5.3.4
Release:        0
%define tarball_version %{version}
%define gutenprintmajor 5.3
BuildRequires:  cups-ddk
BuildRequires:  cups-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  zlib-devel
Summary:        Printer drivers for CUPS from the Gutenprint project
License:        GPL-2.0-or-later
Group:          Hardware/Printing
# The "rastertogutenprint" filter requires CUPS and the "cups" output device in Ghostscript:
Requires:       cups
Requires:       ghostscript
# Install into this non-root directory (required when it is built as non-root user):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source0:        http://downloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM bmwiedemann https://sourceforge.net/p/gimp-print/source/merge-requests/9/
Patch0:         reproducible.patch
# How to get Source0 directly:
# wget --no-check-certificate -O gutenprint-5.3.4.tar.bz2 https://sourceforge.net/projects/gimp-print/files/gutenprint-5.3/5.3.4/gutenprint-5.3.4.tar.bz2
# Patch0...Patch9 is for patches from upstream:
# Patch10...Patch99 is for openSUSE patches which which are intended for upstream:

%description
The Gutenprint (formerly Gimp-Print) printer drivers for CUPS.
See the user's manual at /usr/share/gutenprint/doc/gutenprint-users-manual.pdf

%package devel
Summary:        Development environment for Gutenprint
Group:          Development/Libraries/C and C++
Requires:       cups
Requires:       ghostscript
Requires:       glibc-devel
Requires:       gutenprint = %{version}

%description devel
The development environment for the Gutenprint printer drivers.
See the developers guide to Gutenprint at /usr/share/gutenprint/doc/gutenprint.pdf

%prep
%autosetup -p1 -n gutenprint-%{tarball_version}

%build
#autoreconf -fvi
# No need to set our preferred architecture-specific flags for the compiler and linker
# via something like export CFLAGS="$RPM_OPT_FLAGS" and export CXXFLAGS="$RPM_OPT_FLAGS"
# because the RPM macro configure does that:
%configure \
           --disable-static \
           --disable-silent-rules \
           --enable-test \
           --enable-cups-ppds \
           --enable-simplified-cups-ppds \
           --disable-translated-cups-ppds \
           --disable-libgutenprintui2 \
           --without-gimp2
make %{?_smp_mflags}
# Do not run "make check" here because it fails.
# But "make DESTDIR=$RPM_BUILD_ROOT installcheck" works (see below).

%install
# Create required directories first:
install -d -m755 $RPM_BUILD_ROOT/bin
install -d -m755 $RPM_BUILD_ROOT/usr/share/cups/model
install -d -m755 $RPM_BUILD_ROOT/usr/lib/cups/filter
install -d -m755 $RPM_BUILD_ROOT/%{_libdir}/gutenprint/%{gutenprintmajor}
# Install Gutenprint:
make DESTDIR=$RPM_BUILD_ROOT install
# Run self-tests using the binaries in their installed location:
make DESTDIR=$RPM_BUILD_ROOT installcheck
# Remove libtool archives:
rm -rf %{buildroot}%{_libdir}/*.la
# Work with upstream compliant CUPS 1.4 on all platforms
# which means to have a fixed "/usr/lib/cups/" directory
# on all platforms (see Novell/Suse Bugzilla bnc#575544):
for D in lib32 lib64
do for F in commandtocanon commandtoepson rastertogutenprint.%{gutenprintmajor}
   do if test -e $RPM_BUILD_ROOT/usr/$D/cups/filter/$F
      then mv -f $RPM_BUILD_ROOT/usr/$D/cups/filter/$F $RPM_BUILD_ROOT/usr/lib/cups/filter/$F
      fi
   done
   F="gutenprint.%{gutenprintmajor}"
   if test -e $RPM_BUILD_ROOT/usr/$D/cups/driver/$F
   then mv -f $RPM_BUILD_ROOT/usr/$D/cups/driver/$F $RPM_BUILD_ROOT/usr/lib/cups/driver/$F
   fi
done
# Disable the run-time PPD generator /usr/lib/cups/driver/gutenprint.5.3
# so that it is not executed by the cups-driverd (e.g. in response to a "lpinfo -m" request)
# to avoid duplicated PPDs because we create the PPDs during compile-time (via --enable-cups-ppds)
# and provide ready-made PPDs in /usr/share/cups/model/gutenprint/... in the RPM package
# see "Regarding CUPS PPD files" at https://bugzilla.novell.com/show_bug.cgi?id=514994#c9
chmod a-x $RPM_BUILD_ROOT/usr/lib/cups/driver/gutenprint.%{gutenprintmajor}
# Move the special testpattern generator away from the usual bin directory:
mv $RPM_BUILD_ROOT/%{_bindir}/testpattern $RPM_BUILD_ROOT/%{_libdir}/gutenprint/%{gutenprintmajor}
# Remove dispensable .po files (only the .mo files are needed on the end-user's system):
rm $RPM_BUILD_ROOT/usr/share/locale/*/gutenprint_*.po
# Remove to make builds reproducible because hostname in here made results vary:
rm $RPM_BUILD_ROOT%_libdir/gutenprint/*/config.summary
# Mark locale-dependent files with the respective %lang tag in the file list
# see https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros
%find_lang gutenprint

%post
/sbin/ldconfig
# update quietly Gutenprint PPD files in /etc/cups/ppd/ if such PPD files exist
# using the new PPD files under /usr/share/cups/model/gutenprint/ as templates
# see https://bugzilla.novell.com/show_bug.cgi?id=637455
/usr/sbin/cups-genppdupdate -q || /bin/true
# exit successfully in any case:
exit 0

%postun
/sbin/ldconfig
# exit successfully in any case:
exit 0

%files -f gutenprint.lang
%defattr(-,root,root)
%config /etc/cups/command.types
%{_bindir}/cups-calibrate
%{_bindir}/escputil
%{_sbindir}/cups-genppd*
%dir %{_libdir}/gutenprint
%dir %{_libdir}/gutenprint/%{gutenprintmajor}
%{_libdir}/gutenprint/%{gutenprintmajor}/*
%{_libdir}/libgutenprint*.so?*
%dir /usr/share/cups
/usr/share/cups/calibrate.ppm
%dir /usr/share/cups/model
%dir /usr/share/cups/model/gutenprint
%dir /usr/share/cups/model/gutenprint/%{gutenprintmajor}
%dir /usr/share/cups/model/gutenprint/%{gutenprintmajor}/C
/usr/share/cups/model/gutenprint/%{gutenprintmajor}/C/*
%dir /usr/lib/cups/driver
/usr/lib/cups/driver/gutenprint.%{gutenprintmajor}
%dir /usr/lib/cups/filter
/usr/lib/cups/filter/commandtocanon
/usr/lib/cups/filter/commandtoepson
/usr/lib/cups/filter/rastertogutenprint.%{gutenprintmajor}
%dir /usr/lib/cups/backend
/usr/lib/cups/backend/gutenprint53+usb
%dir /usr/share/cups/usb
/usr/share/cups/usb/net.sf.gimp-print.usb-quirks
%dir /usr/share/gutenprint
%dir /usr/share/gutenprint/%{gutenprintmajor}
/usr/share/gutenprint/%{gutenprintmajor}/*
%dir /usr/share/gutenprint/samples/
/usr/share/gutenprint/samples/*
%dir /usr/share/gutenprint/doc
%doc /usr/share/gutenprint/doc/*
%doc /usr/share/man/man?/*.gz

%files devel
%defattr(-,root,root)
%dir /usr/include/gutenprint
/usr/include/gutenprint/*
%{_libdir}/pkgconfig/gutenprint*
%{_libdir}/libgutenprint*.so

%changelog
