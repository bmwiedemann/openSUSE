#
# spec file for package gutenprint
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gutenprint
Url:            http://gutenprint.sourceforge.net
#Version:        5.2.14
Version:        5.2.14pre15.1
Release:        0
#define tarball_version %{version}
%define tarball_version 5.2.15-pre1
%define gutenprintmajor 5.2
BuildRequires:  cairo-devel
# SLE10 and SLE11 and SLE12 need special BuildRequires.
# For suse_version values see https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} != 1010 && 0%{?suse_version} != 1110 && 0%{?suse_version} != 1315
# Anything what is not SLE10 or SLE11 or SLE12 (i.e. all openSUSE versions) have "normal" BuildRequires.
BuildRequires:  cups-ddk
BuildRequires:  cups-devel
%endif
%if 0%{?suse_version} == 1110 || 0%{?suse_version} == 1010
# On SLE11 and SLE10 there is the separated package cupsddk.
BuildRequires:  cups-devel
BuildRequires:  cupsddk
%endif
%if 0%{?suse_version} == 1315
# For SLE12 by default CUPS 1.7.5 is provided and alternatively CUPS 1.5.4 is provided in the "legacy" module.
# For SLE12 build it with traditional CUPS 1.5.4 to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4.
# Only in the Printing project for SLE12 use cups154-ddk (a sub package of the cups154-SLE12 source package):
BuildRequires:  cups154-ddk
BuildRequires:  cups154-devel
%endif
BuildRequires:  gimp-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
%if 0%{?suse_version} >= 1140
# The CUPS dyesub USB backend requires libusb-1.0 which is available since openSUSE 11.4.
# When libusb-1.0 is not available, the configure magic does not build the CUPS dyesub USB backend.
BuildRequires:  libusb-1_0-devel
%endif
BuildRequires:  pango-devel
%if 0%{?suse_version} != 1010
# On SLE10 there is no python-cups. Simply omit it because that BuildRequires is only there to
# add python-cups BuildRequires to have postscriptdriver() Provides for the drivers in gutenprint.
BuildRequires:  python-cups
%endif
Summary:        Printer drivers for CUPS from the Gutenprint project
License:        GPL-2.0+
Group:          Hardware/Printing
# The "rastertogutenprint" filter requires CUPS and the "cups" output device in Ghostscript:
%if 0%{?suse_version} == 1010
# For SLE10 it must be built with --disable-escputil because in SLE10 escputil is provided by ghostscript-library
%define enable_or_disable_escputil disable-escputil
# For SLE10 it must be built with --disable-cups-1_2-enhancements because SLE10 has CUPS 1.1
%define enable_or_disable_cups_1_2_enhancements disable-cups-1_2-enhancements
Requires:       cups
%else
%define enable_or_disable_escputil enable-escputil
%define enable_or_disable_cups_1_2_enhancements enable-cups-1_2-enhancements
Requires:       cups >= 1.2.2
%endif
%if 0%{?suse_version} == 1110 || 0%{?suse_version} == 1010
# For SLE11 and SLE10 it must be built --without-gimp2 because since Gutenprint 5.2.13
# the gimp_pixels_to_units function is called in in src/gimp2/print.c and according to
# https://developer.gimp.org/api/2.0/libgimpbase/libgimpbase-gimpunit.html
# the gimp_pixels_to_units function is available since GIMP 2.8
# but SLE11 provides GIMP 2.6.2 and SLE10 provides GIMP 2.2.10:
%define with_or_without_gimp2 without-gimp2
# Let the main package confict with an installed gutenprint-gimpplugin <= 5.2.12
# which intentionally should break an automated RPM package version upgrade
# to make the user aware that by installing Gutenprint 5.2.13
# there will be no longer a gutenprint-gimpplugin:
Conflicts:      gutenprint-gimpplugin < 5.2.13
%else
%define with_or_without_gimp2 with-gimp2
%endif
# Up to openSUSE 12.1 the package cups has "Requires: ghostscript_any" so that the above
# "Requires: cups" is sufficient to also get the "cups" output device in Ghostscript.
# Since openSUSE 12.2 the package cups has only "Recommends: ghostscript" to avoid
# an implicit build dependency cycle between the main-packages cups and ghostscript.
# Therefore after openSUSE 12.1 gutenprint needs an explicit "Requires: ghostscript"
# to ensure that the "cups" output device in Ghostscript is available:
%if 0%{?suse_version} > 1210
Requires:       ghostscript
%endif
# Install into this non-root directory (required when it is built as non-root user):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# URL for Source0 automated download:
# https://sourceforge.net/projects/gimp-print/files/gutenprint-5.2/5.2.14/gutenprint-5.2.14.tar.bz2/download
# How to get Source0 directly:
# wget --no-check-certificate -O gutenprint-5.2.14.tar.bz2 https://sourceforge.net/projects/gimp-print/files/gutenprint-5.2/5.2.14/gutenprint-5.2.14.tar.bz2
#Source0:        http://downloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.bz2
# How to get Source0 directly:
# wget --no-check-certificate -O gutenprint-5.2.15-pre1.tar.bz2 https://sourceforge.net/projects/gimp-print/files/gutenprint-5.2/5.2.15-pre1/gutenprint-5.2.15-pre1.tar.bz2/download
Source0:        gutenprint-5.2.15-pre1.tar.bz2
# Patch0...Patch9 is for patches from upstream:
# Patch10...Patch99 is for openSUSE patches which which are intended for upstream:

%description
The Gutenprint (formerly Gimp-Print) printer drivers for CUPS.
See the user's manual at /usr/share/gutenprint/doc/gutenprint-users-manual.pdf

%package devel
Summary:        Development environment for Gutenprint
Group:          Development/Libraries/C and C++
Requires:       cups >= 1.2.2
Requires:       ghostscript-library >= 7.05
Requires:       glibc-devel
Requires:       gtk2-devel
Requires:       gutenprint = %{version}

%description devel
The development environment for the Gutenprint printer drivers.
See the developers guide to Gutenprint at /usr/share/gutenprint/doc/gutenprint.pdf

%if 0%{?suse_version} > 1110
# For SLE11 and SLE10 it is built --without-gimp2 (see above):
%package gimpplugin
Summary:        Alternative GIMP print plug-in from the Gutenprint project
Group:          Hardware/Printing

%description -n gutenprint-gimpplugin
The enhanced Gutenprint GIMP print plug-in offers an alternative
with additional capabilities to the plugin supplied with GIMP.
See the user's manual at /usr/share/gutenprint/doc/gutenprint-users-manual.pdf
%endif

%prep
# Be quiet when unpacking:
%setup -q -n gutenprint-%{tarball_version}

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
           --enable-libgutenprintui2 \
           --%{enable_or_disable_escputil} \
           --%{enable_or_disable_cups_1_2_enhancements} \
           --%{with_or_without_gimp2}
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
# Remove libtool archives
rm -rf %{buildroot}%{_libdir}/*.la
# Work with upstream compliant CUPS 1.4 on all platforms
# which means to have a fixed "/usr/lib/cups/" directory
# on all platforms (see Novell/Suse Bugzilla bnc#575544).
# Do not do this for SLE11 and SLE10 where still /usr/lib64/cups/ is used on x86_64:
%if 0%{?suse_version} > 1110
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
%endif
%if 0%{?suse_version} != 1010
# Skip that on SLE10 because there is no .../cups/driver/ directory.
# Disable the run-time PPD generator /usr/lib/cups/driver/gutenprint.5.2
# so that it is not executed by the cups-driverd (e.g. in response to a "lpinfo -m" request)
# to avoid duplicated PPDs because we create the PPDs during compile-time (via --enable-cups-ppds)
# and provide ready-made PPDs in /usr/share/cups/model/gutenprint/... in the RPM package
# see "Regarding CUPS PPD files" at https://bugzilla.novell.com/show_bug.cgi?id=514994#c9
%if 0%{?suse_version} == 1110
# On SLE11 there is still /usr/lib64/cups/ used on x86_64.
chmod a-x $RPM_BUILD_ROOT%_libdir/cups/driver/gutenprint.%{gutenprintmajor}
%else
chmod a-x $RPM_BUILD_ROOT/usr/lib/cups/driver/gutenprint.%{gutenprintmajor}
%endif
%endif
# Move the special testpattern generator away from the usual bin directory:
mv $RPM_BUILD_ROOT/%{_bindir}/testpattern $RPM_BUILD_ROOT/%{_libdir}/gutenprint/%{gutenprintmajor}
# Remove dispensable .po files (only the .mo files are needed on the end-users's system):
rm $RPM_BUILD_ROOT/usr/share/locale/*/gutenprint_*.po
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
%if 0%{?suse_version} != 1010
# In SLE10 escputil is provided by ghostscript-library
%{_bindir}/escputil
%endif
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
%if 0%{?suse_version} == 1110 || 0%{?suse_version} == 1010
# On SLE11 and SLE10 there is still /usr/lib64/cups/ used on x86_64.
%if 0%{?suse_version} != 1010
# On SLE10 there is no .../cups/driver/ directory
%dir %_libdir/cups/driver
%_libdir/cups/driver/gutenprint.%{gutenprintmajor}
%endif
%_libdir/cups/filter/commandtocanon
%_libdir/cups/filter/commandtoepson
%_libdir/cups/filter/rastertogutenprint.%{gutenprintmajor}
%else
%dir /usr/lib/cups/driver
/usr/lib/cups/driver/gutenprint.%{gutenprintmajor}
/usr/lib/cups/filter/commandtocanon
/usr/lib/cups/filter/commandtoepson
/usr/lib/cups/filter/rastertogutenprint.%{gutenprintmajor}
%endif
%if 0%{?suse_version} >= 1140
/usr/lib/cups/backend/gutenprint52+usb
%dir /usr/share/cups/usb
/usr/share/cups/usb/net.sf.gimp-print.usb-quirks
%endif
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
%dir /usr/include/gutenprintui2
/usr/include/gutenprintui2/*
%{_libdir}/pkgconfig/gutenprint*
%{_libdir}/libgutenprint*.so

%if 0%{?suse_version} > 1110
# For SLE11 and SLE10 it is built --without-gimp2 (see above):
%files gimpplugin
%defattr(-,root,root)
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/2.0
%dir %{_libdir}/gimp/2.0/plug-ins
%{_libdir}/gimp/2.0/plug-ins/*
%endif

%changelog
