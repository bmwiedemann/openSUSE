#
# spec file for package hplip
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


# python-rpm-macros doesn't work for hplip!
# We just build for py3 since SLE15
%define pyversion 3
%define pymod() python3-%{**}
%define pyver %{py3_ver}
%define pyexe %{_bindir}/python3
%global use_qt5 1
Name:           hplip
Version:        3.24.4
Release:        0
Summary:        HP's Printing, Scanning, and Faxing Software
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Hardware/Printing
URL:            https://developers.hp.com/hp-linux-imaging-and-printing
# Source0...Source9 is for sources from HP:
# URL for Source0: http://prdownloads.sourceforge.net/hplip/hplip-3.15.9.tar.gz
# URL to verify Source0: http://prdownloads.sourceforge.net/hplip/hplip-3.15.9.tar.gz.asc
# How to verify Source0 see: http://hplipopensource.com/node/327
# For example: /usr/bin/gpg --keyserver pgp.mit.edu --recv-keys 0xA59047B9
#              /usr/bin/gpg --verify hplip-3.15.9.tar.gz.asc hplip-3.15.9.tar.gz
# must result: Good signature from "HPLIP (HP Linux Imaging and Printing) <hplip@hp.com>"
Source0:        https://sourceforge.net/projects/hplip/files/hplip/%{version}/hplip-%{version}.tar.gz
Source1:        https://sourceforge.net/projects/hplip/files/hplip/%{version}/hplip-%{version}.tar.gz.asc
Source2:        hplip.keyring
# Patch0...Patch9 is for patches from HP:
# Patch10...Patch99 is for Suse patches for the sources from HP:
# Source100... is for special SUSE sources:
# Source102 is a small man page for /usr/bin/hpijs:
Source102:      hpijs.1.gz
# Actual drivers for hplip-missing-drivers.patch
Source103:      hp-laserjet_cp_1025nw.ppd.gz
Source104:      hp-laserjet_professional_p_1102w.ppd.gz
#
Source1000:     %{name}-rpmlintrc
# Patch100... is for special Suse patches:
# Patch101 change-udev-rules.diff changes the udev rules file 56-hpmud.rules
Patch101:       change-udev-rules.diff
# Patch106 disable_hp-upgrade.patch disables hp-upgrade/upgrade.py for security reasons,
# see https://bugzilla.novell.com/show_bug.cgi?id=853405
# To upgrade HPLIP an openSUSE software package manager like YaST or zypper should be used.
Patch106:       disable_hp-upgrade.patch
# PATCH-FIX-SUSE: use proper udev rulesdir which is in usr not in /etc
Patch107:       hplip-udev-rules-in-usr.patch
# Patch108 add_missing_includes_and_define_GNU_SOURCE.patch adds missing '#include <...>'
# and missing '#define _GNU_SOURCE' see https://bugs.launchpad.net/hplip/+bug/1456590
Patch108:       add_missing_includes_and_define_GNU_SOURCE.patch
Patch110:       hpijs-avoid-segfault-in-DJGenericVIP-DJGenericVIP.patch
Patch112:       ui5-systemtray-wait-only-10s-for-system-tray.patch
# Python3 port: cleanup patches
Patch300:       pcardext-python3-fixes.patch
Patch301:       hplip-misc-missing-includes-and-definitions.patch
Patch302:       hp_ipp.h-add-missing-prototypes.patch
# bsc#1159240, lp#1859179
Patch304:       hp-sendfax-avoid-crash-if-python-reportlab-is-missin.patch
# bsc#1166623, hp-toolbox crashes without python3-distro module
Patch305:       Use-lsb_release-fallback-code-if-import-distro-fails.patch
# bsc#1180724
Patch306:       dcheck.py-fix-crash-in-Qt4-version-check.patch
# PATCH-FIX-SUSE: Remove references to the closed-source ImageProcessor
Patch400:       hplip-remove-imageprocessor.diff
# Let a function return NULL instead of nothing
Patch401:       hplip-orblite-return-null.diff
# Use a pgp server (pool.sks-keyservers.net) which doesn't throw proxy errors
# or run into timeouts most of the time
Patch402:       hplip-change-pgp-server.patch
# boo#1107711
Patch403:       Revert-changes-from-3.18.5-that-break-hp-setup-for-f.patch
# PATCH-FIX-UPSTREAM: https://bugs.launchpad.net/hplip/+bug/1879445
Patch404:       hplip-3.20.6-python-includes.patch
Patch500:       hplip-missing-drivers.patch
BuildRequires:  %{pymod devel}
BuildRequires:  %{pymod qt5-devel}
BuildRequires:  %{pymod xml}
BuildRequires:  cups > 1.5
BuildRequires:  cups-devel > 1.5
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libavahi-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  readline-devel
BuildRequires:  sane-backends-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
#!BuildIgnore:  clang8
#!BuildIgnore:  libclang8
# Break this dependency chain that has caused build breakage
# python3-qt5-devel -> libqt5-qttools-devel -> libqt5-qttools-doc -> clang8
#!BuildIgnore:  libqt5-qttools-devel
#!BuildIgnore:  libqt5-qtwebengine
# Break this dependency chain that has caused build breakage
# python3-qt5-devel -> libqt5-qtwebengine-devel -> libavcodec58 -> libdav1d.so.1
#!BuildIgnore:  libqt5-qtwebengine-devel
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed.
# The exact matching version-release of the sub-package is available on the same
# repository where the main-package is (compare the "Recommends: hplip" entry below).
Requires:       %{name}-hpijs = %{version}-%{release}
# Require the exact matching version-release of the sane sub-package to make sure
# to have the exact matching version of libsane-hpaio installed:
Requires:       %{name}-sane = %{version}-%{release}
Requires:       %{pymod dbus-python} >= 0.80
Requires:       %{pymod gobject}
Requires:       %{pymod qt5}
Requires:       cups > 1.5
# foomatic-filters and cups-filters-foomatic-rip
# do not require Ghostscript because depending on the PPD
# (e.g. some PPDs for PostScript printers in OpenPrintingPPDs-postscript)
# foomatic-rip can also be used without Ghostscript but for the drivers
# HPIJS and HPCUPS Ghostscript is needed.
# The RPM requirement for ghostscript should actually be in the
# hplip-hpijs sub-package but this would bloat a minimalist system
# (see the comment for the hplip-hpijs sub-package below).
# Therefore the hplip main package which is intended
# to get "all the HPLIP stuff" installed has the RPM requirement:
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451)
# plus a leftover in CVE-2004-0801 (bnc#59233)
# foomatic-rip-hplip is no longer installed and foomatic-rip
# from foomatic-filters or cups-filters-foomatic-rip is used instead.
# The RPM requirement for foomatic-filters should actually be
# in the hplip-hpijs sub-package but this would bloat a minimalist system
# (see the comment for the hplip-hpijs sub-package below).
# Therefore the hplip main package which is intended
# to get "all the HPLIP stuff" installed has the RPM requirement:
Requires:       foomatic-filters
Requires:       ghostscript
# hp-plugin requries lsb_release
Requires:       lsb-release
Requires(post): %{_bindir}/find
Requires(post): /bin/grep
Requires(post): /bin/sed
Requires(post): coreutils
Recommends:     python3-reportlab
# Obsolete earlier package names
Obsoletes:      hplip17
Provides:       hplip3 = 3.9.5
Obsoletes:      hplip3 < 3.9.5
# cups-rpm-helper is now pulled in indirectly via cups-devel.
# This causes the "postscriptdriver" provides to be generated.
# To avoid that, put "Ignore: cups-devel: cups-rpm-helper in the prjconf.

%description
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
a unified single and multifunction connectivity solution for HP
printers, scanners, and all-in-one devices.

This package contains command line and UI front-ends for HPLIP, and tools
for extra functionality such as status and supply information. It is
not required for basic printing and scanning with HP hardware, except
for those devices that need the proprietary hplip plugin, see
https://developers.hp.com/hp-linux-imaging-and-printing/binary_plugin.html

%package hpijs
Summary:        Printer drivers for HP printers and all-in-one devices
# On a minimalist system only hplip-hpijs may be installed
# or on a minimalist package repository (e.g. on the openSUSE CDs)
# only hplip-hpijs may be available (even when a usual system is installed).
# When only hplip-hpijs is there, it should tell the dependency resolver
# that for usual functionality, hplip should be installed too (if possible).
# Unfortunately the installer ignores suggested packages silently
# but on the other hand I cannot use "Recommends hplip" here
# because the installer installs recommended packages silently
# which would bloat a minimal selection (when hplip is available to be installed)
# because the minimal selection contains hplip-hpijs which recommends hplip
# so that the installer installs hplip and all what this requires silently
# see https://bugzilla.novell.com/show_bug.cgi?id=546893
# Require only the matching version of the hplip main-package
# (compare the "Requires: hplip-hpijs" entry above) but do not depend
# on the exact matching release because the exact matching release
# may be not available to be installed (e.g. when hplip-hpijs-1.2.3-4.5 is
# installed from the openSUSE CDs but on our official online repository
# only hplip-1.2.3-6.7 is available which should usually also work):
Group:          Hardware/Printing
Requires:       %{name}-udev-rules = %{version}-%{release}
Suggests:       %{name} = %{version}
# Since Nov 14 2007 ghostscript-library does no longer require /usr/bin/hpijs
# but only "Suggests hplip-hpijs" (see Novell/Suse Bugzilla bnc#341564).
# Have the matching "reverse suggests" = "Enhances" here
# to document the ghostscript <-> hplip-hpijs relationship:
Enhances:       ghostscript
# hpijs-standalone was a stand-alone minimalist package
# which is no longer provided since a long time.
# hplip-hpijs and hpijs-standalone both contain /usr/bin/hpijs
# so that both packages have a RPM conflict which should
# be solved by a silent replacement of the old hpijs-standalone.
# This Obsoletes is intentionally unversioned because
# hplip-hpijs should replace any version of hpijs-standalone.
Obsoletes:      hpijs-standalone
# Either the hplip17 packages or the hplip packages can be installed,
# see https://bugzilla.novell.com/show_bug.cgi?id=251830#c20
# for the full story why there is this unversioned Obsoletes:
Obsoletes:      hplip17-hpijs
# Obsolete the hplip3 copy that was introduced for older SLED11-GA HP preloads:
Provides:       hplip3-hpijs = 3.9.5
Obsoletes:      hplip3-hpijs < 3.9.5
# PackMan provides HPLIP in the packages hplip and hplip-hpcups.
# HPLIP does not work if the openSUSE packages hplip and hplip-hpijs
# are installed together with a leftover PackMan package hplip-hpcups
# see https://bugzilla.novell.com/show_bug.cgi?id=515005#c17
# This Obsoletes is intentionally unversioned because
# the openSUSE package hplip-hpijs must replace
# any version of PackMan's hplip-hpcups package.
Obsoletes:      hplip-hpcups

%description hpijs
This package contains the backend drivers and PPDs for printing
with HP printers using CUPS.

HPCUPS is HPLIP's native CUPS printer driver for HP printers.
HPIJS (deprecated) is HPLIP's Ghostscript printer driver for
HP printers, and only used for some Fax devices nowadays.

Install the "hplip" package if you need the proprietary HP plugin
required by some devices, or additional functionality besides plain
printing.

%package sane
Summary:        SANE backends for HP scanners and all-in-one devices
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed.
# A wrong library version may let libsane-hpaio crash (e.g. segfault)
# which lets the whole scanning stack frontend<->libsane-dll<->libsane-backend crash
# also for any other backend when the hpaio backend is enabled (e.g. "scanimage -L"):
Group:          Hardware/Scanner
Requires:       %{name}-hpijs = %{version}-%{release}
Requires:       %{name}-udev-rules = %{version}-%{release}
# See comment in hpijs sub-package for same Suggests:
Suggests:       %{name} = %{version}
Enhances:       sane-backends
# Automatically install this package if hpijs sub-package and sane-backends are
# both installed:
Supplements:    (%{name}-hpijs and sane-backends)

%description sane
This package includes the backend driver for scanning with HP scanners
and all-in-one devices using SANE tools like xsane or scanimage.

%package scan-utils
Summary:        HPLIP scanning frontends hp-scan and hp-uiscan
# SLE does not provide python-pillow (PIL) (bsc#1131613)
Group:          Hardware/Scanner
Requires:       %{pymod Pillow}
# hp-scan et al. import skimage from the scikit-image package.
# It is pretty heavy-weight and pulls in various other packages.
Requires:       %{pymod scikit-image}
Requires:       hplip
Enhances:       hplip
# "hplip-scan" has been replaced by hplip-scan-utils
Provides:       %{name}-scan = %{version}-%{release}
Obsoletes:      %{name}-scan < %{version}-%{release}

%description scan-utils
This package provides the "hp-scan" and "hp-uiscan" frontend utilities. These
utilities are alternatives to the SANE frontends "xsane" and "scanimage". They
expose some advanced features of certain HP scanner models.

%package udev-rules
Summary:        HPLIP udev rules
Group:          Hardware/Scanner

%description udev-rules
This package provides the udev rules required to use these devices as a normal user.

%package devel
Summary:        Development files for hplip
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed:
Group:          Development/Languages/C and C++
Requires:       %{name}-hpijs = %{version}-%{release}
# Require the exact matching version-release of the sane sub-package to make sure
# to have the exact matching version of libsane-hpaio installed:
Requires:       %{name}-sane = %{version}-%{release}
Requires:       cups-devel
Requires:       dbus-1-devel
Requires:       libopenssl-devel
Requires:       libusb-1_0-devel
Requires:       net-snmp-devel

%description devel
This sub-package is only required by developers.

%prep
# Be quiet when unpacking:
%setup -q
# Patch101 change-udev-rules.diff changes the udev rules file 56-hpmud.rules
%patch -P 101 -p1 -b .change-udev-rules.orig
# Patch106 disable_hp-upgrade.patch disables hp-upgrade/upgrade.py for security reasons,
# see https://bugzilla.novell.com/show_bug.cgi?id=853405
# To upgrade HPLIP an openSUSE software package manager like YaST or zypper should be used.
%patch -P 106 -p1 -b .disable_hp-upgrade.orig
%patch -P 107 -p1 -b .udev_rules_dir.orig
# Patch108 add_missing_includes_and_define_GNU_SOURCE.patch adds missing '#include <...>'
# and missing '#define _GNU_SOURCE' see https://bugs.launchpad.net/hplip/+bug/1456590
%patch -P 108 -p1 -b .add_missing_includes_and_define_GNU_SOURCE.orig
%patch -P 110 -p1 -b .boo1094141
%patch -P 112 -p1
%patch -P 300 -p1 -b .pcardext-python3
%patch -P 301 -p1 -b .misc-headers
%patch -P 302 -p1 -b .hp_ipp_missing_prototypes
%patch -P 304 -p1
%patch -P 305 -p1
%patch -P 306 -p1
%patch -P 400 -p1
%patch -P 401 -p1
%patch -P 402 -p1
%patch -P 403 -p1
%patch -P 404 -p1
%patch -P 500 -p1
# replace "env" shebang and "/usr/bin/python" with real executable
find . -name '*.py' -o -name pstotiff | \
    xargs -n 1 sed -i '1s,^#!\(%{_bindir}/env python\|%{_bindir}/python\),#!%{pyexe},'
sed -i 's,%{_bindir}/python\>,%{pyexe},'  \
    data/rules/*

# remove shebang line and replace icon not available on openSUSE
sed -i -e '/#!.*xdg-open$/d' \
  -e 's|%{_datadir}/icons/Humanity/devices/48/printer.svg|printer|' hp-uiscan.desktop.in

cp -p %{SOURCE103} %{SOURCE104} ppd/hpcups

%build
# If AUTOMAKE='automake --foreign' is not set, autoreconf (in fact automake)
# complains about missing files like NEWS, README, AUTHORS, ChangeLog
# in each directory where a Makefile.am exists:
AUTOMAKE='automake --foreign' autoreconf -fvi
# Fix improper method of Python.h lookup in configure, no longer working with Python 3.8
PYTHON_INCLUDEDIR="$(python3-config --includes)"
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} ${PYTHON_INCLUDEDIR} -Wno-error=return-type"
export CXXFLAGS="%{optflags} ${PYTHON_INCLUDEDIR} -fno-strict-aliasing -Wno-error=return-type"
# --disable-pp-build disables parallel port build because parallel port support is deprecated by upstream HPLIP
# and by upstream in general cf. "Parallel port printers" at https://en.opensuse.org/SDB:Installing_a_Printer
# Since version 3.9.6 the default printer driver install changed from hpijs to hpcups.
# According to http://hplipopensource.com/hplip-web/release_notes.html
# all drv installs require CUPSDDK 1.2.3 or higher.
# Otherwise a static PPD install must be performed.
# Furthermore dynamic PPDs will be deprecated in the future in CUPS,
# see http://www.cups.org/str.php?L3772
# For hpcups static PPD install one needs:
# --enable-hpcups-install enable hpcups install (default=yes)
# --disable-cups-drv-install enable cups dynamic ppd install (default=yes)
# --enable-cups-ppd-install enable cups static ppd install (default=no)
# For both hpcups and hpijs install with static PPDs one needs additionally:
# --enable-hpijs-install enable hpijs install (default=no)
# --disable-foomatic-drv-install enable foomatic dynamic ppd install (default=no), uses drvdir and hpppddir
# --enable-foomatic-ppd-install enable foomatic static ppd install (default=no), uses hpppddir
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451) plus a leftover in CVE-2004-0801 (bnc#59233)
# which are fixed up to openSUSE 11.4 with patches, after openSUSE 11.4 (i.e. since openSUSE 12.1)
# foomatic-rip-hplip is no longer installed and foomatic-rip from
# foomatic-filters or cups-filters-foomatic-rip is used instead so that
# --disable-foomatic-rip-hplip-install is explicitly set and as a consequence the "cupsFilter" entries
# in the static PPDs are changed in the install section to use foomatic-rip.
# Since HPLIP 3.13.10 --with-htmldir is new but it does not inhertit its value from --with-docdir
# so that --with-htmldir must be explicitly set.
%configure \
            --disable-qt3 \
            --disable-qt4 \
            --enable-qt5 \
            --disable-policykit \
            --enable-doc-build \
            --enable-network-build \
            --disable-pp-build \
            --enable-scan-build \
            --enable-gui-build \
            --enable-fax-build \
            --enable-dbus-build \
            --enable-hpcups-install \
            --disable-cups-drv-install \
            --enable-cups-ppd-install \
            --enable-hpijs-install \
            --disable-foomatic-drv-install \
            --disable-imageProcessor-build \
            --enable-foomatic-ppd-install \
            --disable-foomatic-rip-hplip-install \
            --with-hpppddir=%{_datadir}/cups/model/manufacturer-PPDs/%{name} \
            --with-cupsbackenddir=%{_prefix}/lib/cups/backend \
            --with-cupsfilterdir=%{_prefix}/lib/cups/filter \
            --with-drvdir=%{_prefix}/lib/cups/driver \
            --with-mimedir=%{_sysconfdir}/cups \
            --with-docdir=%{_defaultdocdir}/%{name} \
            --with-htmldir=%{_defaultdocdir}/%{name} \
	    PYTHON=%{pyexe}
%make_build
sed -i 's|ppd/hpcups/\*.ppd.gz ||g' Makefile

%install
%make_install

# Make and install Python compiled bytecode files
%py3_compile %{buildroot}%{_datadir}/hplip
%py3_compile -O %{buildroot}%{_datadir}/hplip

# Hardlink .pyc and .pyo when they have same content.
# Do not run "fdupes buildroot/_datadir/hplip" because
# fdupes will link any files with same content there
# which can have unexpected side-effects, compare
# https://bugzilla.opensuse.org/show_bug.cgi?id=784670
for pyc in $( find %{buildroot}%{_datadir}/hplip -name '*.pyc' )
do
   pyo="${pyc%.pyc}.opt-1.pyc"
   if test -f $pyo && cmp -s $pyc $pyo
   then echo hardlinking $pyc and $pyo because both have same content
        ln -f $pyc $pyo
   fi
done
# HPLIP's "make install" installs -rw-r--r-- usr/share/hplip/fax/pstotiff
# and usr/lib/cups/filter/pstotiff -> usr/share/hplip/fax/pstotiff
# so that when the CUPS filter usr/lib/cups/filter/pstotiff is called,
# it cannot execute usr/share/hplip/fax/pstotiff which is fixed hereby
# (see https://bugs.launchpad.net/hplip/+bug/1064247 and bnc#783810):
chmod a+x %{buildroot}%{_datadir}/hplip/fax/pstotiff
# The /var/lib/hp directory is created everywhere except on openSUSE 12.2 and later versions
# (perhaps an autoconf issue) so that it is created here as simple and fail-safe workaround
# see https://bugs.launchpad.net/bugs/1018303 and bnc#780413
# using fixed "/var/log/hp" because this is hardcoded in the HPLIP sources
# regarding owner and permissions see the "files hpijs" section below
# and Patch102 no-chgrp_lp_hplip_Logdir.diff:
test -d %{buildroot}%{_localstatedir}/lib/hp || install -d %{buildroot}%{_localstatedir}/lib/hp
# Create a /var/log/hp/tmp/ directory that is needed by hp-sendfax
# as a workaround until HPLIP upstream implemented it correctly
# see https://bugzilla.novell.com/show_bug.cgi?id=800312
# and https://bugs.launchpad.net/bugs/1016507
install -d %{buildroot}%{_localstatedir}/log/hp/tmp
# Remove the installed /etc/sane.d/dll.conf
# because this is provided by the sane-backends package:
rm %{buildroot}%{_sysconfdir}/sane.d/dll.conf
mkdir %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio >%{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio
# Remove the installed HAL fdi file because HAL is no longer used (HAL is deprecated):
rm %{buildroot}%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
# Remove the installed hplip-printer@.service file for systemd
# because it would run hp-config_usb_printer - a tool to automatically
# set up HP USB printers and if needed automatically download and install
# non-free proprietary plugin software from HP which should not happen
# and it can cause whatever kind of strange behaviour
# see for example https://bugs.launchpad.net/bugs/1197416
# while in contrast manual printer setup via hp-setup usually "just works"
# and it is clear for the user what goes on and in case of failure what went wrong.
rm %{buildroot}%{_unitdir}/hplip-printer@.service
# Remove selinux configurations we are not supporting on SUSE
# force for not on all distributions the files were installed
# Can't be disabled during configure
rm -f %{buildroot}/%{name}.{fc,if,pp,te}
# Begin "General tests and adjustments for all PPDs" (see manufacturer-PPDs.spec):
pushd %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}
# Do not pollute the build log file with zillions of meaningless messages:
set +x
gunzip *.ppd.gz
# Make some general tests and adjustments for all PPDs:
echo "Making some general tests and adjustments for all PPDs:"
# Add a line-feed to the end of all PPDs to fix those PPDs where it is missing.
# See Novell/Suse Bugzilla bug #309832: Unix/Linux text files must end with a line-feed.
# Otherwise reading the last line results EOF and then some programs may ignore the last line.
echo "Adding a line-feed to the end of all PPDs to fix those PPDs where it is missing..."
for p in *.ppd
do echo -en '\n' >>$p
done
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451) plus a leftover in CVE-2004-0801 (bnc#59233)
# foomatic-rip-hplip is no longer installed and foomatic-rip from foomatic-filters or cups-filters-foomatic-rip
# is used instead so that the "cupsFilter" entries in the static PPDs must be changed accordingly:
echo "Replacing insecure foomatic-rip-hplip with foomatic-rip everywhere in in the PPDs..."
for p in *.ppd
do sed -i -e 's/foomatic-rip-hplip/foomatic-rip/' $p
done
# Final test by cupstestppd:
# To save disk space gzip the files (gzipped PPDs can also be used by CUPS).
# Future goal: Only have files which don't FAIL for cupstestppd.
# Ignore FAILs because of errors in UIConstraints and/or NonUIConstraints
# which are detected since cupstestppd in CUPS > 1.2.7 (i.e. in openSUSE 10.3).
# See Novell/Suse Bugzilla bug #309822: When this bug is fixed, cupstestppd would
# no longer result zero exit code.
# In the long run the PPDs should be fixed but as far as we know there have been
# no problems because of such UIConstraints errors so that it should be o.k.
# let those PPDs pass even if they are not strictly compliant.
# Ignore FAILs because of missing cupsFilter programs because
# in the package build environment the usual HPLIP filters
# like "hpcups" and "hpcupsfax" are
# installed at an unusual place (in the BuildRoot directory).
# For now keep all PPDs even if cupstestppd FAILs.
# Reason:
# With each CUPS version upgrade cupstestppd finds more and more errors
# so that more and more PPDs would be no longer included in the RPM
# which have been included before which results a regression.
# As far as we know there have been no problems at all because of
# not strictly compliant PPDs in HPLIP so that it is much better
# to provide all HPLIP PPDs so that the matching printers can be used
# than to be rigorous regarding enforcing compliance to the PPD specification:
echo "Final testing by cupstestppd..."
for p in *.ppd
do grep -E -v '^\*UIConstraints:|^\*NonUIConstraints:|^\*cupsFilter:' $p | cupstestppd - || true
   gzip -n -9 $p
done
echo "Moving PPDs that use the hpps filter to %{_datadir}/cups/model/manufacturer-PPDs/hplip-hpps..."
# PPDs for various printers that use the hpps filter
# must be moved to the hplip main-package because
# the /usr/lib/cups/filter/hpps Python script imports
# various HPLIP modules from the hplip main-package
# so that the hpps filter belongs to the hplip main-package
# (see https://bugzilla.novell.com/show_bug.cgi?id=876690).
# Accordingly the PPDs that use the hpps filter must be moved
# to the hplip main-package which is implemented by moving them
# to a new directory /usr/share/cups/model/manufacturer-PPDs/hplip-hpps
# that is listed in the files list of the hplip main-package:
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpps
for p in *.ppd.gz
do zgrep -q '^\*cupsFilter:.*hpps' $p && mv $p ../%{name}-hpps
done
echo "Moving PPDs that require a proprietary plugin from HP to %{_datadir}/cups/model/manufacturer-PPDs/hplip-plugin..."
# PPDs for various printers that require a proprietary plugin from HP
# must be moved to the hplip main-package because
# the proprietary plugin from HP must be downloaded and installed
# by using HP's "hp-plugin" tool from the hplip main-package
# (HP's "hp-setup" tool calls "hp-plugin" when needed).
# Accordingly PPDs that require a proprietary plugin from HP must be moved
# to the hplip main-package which is implemented by moving them
# to a new directory /usr/share/cups/model/manufacturer-PPDs/hplip-plugin
# that is listed in the files list of the hplip main-package
# (see https://bugzilla.novell.com/show_bug.cgi?id=876690):
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-plugin
for p in *.ppd.gz
do zgrep -q '^\*NickName:.*requires proprietary plugin' $p && mv $p ../%{name}-plugin
done
echo "End of general tests and adjustments for all PPDs."
# Switch back to the usual build log messages:
set -x
# End of "General tests and adjustments for all PPDs":
popd
# Replace the invalid Desktop categories
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/hplip.desktop System HardwareSettings
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/hp-uiscan.desktop System HardwareSettings

# Let suse_update_desktop_file add X-SuSE-translate key to /etc/xdg/autostart/hplip-systray.desktop
# so that we can update its translations with translation-only packages.
%suse_update_desktop_file -i %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop
# End of "Desktop menue entry stuff".
# Install the man page for /usr/bin/hpijs:
install -d %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE102} %{buildroot}%{_mandir}/man1/

# remove libtool archives
find "%{buildroot}" -type f -name "*.la" -delete -print

# Run fdupes:
# The RPM macro fdupes runs /usr/bin/fdupes that links files with identical content.
# Never run fdupes carelessly over the whole buildroot directory
# because in older openSUSE and SLE11 versions fdupes
# links files with different owner, group, or permissions
# see https://bugzilla.novell.com/show_bug.cgi?id=784670
# and even in current openSUSE versions fdupes links across sub-package boundaries,
# compare https://bugzilla.novell.com/show_bug.cgi?id=784869
# so that fdupes can only run for specific directories where linking files is safe:
%fdupes -s %{buildroot}%{_datadir}/hplip/data/images

%post -p /bin/bash
%udev_rules_update
%desktop_database_post
%icon_theme_cache_post
/sbin/ldconfig
exit 0

%postun -p /bin/bash
%desktop_database_postun
%icon_theme_cache_postun
/sbin/ldconfig

%postun sane
# Earlier versions of hplip modified /etc/sane.d/dll.conf
# Now we use /etc/sane.d/dll.d (multiple hpaio entries don't hurt).
# If the package was removed (but not if it was updated)
# then remove the hpaio lines in /etc/sane.d/dll.conf.
if [ "$1" = "0" ] && [ -w %{_sysconfdir}/sane.d/dll.conf ]; then
    sed -i -e '/hpaio/d' %{_sysconfdir}/sane.d/dll.conf
fi
exit 0

%post hpijs -p /bin/bash
/sbin/ldconfig
exit 0

%postun hpijs -p /bin/bash
/sbin/ldconfig
exit 0

%files
%config %{_sysconfdir}/xdg/autostart/hplip-systray.desktop
%{_bindir}/hp-align
%{_bindir}/hp-check
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-devicesettings
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-doctor
%{_bindir}/hp-fab
%{_bindir}/hp-faxsetup
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-logcapture
%{_bindir}/hp-makecopies
%{_bindir}/hp-makeuri
%{_bindir}/hp-pkservice
%{_bindir}/hp-plugin
%{_bindir}/hp-pqdiag
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-probe
%{_bindir}/hp-query
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-systray
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-toolbox
%{_bindir}/hp-uninstall
%{_bindir}/hp-unload
%{_bindir}/hp-upgrade
%{_bindir}/hp-wificonfig
%{_libdir}/python%{pyver}/site-packages/cupsext.*
%{_libdir}/python%{pyver}/site-packages/hpmudext.*
%{_libdir}/python%{pyver}/site-packages/pcardext.*
%dir %{_prefix}/lib/cups
%dir %{_prefix}/lib/cups/backend
%{_prefix}/lib/cups/backend/hpfax
%dir %{_prefix}/lib/cups/filter
%{_prefix}/lib/cups/filter/hpps
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/manufacturer-PPDs
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpps/
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-plugin/
%doc %{_defaultdocdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/hplip/
%exclude %{_datadir}/hplip/data/models/models.dat
%exclude %{_datadir}/hplip/base/imageprocessing.py*
%exclude %{_datadir}/hplip/ui5/scandialog.py*
%exclude %{_datadir}/hplip/scan
%exclude %{_datadir}/hplip/scan.py*
%exclude %{_datadir}/hplip/uiscan.py*
%exclude %{_datadir}/hplip/__pycache__/uiscan.*
%exclude %{_datadir}/hplip/__pycache__/scan.*
%exclude %{_datadir}/hplip/base/__pycache__/imageprocessing.*
%exclude %{_datadir}/hplip/ui5/__pycache__/scandialog.*

# The scanning utils depend on PIL and python3-scikit-image,
# which are not available in SLE
%files scan-utils
%{_datadir}/applications/hp-uiscan.desktop
%{_libdir}/python%{pyver}/site-packages/scanext.*
%{_bindir}/hp-scan
%{_bindir}/hp-uiscan
%{_datadir}/hplip/scan
%{_datadir}/hplip/scan.py*
%{_datadir}/hplip/uiscan.py*
%{_datadir}/hplip/base/imageprocessing.py*
%{_datadir}/hplip/ui5/scandialog.py*
%{_datadir}/hplip/__pycache__/uiscan.*
%{_datadir}/hplip/__pycache__/scan.*
%{_datadir}/hplip/base/__pycache__/imageprocessing.*
%{_datadir}/hplip/ui5/__pycache__/scandialog.*

%files hpijs
%config %{_sysconfdir}/hp/
%config %{_sysconfdir}/cups/pstotiff.convs
%config %{_sysconfdir}/cups/pstotiff.types
%{_bindir}/hpijs
%{_mandir}/man1/hpijs.1%{?ext_man}
%{_libdir}/libhpip.so.*
%{_libdir}/libhpipp.so.*
%{_libdir}/libhpmud.so.*
%{_libdir}/libhpdiscovery.so.*
%dir %{_prefix}/lib/cups
%dir %{_prefix}/lib/cups/backend
%{_prefix}/lib/cups/backend/hp
%dir %{_prefix}/lib/cups/filter
%{_prefix}/lib/cups/filter/hpcups
%{_prefix}/lib/cups/filter/hpcupsfax
%{_prefix}/lib/cups/filter/hpcdmfax
%{_prefix}/lib/cups/filter/pstotiff
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/manufacturer-PPDs
%{_datadir}/cups/model/manufacturer-PPDs/%{name}/
%{_datadir}/%{name}/data/models/models.dat
# Use fixed "/var/log/hp" because this is hardcoded in the HPLIP sources.
# Regarding attr(0775,root,lp) see the comment for /var/log/hp/tmp below:
%dir %attr(0775,root,lp) %{_localstatedir}/log/hp
# Regarding attr(0775,root,lp) for /var/log/hp/tmp
# see https://bugzilla.novell.com/show_bug.cgi?id=800312#c0
# i.e. it is reasonable secure and hp-sendfax works with it:
%dir %attr(0775,root,lp) %{_localstatedir}/log/hp/tmp
# Use fixed "/var/lib/hp" because this is hardcoded in the HPLIP sources:
%dir %{_localstatedir}/lib/hp

%files sane
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-hpaio.so.*
%dir %{_sysconfdir}/sane.d
%dir %{_sysconfdir}/sane.d/dll.d
%{_sysconfdir}/sane.d/dll.d/hpaio

%files udev-rules
%{_udevrulesdir}/56-hpmud.rules

%files devel
%{_libdir}/libhpip.so
%{_libdir}/libhpipp.so
%{_libdir}/libhpmud.so
%{_libdir}/libhpdiscovery.so
%{_libdir}/sane/libsane-hpaio.so

%changelog
