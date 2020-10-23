#
# spec file for package ghostscript
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ghostscript
# SLE12 needs special BuildRequires.
# For suse_version values see https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} == 1315
# For SLE12 by default CUPS 1.7.5 is provided and alternatively CUPS 1.5.4 is provided in the "legacy" module.
# For SLE12 build it with traditional CUPS 1.5.4 to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4
# because libcups and libcupsimage in CUPS 1.7.5 are backward compatible with CUPS 1.5.4 so that applications
# that have been built with CUPS 1.5.4 also work under CUPS 1.7.5 but the libraries in CUPS 1.7.5 provide
# some additional functions so that applications that have been built with CUPS 1.7.5 and use those
# additional functions would not work under CUPS 1.7.5.
# Only in the Printing project for SLE12 use cups154-ddk (a sub package of the cups154-SLE12 source package):
BuildRequires:  cups154-devel
%else
# Anything what is not SLE12 (i.e. SLE11 and all openSUSE versions) have "normal" BuildRequires:
BuildRequires:  cups-devel
%endif
# dbus-1-devel is needed for "configure --enable-dbus" (see below):
BuildRequires:  dbus-1-devel
BuildRequires:  freetype2-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  update-alternatives
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-fonts
BuildRequires:  zlib-devel
# Always check if latest version of penjpeg becomes compatible with ghostscript
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(libopenjp2) >= 2.3.1
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Requires:       apparmor-abstractions
%endif
Requires(post): update-alternatives
Requires(preun): update-alternatives
Summary:        The Ghostscript interpreter for PostScript and PDF
License:        AGPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://www.ghostscript.com/
# Special version needed for Ghostscript release candidates (e.g. "Version: 9.14pre15rc1" for 9.15rc1).
# Version 9.15rc1 would be newer than 9.15 (run "zypper vcmp 9.15rc1 9.15") because the rpmvercmp algorithm
# would treat 9.15rc1 as 9.15.rc.1 (alphabetic and numeric sections get separated into different elements)
# and 9.15.rc.1 is newer than 9.15 (it has one more element in the list while previous elements are equal)
# so that we use an alphabetic prefix 'pre' to make it older than 9.15 (numbers are considered newer than letters).
# But only with the alphabetic prefix "9.pre15rc1" would be older than the previous version number "9.14"
# because rpmvercmp would treat 9.pre15rc1 as 9.pre.15.rc1 and letters are older than numbers
# so that we keep additionally the previous version number to upgrade from the previous version:
# Starting SLE12/rpm-4.10, one can use tildeversions: 9.15~rc1.
#Version:        9.25pre26rc1
Version:        9.53.3
Release:        0
# Normal version for Ghostscript releases is the upstream version:
# tarball_version is used below to specify the directory via "setup -n":
# Special tarball_version needed for Ghostscript release candidates e.g. "define tarball_version 9.15rc1".
# For Ghostscript releases tarball_version and version are the same (i.e. the upstream version):
%define tarball_version %{version}
#define tarball_version 9.26rc1
# built_version is used below in the install and files sections:
# Separated built_version needed in case of Ghostscript release candidates e.g. "define built_version 9.15".
# For Ghostscript releases built_version and version are the same (i.e. the upstream version):
%define built_version %{version}
#define built_version 9.26
# Source0...Source9 is for sources from upstream:
# Special URLs for Ghostscript release candidates:
# see https://github.com/ArtifexSoftware/ghostpdl-downloads/releases
# URL for Source0:
# wget -O ghostscript-9.26rc1.tar.gz https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs9.26rc1/ghostscript-9.26rc1.tar.gz
# URL for MD5 checksums:
# wget -O gs9.26rc1.MD5SUMS https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs9.26rc1/MD5SUMS
# MD5 checksum for Source0: 6539d5b270721938936d721f279a3520 ghostscript-9.26rc1.tar.gz
#Source0:        ghostscript-%{tarball_version}.tar.gz
# Normal URLs for Ghostscript releases:
# URL for Source0:
# wget -O ghostscript-9.53.3.tar.gz https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs9533/ghostscript-9.53.3.tar.gz
# URL for MD5 checksums:
# wget -O gs9533.MD5SUMS https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs9533/MD5SUMS
# MD5 checksum for Source0: 807a5c4934a814e8a6cd83eff702f212 ghostscript-9.53.3.tar.gz
Source0:        ghostscript-%{version}.tar.gz
Source1:        apparmor_ghostscript
# Patch0...Patch9 is for patches from upstream:
# Patch2 41ef9a0bc36b9db7115fbe9623f989bfb47bbade.patch fixes compilation with FreeType 2.10.3+
# http://git.ghostscript.com/?p=ghostpdl.git;a=commitdiff;h=41ef9a0bc36b9db7115fbe9623f989bfb47bbade
# c.f. https://bugs.ghostscript.com/show_bug.cgi?id=702985
Patch2:         41ef9a0bc36b9db7115fbe9623f989bfb47bbade.patch
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
# (ghostscript_x11 is provided by the ghostscript-x11 sub-package, see below):
Provides:       ghostscript_any
Provides:       gs
Provides:       gs_lib
# There is a needless requirement for pstoraster in gutenprint up to openSUSE 11.4.
# Satisfy it to be backward compatible with installed gutenprint packages:
Provides:       pstoraster
# Replace any version of the packages ghostscript-library and ghostscript-mini silently.
# The "Obsoletes: ghostscript-mini" is intentionally unversioned because
# this package ghostscript should replace any version of ghostscript-mini.
# There is intentionally no "Provides: ghostscript-mini" here because this
# would cause a conflict when this package ghostscript should be re-replaced
# by ghostscript-library because ghostscript-library conflicts with ghostscript-mini
# so that there would be no easy way back from ghostscript to ghostscript-library.
# Different versions must be explicitly specified in Provides and Obsoletes
# to avoid a RPMLINT warning that the package obsoletes itself
# because an unversioned RPM dependency means "all versions".
# The RPM documentation http://www.rpm.org/max-rpm/s1-rpm-depend-manual-dependencies.html
# and /usr/share/doc/packages/rpm/manual/dependencies (in rpm-4.8.0 in openSUSE 11.4)
# does not show a comparison operator for "not equal" so that two obsoletes are used:
Provides:       ghostscript-library = %{version}
Obsoletes:      ghostscript-library < %{version}
Obsoletes:      ghostscript-library > %{version}
Obsoletes:      ghostscript-mini
# The ghostscript-x11 sub-package requires the exact matching version-release
# of the ghostscript main-package (see below) so that the ghostscript main-package
# should conflict with a non-matching ghostscript-x11 package to make sure
# that the ghostscript main-package is not changed without changing
# the ghostscript-x11 sub-package accordingly.
# The RPM documentation http://www.rpm.org/max-rpm/s1-rpm-depend-manual-dependencies.html
# and /usr/share/doc/packages/rpm/manual/dependencies (in rpm-4.8.0 in openSUSE 11.4)
# does not show a comparison operator for "not equal" so that two conflicts are used:
Conflicts:      ghostscript-x11 < %{version}-%{release}
Conflicts:      ghostscript-x11 > %{version}-%{release}
# When the ghostscript main-package is installed, usually the exact matching
# version-release of the ghostscript-x11 sub-package should be also installed:
Recommends:     ghostscript-x11 = %{version}-%{release}
# When the ghostscript main-package is installed, usually the CUPS filters gstoraster and gstopxl
# should be also installed. Since version 9.10 those CUPS filters are removed from Ghostscript
# and are now provided by the binary RPM sub-package cups-filters-ghostscript
# (see the cups-filters-ghostscript sub-package description).
# No RPM requirement because Ghostscript can be used without those CUPS filters
# and cups-filters-ghostscript is only available for newer openSUSE versions
# (currently since openSUSE 12.2) but in particular not for SLE11:
%if 0%{?suse_version} > 1210
Recommends:     cups-filters-ghostscript
%endif
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
/usr/share/ghostscript/%{version}/doc/Use.htm

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
# In openSUSE:Factory (dated 22 Feb. 2012) ghostview gv and texlive-bin require ghostscript_x11 (see above):
Provides:       ghostscript_x11

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
# Be quiet when unpacking and
# use a directory name matching Source0 to make it work also for ghostscript-mini:
%setup -q -n ghostscript-%{tarball_version}
# Patch2 41ef9a0bc36b9db7115fbe9623f989bfb47bbade.patch fixes compilation with FreeType 2.10.3+
# http://git.ghostscript.com/?p=ghostpdl.git;a=commitdiff;h=41ef9a0bc36b9db7115fbe9623f989bfb47bbade
# c.f. https://bugs.ghostscript.com/show_bug.cgi?id=702985
%patch2 -p1
# Patch100 remove-zlib-h-dependency.patch removes dependency on zlib/zlib.h
# in makefiles as we do not use the zlib sources from the Ghostscript upstream tarball.
# Again use the zlib sources from Ghostscript upstream
# and disable remove-zlib-h-dependency.patch because
# Ghostscript 9.21 does no longer build this way:
#patch100 -p1 -b remove-zlib-h-dependency.orig
# Patch101 ijs_exec_server_dont_use_sh.patch fixes IJS printing problem
# additionally allow exec'ing hpijs in apparmor profile was needed (bsc#1128467):
%patch101 -p1
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
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/%{name}.changes | tail -n 1 | cut -d- -f1 )" +%s)
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
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
%define gs_font_path /usr/share/fonts/truetype:/usr/share/fonts/Type1:/usr/share/fonts/CID:/usr/share/fonts/URW
# See http://bugs.ghostscript.com/show_bug.cgi?id=693100
export SUSE_ASNEEDED=0
./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --libdir=%{_libdir} \
            --datadir=%{_datadir} \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
            --with-fontpath=%{gs_font_path} \
            --with-libiconv=maybe \
            --enable-freetype \
            --with-jbig2dec \
            --enable-openjpeg \
            --enable-dynamic \
            --disable-compile-inits \
            --with-ijs \
            --enable-cups \
            --with-drivers=ALL \
            --with-x \
            --disable-gtk \
            --without-ufst \
            --without-luratech \
            --without-libpaper

# Make libgs.so and two programs which use it, gsx and gsc:
# With --disable-gtk, gsx and gsc are identical. It provides a command line
# frontend to libgs equivalent (functional and command line arguments) to
# the gs binary, but uses the shared libgs instead of static linking
make so
# Configure and make libijs (that is not done regardless whether or not --with-ijs is used above):
pushd ijs
./autogen.sh
autoreconf -fi
./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --libdir=%{_libdir} \
            --datadir=%{_datadir} \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
            --enable-shared \
            --disable-static
make
popd

%install
# Install libgs.so gsx gsc and some header files:
make soinstall DESTDIR=%{buildroot}
# Use gsc instead of gs, and remove duplicate gsx (see above)
mv %{buildroot}/%{_bindir}/{gsc,gs}
rm %{buildroot}/%{_bindir}/gsx
# Install libijs and its header files:
pushd ijs
make install DESTDIR=%{buildroot}
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
for D in $( LD_LIBRARY_PATH=%{buildroot}/%{_libdir} %{buildroot}/usr/bin/gs -h | sed -n -e '/^Available devices:/,/^Search path:/p' | egrep -v '^Available devices:|^Search path:' )
do for F in $catalog_devices_source_files
   do sed -n -e '/ Catalog /,/ End of catalog /p' $F | grep "[[:space:]]$D[[:space:]]" | grep -o '[[:alnum:]].*' | tr -s '[:blank:]' ' ' | sed -e 's/ /\t/' | expand -t16 >>catalog.devices
   done
done
# Switch back to the usual build log messages:
set -x
install -m 644 catalog.devices $DOCDIR
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apparmor.d/ghostscript

# Move /usr/bin/gs to /usr/bin/gs.bin to be able to use update-alternatives
install -d %buildroot%{_sysconfdir}/alternatives
mv %{buildroot}%{_bindir}/gs %{buildroot}%{_bindir}/gs.bin
ln -sf %{_bindir}/gs.bin %{buildroot}%{_sysconfdir}/alternatives/gs
ln -sf %{_sysconfdir}/alternatives/gs %{buildroot}%{_bindir}/gs

%post
/sbin/ldconfig
%if 0%{?suse_version} >= 1500
%apparmor_reload /etc/apparmor.d/ghostscript
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
%defattr(-, root, root)
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
%doc %{_mandir}/man1/dvipdf.1.gz
%doc %{_mandir}/man1/eps2eps.1.gz
%doc %{_mandir}/man1/gs.1.gz
%doc %{_mandir}/man1/gsbj.1.gz
%doc %{_mandir}/man1/gsdj.1.gz
%doc %{_mandir}/man1/gsdj500.1.gz
%doc %{_mandir}/man1/gslj.1.gz
%doc %{_mandir}/man1/gslp.1.gz
%doc %{_mandir}/man1/gsnd.1.gz
%doc %{_mandir}/man1/pdf2dsc.1.gz
%doc %{_mandir}/man1/pdf2ps.1.gz
%doc %{_mandir}/man1/pf2afm.1.gz
%doc %{_mandir}/man1/pfbtopfa.1.gz
%doc %{_mandir}/man1/printafm.1.gz
%doc %{_mandir}/man1/ps2ascii.1.gz
%doc %{_mandir}/man1/ps2epsi.1.gz
%doc %{_mandir}/man1/ps2pdf.1.gz
%doc %{_mandir}/man1/ps2pdf12.1.gz
%doc %{_mandir}/man1/ps2pdf13.1.gz
%doc %{_mandir}/man1/ps2pdf14.1.gz
%doc %{_mandir}/man1/ps2pdfwr.1.gz
%doc %{_mandir}/man1/ps2ps.1.gz
%doc %{_mandir}/de/man1/dvipdf.1.gz
%doc %{_mandir}/de/man1/eps2eps.1.gz
%doc %{_mandir}/de/man1/gsnd.1.gz
%doc %{_mandir}/de/man1/pdf2dsc.1.gz
%doc %{_mandir}/de/man1/pdf2ps.1.gz
%doc %{_mandir}/de/man1/printafm.1.gz
%doc %{_mandir}/de/man1/ps2ascii.1.gz
%doc %{_mandir}/de/man1/ps2pdf.1.gz
%doc %{_mandir}/de/man1/ps2pdf12.1.gz
%doc %{_mandir}/de/man1/ps2pdf13.1.gz
%doc %{_mandir}/de/man1/ps2pdf14.1.gz
%doc %{_mandir}/de/man1/ps2ps.1.gz
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
%exclude %{_libdir}/ghostscript/%{built_version}/X11.so
%if 0%{?suse_version} < 1500
%dir %{_sysconfdir}/apparmor.d
%endif
%{_sysconfdir}/apparmor.d/ghostscript

%files x11
%defattr(-,root,root)
%{_libdir}/ghostscript/%{built_version}/X11.so

%files devel
%defattr(-,root,root)
%{_includedir}/ghostscript/
%{_libdir}/libgs.so
%{_includedir}/ijs/
%{_libdir}/libijs.so
%{_libdir}/pkgconfig/ijs.pc

%changelog
