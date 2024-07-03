#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "mini"
%global psuffix -mini
%else
%global psuffix %{nil}
%bcond_without  apparmor
%endif
Name:           ghostscript%{psuffix}
Version:        10.03.1
Release:        0
Summary:        The Ghostscript interpreter for PostScript and PDF
License:        AGPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://www.ghostscript.com/
# How to manually get Source0:
# Go to https://www.ghostscript.com
# -> "The current Ghostscript release 10.03.1 can be downloaded here" https://www.ghostscript.com/releases/index.html
# -> "Ghostscript" https://www.ghostscript.com/releases/gsdnld.html
# -> "Ghostscript 10.03.1 Source for all platforms / GNU Affero General Public License" = "Ghostscript AGPL Release"
# https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10031/ghostscript-10.03.1.tar.gz
Source0:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10031/ghostscript-10.03.1.tar.gz
Source10:       apparmor_ghostscript
# Patch0...Patch9 is for patches from upstream:
# Source10...Source99 is for sources from SUSE which are intended for upstream:
# Patch10...Patch99 is for patches from SUSE which are intended for upstream:
# Source100...Source999 is for sources from SUSE which are not intended for upstream:
# Patch100...Patch999 is for patches from SUSE which are not intended for upstream:
# Patch101 ijs_exec_server_dont_use_sh.patch fixes IJS printing problem
# additionally allow exec'ing hpijs in apparmor profile was needed (bsc#1128467):
Patch101:       ijs_exec_server_dont_use_sh.patch
# Build Requirements:
BuildRequires:  freetype2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-alternatives
BuildRequires:  zlib-devel
Requires(post): update-alternatives
Requires(preun):update-alternatives
# Provide the additional RPM Provides of the ghostscript-library package
# (ghostscript_x11 is provided by the ghostscript-x11 sub-package, see below).
# The "Provides: ghostscript_any" is there to support "BuildRequires: ghostscript_any"
# so other packages can build with any available Ghostscript implementation,
# either ghostscript or ghostscript-mini ("BuildRequires: ghostscript-mini" should not
# be used because ghostscript-mini does not exist outside of OBS so other packages that
# use "BuildRequires: ghostscript-mini" could not be built in published products).
# The "Provides: ghostscript_any" does not affect end-users who should not get
# ghostscript-mini installed (but only the full featured ghostscript package)
# because ghostscript-mini (and ghostscript-mini-devel) are not published
# in openSUSE products, cf. https://build.opensuse.org/request/show/877083
Provides:       ghostscript_any = %{version}
%if "%{flavor}" != "mini"
BuildRequires:  dbus-1-devel
BuildRequires:  libexpat-devel
BuildRequires:  xorg-x11-fonts
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
%if 0%{?suse_version} == 1315
BuildRequires:  cups154-devel
%else
BuildRequires:  cups-devel
%endif
%if %{with apparmor}
%if 0%{?suse_version} >= 1500
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
%endif
%endif
%endif
# Always check if latest version of openjpeg becomes compatible with ghostscript
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(libopenjp2) >= 2.3.1
%endif
%if "%{flavor}" == "mini"
Conflicts:      ghostscript
Conflicts:      ghostscript-devel
Conflicts:      ghostscript-library
Conflicts:      ghostscript-x11
%else
Recommends:     ghostscript-x11 = %{version}-%{release}
Conflicts:      ghostscript-x11 < %{version}-%{release}
Provides:       %{version}
Provides:       ghostscript-library = %{version}
Provides:       gs = %{version}
Provides:       gs_lib = %{version}
Provides:       pstoraster
Obsoletes:      ghostscript-library < %{version}
# The "Obsoletes: ghostscript-mini" is intentionally unversioned because
# this package ghostscript should replace any version of ghostscript-mini.
Obsoletes:      ghostscript-mini
%if 0%{?suse_version} > 1210
Recommends:     (cups-filters-ghostscript if cups)
%endif
%endif

%description
Ghostscript is a package of software that provides:

An interpreter for the PostScript language, with the ability to convert
PostScript language files to many raster formats, view them on displays, and
print them on printers that don't have PostScript language capability built in.

An interpreter for Portable Document Format (PDF) files, with the same
abilities.

The ability to convert PostScript language files to PDF (with some limitations)
and vice versa.

A set of C procedures (the Ghostscript library) that implement the graphics and
filtering (data compression / decompression / conversion) capabilities that
appear as primitive operations in the PostScript language and in PDF.

For information how to use Ghostscript see
%{_datadir}/ghostscript/%{version}/doc/Use.htm

%package x11
Summary:        X11 library for Ghostscript
Group:          Productivity/Publishing/PS
Requires:       ghostscript = %{version}-%{release}
Conflicts:      ghostscript-library < %{version}
Conflicts:      ghostscript-library > %{version}
Conflicts:      ghostscript-mini
Provides:       ghostscript_x11 = %{version}

%description x11
This package contains the X11 library which is needed to view PostScript and
PDF files with Ghostscript under the X Window System.

%package devel
Summary:        Development files for Ghostscript
Group:          Development/Libraries/C and C++
Requires:       ghostscript = %{version}
Conflicts:      ghostscript-library < %{version}
Conflicts:      ghostscript-library > %{version}
Conflicts:      ghostscript-mini
Conflicts:      ghostscript-mini-devel

%description devel
This package contains the development files for Ghostscript.

%prep
%setup -q -n ghostscript-%{version}

# Patch101 ijs_exec_server_dont_use_sh.patch fixes IJS printing problem
# additionally allow exec'ing hpijs in apparmor profile was needed (bsc#1128467):
%patch -P 101 -p1
# Remove patch backup files to avoid packaging
# cf. https://build.opensuse.org/request/show/581052
rm -f Resource/Init/*.ps.orig
rm -rf freetype jpeg libpng lcms2art zlib tiff
%if 0%{?suse_version} >= 1550
rm -rf openjpeg
%endif

%build
# Derive build timestamp from latest changelog entry
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/%{name}.changes | tail -n 1 | cut -d- -f1 )" +%{s})
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} -fno-strict-aliasing -fPIC"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fPIC"
export LDFLAGS="-pie"
autoreconf -fi
# --docdir=%%{_defaultdocdir}/%%{name} does not work therefore it is not used.
# --enable-cups but no longer --with-pdftoraster --enable-dbus --with-install-cups because
#   --with-install-cups was introduced in version 9.04 but meanwhile it is an unrecognized option by configure
#   because cups/filter/gstoraster and cups/filter/gstopxl and related files gstoraster.convs pxlcolor.ppd pxlmono.ppd
#   are no longer provided by Ghostscript but were moved to the cups-filters package.
#   also pdftoraster is provided by cups-filters and there is colord support that
#   would need --enable-dbus because colord is accessed via D-Bus.
# --with-ijs to enable IJS printer driver support (in particular needed by HPIJS).
# --with-drivers=ALL to all file format drivers and all printer drivers.
# --with-x to use the X Window System.
# --enable-openjpeg because since Ghostscript 9.05 JasPer is deprecated
#   (--without-jasper is now an unrecognized option by configure)
#   and Ghostscript now ships modified OpenJPEG sources for JPEG2000 decoding
#   (replacing JasPer - although JasPer is still included for this release)
#   Performance, reliability and memory use whilst decoding JPX streams are all improved.
#   see also http://bugs.ghostscript.com/show_bug.cgi?id=691430
# --without-ufst because this is relevant to commercial releases only
#   which would require a commercial license.
# --disable-compile-inits to disable compiling of resources (Fonts, init postscript files, ...)
#   into the library, which is the upstream recommendation for distributions. This also allows
#   unbundling the 35 Postscript Standard fonts, provided by the URW font package
# --without-libpaper disables libpaper support because SUSE does not have libpaper.
# --without-tesseract because this requires C++ (it might be added if Tesseract support in Ghostscript is needed).
%define gs_font_path %{_datadir}/fonts/truetype:%{_datadir}/fonts/Type1:%{_datadir}/fonts/CID:%{_datadir}/fonts/URW
# See http://bugs.ghostscript.com/show_bug.cgi?id=693100
export SUSE_ASNEEDED=0
%configure \
    --with-fontpath=%{gs_font_path} \
    --with-libiconv=maybe \
    --enable-freetype \
    --with-jbig2dec \
    --enable-openjpeg \
    --disable-hidden-visibility \
    --enable-dynamic \
    --disable-compile-inits \
%if "%{flavor}" == "mini"
    --without-ijs \
    --disable-cups \
    --disable-dbus \
    --without-pdftoraster \
    --with-drivers=FILES \
    --without-x \
%else
    --with-ijs \
    --enable-cups \
    --enable-dbus \
    --without-pdftoraster \
    --with-drivers=ALL \
    --with-x \
%endif
    --without-local-zlib \
    --with-system-libtiff \
    --disable-gtk \
    --without-ufst \
    --without-libpaper \
    --without-tesseract

# Make libgs.so and two programs which use it, gsx and gsc:
# With --disable-gtk, gsx and gsc are identical. It provides a command line
# frontend to libgs equivalent (functional and command line arguments) to
# the gs binary, but uses the shared libgs instead of static linking
%make_build so
# Configure and make libijs (that is not done regardless whether or not --with-ijs is used above):
pushd ijs
./autogen.sh
autoreconf -fi
%configure --enable-shared --disable-static
%make_build
popd

%install
# Install libgs.so gsx gsc and some header files:
make soinstall DESTDIR=%{buildroot}
# Use gsc instead of gs, and remove duplicate gsx (see above)
mv %{buildroot}/%{_bindir}/{gsc,gs}
rm %{buildroot}/%{_bindir}/gsx
# Install libijs and its header files:
pushd ijs
%make_install
popd
# Remove installed ijs example client and server and its .la file:
rm %{buildroot}%{_bindir}/ijs_client_example
rm %{buildroot}%{_bindir}/ijs_server_example
rm %{buildroot}%{_libdir}/libijs.la
# Install examples:
EXAMPLESDIR=%{buildroot}%{_datadir}/ghostscript/%{version}/examples
test -d $EXAMPLESDIR || install -d $EXAMPLESDIR
for E in examples/*
do install -m 644 $E $EXAMPLESDIR || :
done
test -d $EXAMPLESDIR/cjk || install -d $EXAMPLESDIR/cjk
for E in examples/cjk/*
do install -m 644 $E $EXAMPLESDIR/cjk || :
done
# Install documentation which is not installed by default
# see http://bugs.ghostscript.com/show_bug.cgi?id=693002
# and fail intentionally as notification if something changed:
DOCDIR=%{buildroot}%{_datadir}/doc/ghostscript/%{version}
for D in LICENSE
do test -e $DOCDIR/$( basename $D ) && exit 99
   install -m 644 $D $DOCDIR
done
# Add a link named 'ghostscript' from SUSE's usual documentation directory /usr/share/doc/packages
# with link target Ghostscript's documentation directory e.g. /usr/share/doc/ghostscript/9.23
# as relative link to get the link independent of the buildroot prefix
# i.e. in /usr/share/doc/packages add the link ghostscript -> ../ghostscript/9.23
# because "configure --docdir=%%{_defaultdocdir}/%%{name}" does not work (see above):
install -d -m 755 %{buildroot}%{_defaultdocdir}
pushd %{buildroot}%{_defaultdocdir}
ln -s ../ghostscript/%{version} ghostscript
popd
# Extract the catalog of devices which are actually built-in in exactly this Ghostscript:
# If a needed source file is no longer accessible fail intentionally as notification
# that something changed which needs adaptions here:
catalog_devices_source_files="devices/devs.mak devices/dcontrib.mak contrib/contrib.mak"
for F in $catalog_devices_source_files
do test -r $F || exit 99
done
# Do not pollute the build log file with zillions of meaningless messages:
set +x
cat /dev/null >catalog.devices
for D in $( LD_LIBRARY_PATH=%{buildroot}/%{_libdir} %{buildroot}%{_bindir}/gs -h | sed -n -e '/^Available devices:/,/^Search path:/p' | grep -E -v '^Available devices:|^Search path:' )
do for F in $catalog_devices_source_files
   do sed -n -e '/ Catalog /,/ End of catalog /p' $F | grep "[[:space:]]$D[[:space:]]" | grep -o '[[:alnum:]].*' | tr -s '[:blank:]' ' ' | sed -e 's/ /\t/' | expand -t16 >>catalog.devices
   done
done
# Switch back to the usual build log messages:
set -x
install -m 644 catalog.devices $DOCDIR
%if %{with apparmor}
%if "%{flavor}" != "mini"
install -D -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/apparmor.d/ghostscript
%endif
%endif

# Move /usr/bin/gs to /usr/bin/gs.bin to be able to use update-alternatives
install -d %{buildroot}%{_sysconfdir}/alternatives
mv %{buildroot}%{_bindir}/gs %{buildroot}%{_bindir}/gs.bin
ln -sf %{_bindir}/gs.bin %{buildroot}%{_sysconfdir}/alternatives/gs
ln -sf %{_sysconfdir}/alternatives/gs %{buildroot}%{_bindir}/gs

%post
/sbin/ldconfig
%if %{with apparmor}
%if "%{flavor}" != "mini"
%if 0%{?suse_version} >= 1500
%apparmor_reload %{_sysconfdir}/apparmor.d/ghostscript
%endif
%endif
%endif
%{_sbindir}/update-alternatives \
  --install %{_bindir}/gs gs %{_bindir}/gs.bin 15

%postun -p /sbin/ldconfig

%preun
if test $1 -eq 0 ; then
    %{_sbindir}/update-alternatives \
    --remove gs %{_bindir}/gs.bin
fi

%files
%license LICENSE
%ghost %config %{_sysconfdir}/alternatives/gs
%{_bindir}/dvipdf
%{_bindir}/eps2eps
%{_bindir}/gs
%{_bindir}/gs.bin
%{_bindir}/gsbj
%{_bindir}/gsdj
%{_bindir}/gsdj500
%{_bindir}/gslj
%{_bindir}/gslp
%{_bindir}/gsnd
%{_bindir}/lprsetup.sh
%{_bindir}/pdf2dsc
%{_bindir}/pdf2ps
%{_bindir}/pf2afm
%{_bindir}/pfbtopfa
%{_bindir}/pphs
%{_bindir}/printafm
%{_bindir}/ps2ascii
%{_bindir}/ps2epsi
%{_bindir}/ps2pdf
%{_bindir}/ps2pdf12
%{_bindir}/ps2pdf13
%{_bindir}/ps2pdf14
%{_bindir}/ps2pdfwr
%{_bindir}/ps2ps
%{_bindir}/ps2ps2
%{_bindir}/unix-lpr.sh
%{_mandir}/man1/dvipdf.1%{?ext_man}
%{_mandir}/man1/eps2eps.1%{?ext_man}
%{_mandir}/man1/gs.1%{?ext_man}
%{_mandir}/man1/gsbj.1%{?ext_man}
%{_mandir}/man1/gsdj.1%{?ext_man}
%{_mandir}/man1/gsdj500.1%{?ext_man}
%{_mandir}/man1/gslj.1%{?ext_man}
%{_mandir}/man1/gslp.1%{?ext_man}
%{_mandir}/man1/gsnd.1%{?ext_man}
%{_mandir}/man1/pdf2dsc.1%{?ext_man}
%{_mandir}/man1/pdf2ps.1%{?ext_man}
%{_mandir}/man1/pf2afm.1%{?ext_man}
%{_mandir}/man1/pfbtopfa.1%{?ext_man}
%{_mandir}/man1/printafm.1%{?ext_man}
%{_mandir}/man1/ps2ascii.1%{?ext_man}
%{_mandir}/man1/ps2epsi.1%{?ext_man}
%{_mandir}/man1/ps2pdf.1%{?ext_man}
%{_mandir}/man1/ps2pdf12.1%{?ext_man}
%{_mandir}/man1/ps2pdf13.1%{?ext_man}
%{_mandir}/man1/ps2pdf14.1%{?ext_man}
%{_mandir}/man1/ps2pdfwr.1%{?ext_man}
%{_mandir}/man1/ps2ps.1%{?ext_man}
%doc %{_defaultdocdir}/ghostscript
%dir %{_datadir}/doc/ghostscript
%doc %{_datadir}/doc/ghostscript/%{version}
%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/%{version}
%{_datadir}/ghostscript/%{version}/Resource
%{_datadir}/ghostscript/%{version}/iccprofiles
%{_datadir}/ghostscript/%{version}/examples/
%{_datadir}/ghostscript/%{version}/lib/
%{_libdir}/libgs.so.*
%{_libdir}/ghostscript/
%{_libdir}/libijs-0.35.so
%if "%{flavor}" != "mini"
%exclude %{_libdir}/ghostscript/%{version}/X11.so
%if %{with apparmor}
%if 0%{?suse_version} < 1500
%dir %{_sysconfdir}/apparmor.d
%endif
%{_sysconfdir}/apparmor.d/ghostscript
%endif

%files x11
%{_libdir}/ghostscript/%{version}/X11.so
%endif

%files devel
%{_includedir}/ghostscript/
%{_libdir}/libgs.so
%{_includedir}/ijs/
%{_libdir}/libijs.so
%{_libdir}/pkgconfig/ijs.pc

%changelog
