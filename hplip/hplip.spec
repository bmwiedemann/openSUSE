#
# spec file for package hplip
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{suse_version} >= 1500
%define pyversion 3
%define pymod() python3-%{**}
%define pyver %py3_ver
%define pyexe /usr/bin/python3
%define gobject gobject
%else
%define pyversion 2
%define pymod() python-%{**}
%define pyver %py_ver
%define pyexe /usr/bin/python
%define gobject gobject2
%endif

%if 0%{?suse_version} == 1315 && 0%{?is_opensuse}
%define is_leap 1
%else
%define is_leap 0
%endif
# For udev macros
%if 0%{?suse_version} > 1130
BuildRequires:  systemd-rpm-macros
%else
# For older suse_version (in particular for SLE11) define needed udev macros manually:
%{!?_udevrulesdir: %global _udevrulesdir %{_prefix}/lib/udev/rules.d }
%endif
%if 0%{?suse_version} == 1110
# For SLE11 redefine _libexecdir because on SLE11 _libexecdir is "/usr/lib64":
%global _libexecdir %{_prefix}/lib
%endif
# Use Qt5 frontend on TW, Leap >= 42.2 and SLE >= 15
%if 0%{?suse_version} > 1320 || (0%{?sle_version} >= 120200 && 0%{?is_opensuse})
%global use_qt5 1
%else
%global use_qt5 0
%endif

Name:           hplip
Version:        3.19.3
Release:        0
Summary:        HP's Printing, Scanning, and Faxing Software
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Hardware/Printing
Url:            https://developers.hp.com/hp-linux-imaging-and-printing
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
# PATCH-FIX-SUSE: GNOME no longer provides a system tray, so don't warn the user that we can't find it
Patch109:       no-systray-failure-message.patch
Patch110:       hpijs-avoid-segfault-in-DJGenericVIP-DJGenericVIP.patch
Patch112:       ui5-systemtray-wait-only-10s-for-system-tray.patch
# Python3 port: cleanup patches
Patch300:       pcardext-python3-fixes.patch
Patch301:       hplip-misc-missing-includes-and-definitions.patch
Patch302:       hp_ipp.h-add-missing-prototypes.patch
# Fix import error for pcardext
Patch303:       photocard-fix-import-error-for-pcardext.patch
# PATCH-FIX-SUSE: Remove references to the closed-source ImageProcessor
Patch400:       hplip-remove-imageprocessor.diff
# Let a function return NULL instead of nothing
Patch401:       hplip-orblite-return-null.diff

BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libdrm-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
# BuildRequires:  python-rpm-macros
# All printer driver packages should have "BuildRequires: python-cups"
# because python-cups installs special rpm macros that adds Provides tags
# for the printer drivers supported by the package,
# see https://bugzilla.novell.com/show_bug.cgi?id=735865
BuildRequires:  %{pymod cups}
BuildRequires:  %{pymod devel}
%if %use_qt5
BuildRequires:  %{pymod qt5-devel}
%else
BuildRequires:  %{pymod qt4}
BuildRequires:  libqt4-devel
%endif
BuildRequires:  %{pymod xml}
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed.
# The exact matching version-release of the sub-package is available on the same
# repository where the main-package is (compare the "Recommends: hplip" entry below).
Requires:       %{name}-hpijs = %{version}-%{release}
# Require the exact matching version-release of the sane sub-package to make sure
# to have the exact matching version of libsane-hpaio installed:
Requires:       %{name}-sane = %{version}-%{release}
# Since version 2.8.4 all interprocess communication uses dbus.
# Therefore python-dbus version 0.80 or greater is required (which pulls in dbus base stuff).
# The dbus stuff in HPLIP requires the Python module gobject
# but there is no automated RPM requirement for python-gobject2,
# see https://answers.launchpad.net/hplip/+question/30741
%if 0%{pyversion} == 3
Requires:       dbus-1-python3 >= 0.80
%else
Requires:       dbus-1-python >= 0.80
%endif
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
Requires:       %{pymod %gobject}

# SLE does not provide python-pillow (PIL) (bsc#1131613)
%if 0%{?is_opensuse}
Requires:       %{pymod Pillow}
%endif
Requires:       ghostscript

%if %use_qt5
Requires:       %{pymod qt5}
%else
Requires:       %{pymod qt4}
%endif
# Require special Python stuff (which pulls in Python base stuff).
# At least since openSUSE 11.1 and SLE11 pyxml is no longer required
# (pyxml was required in particular for openSUSE 10.3 and SLE10,
#  see https://answers.launchpad.net/hplip/+question/25696)
# but meanwhile python-xml alone is sufficient for "import xml.parsers.expat"
# see https://bugzilla.novell.com/show_bug.cgi?id=656779#c3
Requires:       %{pymod xml}
Requires(post): %{_bindir}/find
Requires(post): /bin/grep
Requires(post): /bin/sed
Requires(post): coreutils
# Either the hplip17 packages or the hplip packages can be installed,
# see https://bugzilla.novell.com/show_bug.cgi?id=251830#c20
# for the full story why there is this unversioned Obsoletes:
Obsoletes:      hplip17
# Obsolete the hplip3 copy that was introduced for older SLED11-GA HP preloads:
Provides:       hplip3 = 3.9.5
Obsoletes:      hplip3 < 3.9.5
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# HPLIP's Python module cupsext.so has a build-time dependancy on the CUPS version:
# It needs symbols (like ippFirstAttribute, ippNextAttribute, ippSetOperation etc)
# that are defined only in libcups.so version > 1.5. For backward compatibility
# cupsext.c has a macro (CUPS_VERSION_1_6) which defines those undefined function names
# if CUPS version is <= 1.5. To check the CUPS version the CUPS_VERSION_MAJOR, CUPS_VERSION_MINOR
# macros from cups/cups.h are used which means it depends on the CUPS version during build-time
# whether or not cupsext will work with CUPS <= 1.5 at run-time.
# See https://bugs.launchpad.net/hplip/+bug/1423220
# and https://bugzilla.opensuse.org/show_bug.cgi?id=918387
# Therefore it BuildRequires the CUPS version as provided in the openSUSE/SLE versions.
# Up to openSUSE 13.2 and SLE11 CUPS < 1.6 is provided (from CUPS 1.3.9 for SLE11 up to CUPS 1.5.4 for openSUSE 13.2).
# For SLE12 by default CUPS 1.7.5 is provided and alternatively CUPS 1.5.4 is provided in the "legacy" module.
# After openSUSE 13.2 (i.e. for current openSUSE Factory) CUPS 2.0 is provided.
# Up to openSUSE 13.2 and SLE12 it BuildRequires CUPS < 1.6 to ensure it even works on SLE12 with CUPS 1.5.4.
# When it was built with CUPS > 1.5 it must also require CUPS > 1.5 during run-time.
# In contrast when it was built with CUPS < 1.6 there must not be a run-time requirement
# for a CUPS version to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4.
# For suse_version values see https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} > 1320 || %{is_leap}
# For openSUSE after 13.2 (i.e. for current openSUSE Factory) CUPS > 1.5 is provided and required:
BuildRequires:  cups > 1.5
BuildRequires:  cups-devel > 1.5
Requires:       cups > 1.5
%endif
%if 0%{?suse_version} == 1315 && !%{is_leap}
# For SLE12 build it with traditional CUPS 1.5.4 to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4.
# Only in the Printing project for SLE12 use cups154 and cups154-devel (from the cups154-SLE12 source package):
BuildRequires:  cups154
BuildRequires:  cups154-devel
Requires:       cups
%endif
%if 0%{?suse_version} == 1320 || 0%{?suse_version} < 1315
# For openSUSE 13.2 and for openSUSE 13.1 and older openSUSE and SLE11 versions CUPS < 1.6 is provided:
BuildRequires:  cups < 1.6
BuildRequires:  cups-devel < 1.6
Requires:       cups
%endif
%if 0%{?suse_version} > 1130
BuildRequires:  sane-backends-devel
%else
BuildRequires:  sane-backends
%endif

%description
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
a unified single and multifunction connectivity solution for HP
printers and scanners (in particular, HP all-in-one devices).

HPLIP provides unified connectivity for printing, scanning, sending
faxes, photo card access, and device management and is designed to work
with CUPS.

It includes the Ghostscript printer driver HPIJS for HP printers and a
special "hp" CUPS back-end that provides bidirectional communication
with the device (required for HP printer device management).

It also includes the SANE scanner driver "hpaio" for HP all-in-one
devices. Basic PC send fax functionality is supported on a number of
devices.

The special "hpfax" CUPS back-end is required to send faxes. Direct
uploading (i.e. without print and scan) of received faxes from the
device to the PC is not supported.

The "hp-toolbox" program is provided for device management.

The "hp-sendfax" program must be used to send faxes.

The "hp-setup" program can be used to set up HP all-in-one devices.

The HPLIP project is open source software and uses GPL-compatible
licenses. For more information, see:

http://hplipopensource.com

%{_docdir}/hplip/index.html

%package hpijs
Summary:        Only plain printing with HPLIP printer drivers
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
HPIJS is HPLIP's Ghostscript printer driver for HP printers.
HPCUPS is HPLIP's native CUPS printer driver for HP printers.

This sub-package includes only what is needed for plain printing
with the printer drivers in HPLIP for standard HP printers.

It does neither provide device status information,
nor support for scanning, nor support for faxing,
nor support for memory card (mass storage) access,
nor support for non-standard devices e.g. no support
for devices which require an additional plugin from HP.

This sub-package includes in particular:

The hpijs binary and the libraries libhpip and libhpmud
which are needed to run it.

The HPCUPS driver (%{_prefix}/lib[64]/cups/filter/hpcups).

The CUPS backend "hp".

All HPLIP PPD files (also for HP PostScript printers).

For the full-featured HPLIP printing and scanning solution,
the main-package package hplip must be installed.

For full documentation and license see the main-package hplip.

%package sane
Summary:        Only plain scanning with HPLIP scan drivers
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed.
# A wrong library version may let libsane-hpaio crash (e.g. segfault)
# which lets the whole scanning stack frontend<->libsane-dll<->libsane-backend crash
# also for any other backend when the hpaio backend is enabled (e.g. "scanimage -L"):
Group:          Hardware/Scanner
Requires:       %{name}-hpijs = %{version}-%{release}
# See comment in hpijs sub-package for same Suggests:
Suggests:       %{name} = %{version}
Enhances:       sane-backends
# Automatically install this package if hpijs sub-package and sane-backends are
# both installed:
Supplements:    packageand(%{name}-hpijs:sane-backends)

%description sane
This sub-package includes only what is needed for plain scanning
with the scan drivers in HPLIP for standard HP all-in-one printers.

%package devel
Summary:        Development files for hplip
# Require the exact matching version-release of the hpijs sub-package to make sure
# to have the exact matching version of libhpip and libhpmud installed:
Group:          Development/Languages/C and C++
Requires:       %{name}-hpijs = %{version}-%{release}
# Require the exact matching version-release of the sane sub-package to make sure
# to have the exact matching version of libsane-hpaio installed:
Requires:       %{name}-sane = %{version}-%{release}

%description devel
This sub-package is only required by developers.

%prep
# Be quiet when unpacking:
%setup -q
# Patch101 change-udev-rules.diff changes the udev rules file 56-hpmud.rules
%patch101 -p1 -b .change-udev-rules.orig
# Patch106 disable_hp-upgrade.patch disables hp-upgrade/upgrade.py for security reasons,
# see https://bugzilla.novell.com/show_bug.cgi?id=853405
# To upgrade HPLIP an openSUSE software package manager like YaST or zypper should be used.
%patch106 -p1 -b .disable_hp-upgrade.orig
%patch107 -p1 -b .udev_rules_dir.orig
# Patch108 add_missing_includes_and_define_GNU_SOURCE.patch adds missing '#include <...>'
# and missing '#define _GNU_SOURCE' see https://bugs.launchpad.net/hplip/+bug/1456590
%patch108 -p1 -b .add_missing_includes_and_define_GNU_SOURCE.orig
%patch109 -p1 -b .systemtray.py.orig
%patch110 -p1 -b .boo1094141
%patch112 -p1
%patch300 -p1 -b .pcardext-python3
%patch301 -p1 -b .misc-headers
%patch302 -p1 -b .hp_ipp_missing_prototypes
%patch303 -p1 -b .photocard_import
%patch400 -p1
%patch401 -p1

# replace "env" shebang and "/usr/bin/python" with real executable
find . -name '*.py' -o -name pstotiff | \
    xargs -n 1 sed -i '1s,^#!\(/usr/bin/env python\|/usr/bin/python\),#!%{pyexe},'
sed -i 's,/usr/bin/python\>,%{pyexe},'  \
    data/rules/*

# replace icon not available on openSUSE
sed -i -e 's|/usr/share/icons/Humanity/devices/48/printer.svg|printer|' hp-uiscan.desktop.in

%build
# If AUTOMAKE='automake --foreign' is not set, autoreconf (in fact automake)
# complains about missing files like NEWS, README, AUTHORS, ChangeLog
# in each directory where a Makefile.am exists:
AUTOMAKE='automake --foreign' autoreconf -fvi
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} -Wno-error=return-type"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -Wno-error=return-type"
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
%if %use_qt5
            --disable-qt4 \
            --enable-qt5 \
%else
            --enable-qt4 \
            --disable-qt5 \
%endif
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
            --enable-foomatic-ppd-install \
            --disable-foomatic-rip-hplip-install \
            --with-hpppddir=%{_datadir}/cups/model/manufacturer-PPDs/%{name} \
            --with-cupsbackenddir=%{_libexecdir}/cups/backend \
            --with-cupsfilterdir=%{_libexecdir}/cups/filter \
            --with-drvdir=%{_libexecdir}/cups/driver \
            --with-mimedir=%{_sysconfdir}/cups \
            --with-docdir=%{_defaultdocdir}/%{name} \
            --with-htmldir==%{_defaultdocdir}/%{name} \
	    CFLAGS='%{optflags} -Wno-error=return-type' \
	    PYTHON=%{pyexe}
%make_build
sed -i 's|ppd/hpcups/\*.ppd.gz ||g' Makefile

%install
make DESTDIR=%{buildroot} install
# Make and install Python compiled bytecode files
# (.pyc compiled python and .pyo optimized compiled python)
# because normal users do not have write permissions
# to the install location /usr/share/hplip/ so that
# for normal users Python would recompile the sources every time
# which results longer program startup time and waste of CPU for compiling,
# see https://en.opensuse.org/openSUSE:Packaging_Python#Byte_Compiled_Files
# and http://lists.opensuse.org/opensuse-packaging/2014-10/msg00028.html

%if 0%{pyversion} == 3
# Make and install .pyc files:
%py3_compile %{buildroot}%{_datadir}/hplip
# Make and install .pyo files:
%py3_compile -O %{buildroot}%{_datadir}/hplip
%else
# Make and install .pyc files:
%py_compile %{buildroot}%{_datadir}/hplip
# Make and install .pyo files:
%py_compile -O %{buildroot}%{_datadir}/hplip
%endif

# Hardlink .pyc and .pyo when they have same content.
# Do not run "fdupes buildroot/_datadir/hplip" because
# fdupes will link any files with same content there
# which can have unexpected side-effects, compare
# https://bugzilla.opensuse.org/show_bug.cgi?id=784670
for pyc in $( find %{buildroot}%{_datadir}/hplip -name '*.pyc' )
do
%if 0%{pyversion} == 3
   pyo="${pyc%.pyc}.opt-1.pyc"
%else
   pyo="${pyc%.pyc}.pyo"
%endif
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
rm %{buildroot}%{_libexecdir}/systemd/system/hplip-printer@.service
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

# SLE does not provide python-pillow (PIL) (bsc#1131613)
%if !0%{?is_opensuse}
rm -f %{buildroot}/usr/share/hplip/scan.py %{buildroot}%{_bindir}/hp-scan
cat >%{buildroot}%{_bindir}/hp-scan <<EOF
#! /bin/sh
echo 'Please use "scanimage" from the "sane-backends" package instead.' >&2
exit 1
EOF
chmod a+x %{buildroot}%{_bindir}/hp-scan
%endif

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
%if 0%{?suse_version} > 1130
%udev_rules_update
%desktop_database_post
%icon_theme_cache_post
%else
gtk-update-icon-cache %{_datadir}/icons/hicolor || true
%endif
/sbin/ldconfig
exit 0

%triggerin -p /bin/bash -- sane-backends
# As hplip can be used for plain printers it cannot "PreReq sane-backends".
# Therefore if sane-backends is installed it may be installed or updated after hplip.
# In this case trigger to add the SANE backend "hpaio" to /etc/sane.d/dll.conf if it is not there.
# To be safe there is a test that /etc/sane.d/dll.conf is writable.
if [ -w %{_sysconfdir}/sane.d/dll.conf ]
then if ! grep -q 'hpaio' %{_sysconfdir}/sane.d/dll.conf
     then echo -e '# The hpaio backend is provided by the hplip package:\n#hpaio' >>%{_sysconfdir}/sane.d/dll.conf
     fi
fi
exit 0

%postun -p /bin/bash
%if 0%{?suse_version} >= 1140
%desktop_database_postun
%icon_theme_cache_postun
%else
gtk-update-icon-cache %{_datadir}/icons/hicolor || true
%endif
/sbin/ldconfig
# If the package was removed (but not if it was updated)
# then remove the hpaio lines in /etc/sane.d/dll.conf.
# Don't remove them when the hplip package was automatically
# replaced by the hplip17 package (via RPM obsoletes) or vice versa.
# Because postun of the old package runs last (after triggerin -- sane-backends)
# it is done via a special "ls" test if any libsane-hpaio.so exists
# (e.g. there could be only 32-bit installed on 64-bit hardware).
# If the "ls" test does not fail, some kind of HPLIP is installed.
# The package sane-backends may not be installed (see triggerin)
# and therefore the test that /etc/sane.d/dll.conf is writable.
# The "exit 0" is necessary, otherwise the postun script
# would exit with non-zero exit-code if the package was not removed.
if [ "$1" = "0" ]
then if ! ls %{_prefix}/lib*/sane/libsane-hpaio.so* &>/dev/null
     then [ -w %{_sysconfdir}/sane.d/dll.conf ] && sed -i -e '/hpaio/d' %{_sysconfdir}/sane.d/dll.conf
     fi
fi
exit 0

%post hpijs -p /bin/bash
/sbin/ldconfig
exit 0

%postun hpijs -p /bin/bash
/sbin/ldconfig
exit 0

%files
%defattr(-, root, root)
%config %{_sysconfdir}/xdg/autostart/hplip-systray.desktop
%if 0%{?suse_version} == 1110 || 0%{?suse_version} == 1320 || 0%{?suse_version} == 1315
%dir %{_prefix}/lib/udev
%dir %{_prefix}/lib/udev/rules.d
%endif
%{_udevrulesdir}/56-hpmud.rules
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
%{_bindir}/hp-scan
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-systray
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-toolbox
%{_bindir}/hp-uiscan
%{_bindir}/hp-uninstall
%{_bindir}/hp-unload
%{_bindir}/hp-upgrade
%{_bindir}/hp-wificonfig
%{_libdir}/python%{pyver}/site-packages/cupsext.*
%{_libdir}/python%{pyver}/site-packages/hpmudext.*
%{_libdir}/python%{pyver}/site-packages/pcardext.*
%{_libdir}/python%{pyver}/site-packages/scanext.*
%dir %{_libexecdir}/cups
%dir %{_libexecdir}/cups/backend
%{_libexecdir}/cups/backend/hpfax
%dir %{_libexecdir}/cups/filter
%{_libexecdir}/cups/filter/hpps
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/manufacturer-PPDs
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpps/
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-plugin/
%doc %{_defaultdocdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/hp-uiscan.desktop
%{_datadir}/hplip/
%exclude %{_datadir}/hplip/data/models/models.dat

%files hpijs
%defattr(-, root, root)
%config %{_sysconfdir}/hp/
%config %{_sysconfdir}/cups/pstotiff.convs
%config %{_sysconfdir}/cups/pstotiff.types
%{_bindir}/hpijs
%{_mandir}/man1/hpijs.1.gz
%{_libdir}/libhpip.so.*
%{_libdir}/libhpipp.so.*
%{_libdir}/libhpmud.so.*
%{_libdir}/libhpdiscovery.so.*
%dir %{_libexecdir}/cups
%dir %{_libexecdir}/cups/backend
%{_libexecdir}/cups/backend/hp
%dir %{_libexecdir}/cups/filter
%{_libexecdir}/cups/filter/hpcups
%{_libexecdir}/cups/filter/hpcupsfax
%{_libexecdir}/cups/filter/pstotiff
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
%defattr(-, root, root)
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-hpaio.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/libhpip.so
%{_libdir}/libhpipp.so
%{_libdir}/libhpmud.so
%{_libdir}/libhpdiscovery.so
%{_libdir}/*.la
%{_libdir}/sane/libsane-hpaio.so
%{_libdir}/sane/*.la

%changelog
