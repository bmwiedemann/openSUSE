#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%endif
# built_version is used below in the install and files sections:
# Separated built_version needed in case of Ghostscript release candidates e.g. "define built_version 9.15".
# For Ghostscript releases built_version and version are the same (i.e. the upstream version):
%define built_version %{version}
Name:           ghostscript%{psuffix}
Version:        9.56.1
Release:        0
Summary:        The Ghostscript interpreter for PostScript and PDF
License:        AGPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://www.ghostscript.com/
# sha512:fe5a5103c081dd87cf8b3e0bbbd0df004c0e4e04e41bded7c70372916e6e26249a0e8fa434b561292964c5f3820ee6c60ef1557827a6efb5676012ccb73ded85
Source0:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs9561/ghostscript-%{version}.tar.xz
Source10:       apparmor_ghostscript
# Patch0...Patch9 is for patches from upstream:
# Source10...Source99 is for sources from SUSE which are intended for upstream:
# Patch10...Patch99 is for patches from SUSE which are intended for upstream:
# Source100...Source999 is for sources from SUSE which are not intended for upstream:
# Patch100...Patch999 is for patches from SUSE which are not intended for upstream:
# Patch100 remove-zlib-h-dependency.patch removes dependency on zlib/zlib.h
# in makefiles as we do not use the zlib sources from the Ghostscript upstream tarball:
Patch100:       remove-zlib-h-dependency.patch
# Patch101 ijs_exec_server_dont_use_sh.patch fixes IJS printing problem
# additionally allow exec'ing hpijs in apparmor profile was needed (bsc#1128467):
Patch101:       ijs_exec_server_dont_use_sh.patch
# Patch102 CVE-2023-28879.patch is
# https://git.ghostscript.com/?p=ghostpdl.git;a=commitdiff;h=37ed5022cecd
# that fixes CVE-2023-28879 Buffer Overflow in s_xBCPE_process
# cf. https://bugs.ghostscript.com/show_bug.cgi?id=706494
# and https://bugzilla.suse.com/show_bug.cgi?id=1210062
Patch102:       CVE-2023-28879.patch
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
# RPM dependencies:
# Additional RPM Provides of the ghostscript-library packages in openSUSE 11.4 from
# "rpm -q --provides ghostscript-library" and "rpm -q --provides ghostscript-x11":
#   ghostscript
#   gs
#   gs_lib
#   pstoraster
#   ghostscript_any
#   ghostscript-serv
#   gs_x11
#   ghostscript_x11
#   ghostscript-mini
# Which of those are actually used in openSUSE:Factory (dated 22 Feb. 2012):
#   ghostscript
#   gs
#   gs_lib
#   ghostscript_any
#   ghostscript_x11
#   ghostscript-mini
# Which other packages need those in openSUSE:Factory (dated 22 Feb. 2012):
#   webdot           Requires      ghostscript
#   ddd              BuildRequires ghostscript_any
#   emacs-auctex     BuildRequires ghostscript_any
#   kernel-docs      BuildRequires ghostscript_any
#   texlive-bin      BuildRequires ghostscript_any
#   cups             Requires      ghostscript_any
#   html2ps          Requires      ghostscript_any
#   latex2html       Requires      ghostscript_any
#   pstoedit         Requires      ghostscript_any
#   ghostview        Requires      ghostscript_x11
#   gv               Requires      ghostscript_x11
#   texlive-bin      Requires      ghostscript_x11
#   klatexformula    BuildRequires gs and Requires gs
#   capi4hylafax     Requires      gs_lib
#   hylafax          Requires      gs_lib
#   graphviz-plugins BuildRequires ghostscript-mini
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
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-fonts
%if 0%{?suse_version} == 1315
BuildRequires:  cups154-devel
%else
BuildRequires:  cups-devel
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
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
Provides:       gs = %{version}
Provides:       gs_lib = %{version}
# There is a needless requirement for pstoraster in gutenprint up to openSUSE 11.4.
# Satisfy it to be backward compatible with installed gutenprint packages:
Provides:       pstoraster
Provides:       %{version}
Provides:       ghostscript-library = %{version}
Obsoletes:      ghostscript-library < %{version}
# The "Obsoletes: ghostscript-mini" is intentionally unversioned because
# this package ghostscript should replace any version of ghostscript-mini.
Obsoletes:      ghostscript-mini
%if 0%{?suse_version} > 1210
Recommends:     cups-filters-ghostscript
%endif
%endif

%description
Ghostscript is a package of software that provides:

An interpreter for the PostScript language,
with the ability to convert PostScript language files
to many raster formats, view them on displays,
and print them on printers that don't have
PostScript language capability built in.

An interpreter for Portable Document Format (PDF) files,
with the same abilities.

The ability to convert PostScript language files
to PDF (with some limitations) and vice versa.

A set of C procedures (the Ghostscript library)
that implement the graphics and filtering
(data compression / decompression / conversion)
capabilities that appear as primitive operations
in the PostScript language and in PDF.

For information how to use Ghostscript see
%{_datadir}/ghostscript/%{version}/doc/Use.htm

%package x11
Summary:        X11 library for Ghostscript
# Require the exact matching version-release of the ghostscript main-package because
# a non-matching ghostscript main-package may let it fail or even crash (e.g. segfault)
# because all Ghostscript software is built from one same Ghostscript source tar ball
# so that there could be any kind of Ghostscript-internal dependencies.
# The exact matching version-release of the ghostscript main-package is available
# on the same package repository where the ghostscript-x11 sub-package is because
# all are built simulaneously from the same Ghostscript source package:
Group:          Productivity/Publishing/PS
Requires:       ghostscript = %{version}-%{release}
# Unfortunately ghostscript-library.spec and ghostscript-mini.spec have
# an unversioned "Provides: ghostscript" and for RPM this means that both
# ghostscript-library and ghostscript-mini provide any version of "ghostscript"
# so that any version of ghostscript-library and ghostscript-mini fulfills
# the above versioned requirement which is wrong and therefore an explicit conflicts
# is used here to avoid the mess.
# Above the ghostscript main package "Provides: ghostscript-library = version" so that
# versioned conflicts are needed to avoid a conflict with the ghostscript main package.
# The RPM documentation http://www.rpm.org/max-rpm/s1-rpm-depend-manual-dependencies.html
# and /usr/share/doc/packages/rpm/manual/dependencies (in rpm-4.8.0 in openSUSE 11.4)
# does not show a comparison operator for "not equal" so that two conflicts are used:
Conflicts:      ghostscript-library < %{version}
Conflicts:      ghostscript-library > %{version}
Conflicts:      ghostscript-mini
Provides:       ghostscript_x11 = %{version}

%description x11
This package contains the X11 library which is needed
to view PostScript and PDF files with Ghostscript
under the X Window System.

%package devel
Summary:        Development files for Ghostscript
Group:          Development/Libraries/C and C++
Requires:       ghostscript = %{version}
# Unfortunately ghostscript-library.spec and ghostscript-mini.spec have
# an unversioned "Provides: ghostscript" and for RPM this means that both
# ghostscript-library and ghostscript-mini provide any version of "ghostscript"
# so that any version of ghostscript-library and ghostscript-mini fulfills
# the above versioned requirement which is wrong and therefore an explicit conflicts
# is used here to avoid the mess.
# Above the ghostscript main package "Provides: ghostscript-library = version" so that
# versioned conflicts are needed to avoid a conflict with the ghostscript main package.
# The RPM documentation http://www.rpm.org/max-rpm/s1-rpm-depend-manual-dependencies.html
# and /usr/share/doc/packages/rpm/manual/dependencies (in rpm-4.8.0 in openSUSE 11.4)
# does not show a comparison operator for "not equal" so that two conflicts are used:
Conflicts:      ghostscript-library < %{version}
Conflicts:      ghostscript-library > %{version}
Conflicts:      ghostscript-mini
Conflicts:      ghostscript-mini-devel

%description devel
This package contains the development files for Ghostscript.

%prep
%setup -q -n ghostscript-%{version}

# Patch100 remove-zlib-h-dependency.patch removes dependency on zlib/zlib.h
# in makefiles as we do not use the zlib sources from the Ghostscript upstream tarball.
# Again use the zlib sources from Ghostscript upstream
# and disable remove-zlib-h-dependency.patch because
# Ghostscript 9.21 does no longer build this way:
#patch100 -p1 -b remove-zlib-h-dependency.orig
# Patch101 ijs_exec_server_dont_use_sh.patch fixes IJS printing problem
# additionally allow exec'ing hpijs in apparmor profile was needed (bsc#1128467):
%patch101 -p1
# Patch102 CVE-2023-28879.patch is
# https://git.ghostscript.com/?p=ghostpdl.git;a=commitdiff;h=37ed5022cecd
# that fixes CVE-2023-28879 Buffer Overflow in s_xBCPE_process
# cf. https://bugs.ghostscript.com/show_bug.cgi?id=706494
# and https://bugzilla.suse.com/show_bug.cgi?id=1210062
%patch102
# Remove patch backup files to avoid packaging
# cf. https://build.opensuse.org/request/show/581052
rm -f Resource/Init/*.ps.orig
# Do not use the freetype jpeg libpng tiff zlib sources from the Ghostscript upstream tarball
# because we prefer to use for long-established standard libraries the ones from SUSE
# in particular to automatically get SUSE security updates for standard libraries.
# In contrast we use e.g. lcms2 from the Ghostscript upstream tarball because this one
# is specially modified to work with Ghostscript so that we cannot use lcms2 from SUSE:
#rm -rf freetype jpeg libpng tiff zlib
# Again use the zlib sources from Ghostscript upstream
# and disable remove-zlib-h-dependency.patch because
# Ghostscript 9.21 does no longer build this way:
%if 0%{?suse_version} == 1315
# Again use the freetype sources from Ghostscript upstream because
# Ghostscript 9.27 does no longer build this way for SLE12:
rm -rf jpeg libpng tiff
%else
rm -rf freetype jpeg libpng tiff
%endif
%if 0%{?suse_version} >= 1550
rm -rf openjpeg
%endif
rm -rf zlib
# In contrast to the above we use lcms2 from SUSE since Ghostscript 9.23rc1
# because that is what Ghostscript upstream recommends according to
# https://ghostscript.com/pipermail/gs-devel/2018-March/010061.html
# because singe Ghostscript 9.23rc1 there is no longer lcms2 in Ghostscript
# but now it is lcms2art (the beginning of a lcms2 fork - see News.htm).
# On SLE11 and on SLE12-SP1 there is liblcms2-2-2.5
# which is too old so that configure fails there with
#   checking for local lcms2 library source... no
#   checking for system lcms2 library... checking for _cmsCreateMutex in -llcms2... no
#   configure: error: lcms2 not found, or too old
# (on SLE12-SP2 there is liblcms2-2-2.7 which is not too old)
# but there is no configure option to build it without lcms2
# so that for SLE11 and SLE12-SP1 it is built with lcms2art in Ghostscript
# i.e. lcms2art in Ghostscript is only removed when not SLE11 or SLE12-SP1
# cf. https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} == 1110 || 0%{?sle_version} == 120100
echo "Building it with lcms2art in Ghostscript"
%else
rm -rf lcms2art
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
# --without-ufst and --without-luratech because those are relevant to commercial releases only
#   which would require a commercial license.
# --disable-compile-inits to disable compiling of resources (Fonts, init postscript files, ...)
#   into the library, which is the upstream recommendation for distributions. This also allows
#   unbundling the 35 Postscript Standard fonts, provided by the URW font package
# --without-libpaper disables libpaper support because SUSE does not have libpaper.
%define gs_font_path %{_datadir}/fonts/truetype:%{_datadir}/fonts/Type1:%{_datadir}/fonts/CID:%{_datadir}/fonts/URW
# See http://bugs.ghostscript.com/show_bug.cgi?id=693100
export SUSE_ASNEEDED=0
%configure \
    --with-fontpath=%{gs_font_path} \
    --with-libiconv=maybe \
    --enable-freetype \
    --with-jbig2dec \
    --enable-openjpeg \
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
    --without-local-zlib \
    --with-ijs \
    --enable-cups \
    --with-drivers=ALL \
    --with-x \
%endif
    --disable-gtk \
    --without-ufst \
    --without-luratech \
    --without-libpaper

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
EXAMPLESDIR=%{buildroot}%{_datadir}/ghostscript/%{built_version}/examples
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
DOCDIR=%{buildroot}%{_datadir}/doc/ghostscript/%{built_version}
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
ln -s ../ghostscript/%{built_version} ghostscript
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
%if "%{flavor}" != "mini"
install -D -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/apparmor.d/ghostscript
%endif

# Move /usr/bin/gs to /usr/bin/gs.bin to be able to use update-alternatives
install -d %{buildroot}%{_sysconfdir}/alternatives
mv %{buildroot}%{_bindir}/gs %{buildroot}%{_bindir}/gs.bin
ln -sf %{_bindir}/gs.bin %{buildroot}%{_sysconfdir}/alternatives/gs
ln -sf %{_sysconfdir}/alternatives/gs %{buildroot}%{_bindir}/gs

%post
/sbin/ldconfig
%if "%{flavor}" != "mini"
%if 0%{?suse_version} >= 1500
%apparmor_reload %{_sysconfdir}/apparmor.d/ghostscript
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
%{_mandir}/de/man1/dvipdf.1%{?ext_man}
%{_mandir}/de/man1/eps2eps.1%{?ext_man}
%{_mandir}/de/man1/gsnd.1%{?ext_man}
%{_mandir}/de/man1/pdf2dsc.1%{?ext_man}
%{_mandir}/de/man1/pdf2ps.1%{?ext_man}
%{_mandir}/de/man1/printafm.1%{?ext_man}
%{_mandir}/de/man1/ps2ascii.1%{?ext_man}
%{_mandir}/de/man1/ps2pdf.1%{?ext_man}
%{_mandir}/de/man1/ps2pdf12.1%{?ext_man}
%{_mandir}/de/man1/ps2pdf13.1%{?ext_man}
%{_mandir}/de/man1/ps2pdf14.1%{?ext_man}
%{_mandir}/de/man1/ps2ps.1%{?ext_man}
%doc %{_defaultdocdir}/ghostscript
%dir %{_datadir}/doc/ghostscript
%doc %{_datadir}/doc/ghostscript/%{built_version}
%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/%{built_version}
%{_datadir}/ghostscript/%{built_version}/Resource
%{_datadir}/ghostscript/%{built_version}/iccprofiles
%{_datadir}/ghostscript/%{built_version}/examples/
%{_datadir}/ghostscript/%{built_version}/lib/
%{_libdir}/libgs.so.*
%{_libdir}/ghostscript/
%{_libdir}/libijs-0.35.so
%if "%{flavor}" != "mini"
%exclude %{_libdir}/ghostscript/%{built_version}/X11.so
%if 0%{?suse_version} < 1500
%dir %{_sysconfdir}/apparmor.d
%endif
%{_sysconfdir}/apparmor.d/ghostscript

%files x11
%{_libdir}/ghostscript/%{built_version}/X11.so
%endif

%files devel
%{_includedir}/ghostscript/
%{_libdir}/libgs.so
%{_includedir}/ijs/
%{_libdir}/libijs.so
%{_libdir}/pkgconfig/ijs.pc

%changelog
