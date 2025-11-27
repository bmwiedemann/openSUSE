#
# spec file for package hplip
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global basic_tools align clean colorcal diagnose_queues doctor fab firmware info levels logcapture makecopies makeuri plugin probe query sendfax setup testpage timedate unload

# python-rpm-macros doesn't work for hplip!
%if 0%{?suse_version} >= 1500
%define pyversion 3
%define pymod() python3-%{**}
%define pyver %{py3_ver}
%define pyexe %{_bindir}/python3
%define py_compile(O) %{py3_compile %{-O} %*}
%global use_qt5 1
%define gobject gobject
%else
%define pyversion 2
%define pymod() python-%{**}
%define pyver %{py_ver}
%define pyexe %{_bindir}/python
%define gobject gobject2
%global use_qt5 0
%global make_build make V=1
%global make_install make DESTDIR=%{buildroot} V=1 install
%endif

%if 0%{?suse_version} == 1600 && 0%{?is_opensuse}
# Build without scanning support
%bcond_with scan_utils
%else
# Build scanning support
%bcond_without scan_utils
%endif

# update_desktop_files is deprecated in TW
%if 0%{?suse_version} > 1600
%bcond_with update_desktop
%else
%bcond_without update_desktop
%endif

%if 0%{use_qt5}
%global config_qt_opts --disable-qt4 --enable-qt5
%global requires_qt %{pymod qt5}
%global ui_dir ui5
%else
%global config_qt_opts --enable-qt4 --disable-qt5
%global requires_qt %{pymod qt4}
%global ui_dir ui4
%endif

%global drvdir %{_datadir}/cups/drv

Name:           hplip
Version:        3.25.6
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
# PATCH-FIX-SUSE https://bugs.launchpad.net/hplip/+bug/2115626 bsc#1245358
Patch405:       Fix-ReDoS-issue-in-HPLIP-s-SLP-parser.patch
Patch500:       hplip-missing-drivers.patch
# PATCH-FIX-UPSTREAM boo#1225777
Patch601:       hplip-pserror-c99.patch
Patch602:       hplip-scan-hpaio-include.patch
Patch603:       hplip-scan-orblite-c99.patch
Patch604:       hplip-sclpml-strcasestr.patch
Patch605:       hplip-hpaio-gcc14.patch
Patch606:       hplip-base-fix-error-in-ConfigBase-handling.patch
Patch607:       hplip-utils-Fix-plugin-verification-with-sha256.patch
# lp#2120739
Patch608:       hp-setup-fix-python-crash-when-manually-importing-gz.patch
# lp#2115046
Patch610:       hplip-no-urlopener.patch
Patch611:       hplip-fix-driver-probing-using-avahi.patch
Patch612:       hplip-fix-python-crash-in-avahi.py.patch
# PATCH-FIX-UPSTREAM https://bugs.launchpad.net/hplip/+bug/2096650
Patch651:       hplip-3.24.4-gcc15.patch
# Compatibility patches for old SUSE releases
Patch700:       hplip-base-replace-f-string-with-string.format-for-p.patch
Patch701:       hpcups-fix-compilation-on-SLE12.patch

# cups-rpm-helper is now pulled in indirectly via cups-devel.
# This causes the "postscriptdriver" provides to be generated.
# To avoid that, put "Ignore: cups-devel: cups-rpm-helper in the prjconf.
%if %use_qt5
BuildRequires:  %{pymod qt5-devel}
%else
BuildRequires:  %{pymod qt4}
BuildRequires:  libqt4-devel
%endif
BuildRequires:  %{pymod devel}
BuildRequires:  %{pymod setuptools}
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
%if %{with update_desktop}
BuildRequires:  update-desktop-files
%endif
#!BuildIgnore:  clang8
#!BuildIgnore:  libclang8
# Break this dependency chain that has caused build breakage
# python3-qt5-devel -> libqt5-qttools-devel -> libqt5-qttools-doc -> clang8
#!BuildIgnore:  libqt5-qttools-devel
#!BuildIgnore:  libqt5-qtwebengine
# Break this dependency chain that has caused build breakage
# python3-qt5-devel -> libqt5-qtwebengine-devel -> libavcodec58 -> libdav1d.so.1
#!BuildIgnore:  libqt5-qtwebengine-devel

# Require the exact matching version-release of the utils subackage.
Requires:       %{name}-utils = %{version}-%{release}
# To ensure the "hplip" package provides a similar user experience as before,
# pull in the necessary PPDs.
%if 0%{?suse_version} >= 1500
# Works with either driver-hpcus or ppds-hpcups; driver-hpcups is preferred
Requires:       (%{name}-driver-hpcups or %{name}-ppds-hpcups)
Suggests:       %{name}-driver-hpcups
%else
# On older distros, prefer ppds for historical reasons
Requires:       %{name}-ppds-hpcups
%endif
Requires:       %{name}-ppds-fax = %{version}-%{release}
Requires:       %{name}-ppds-hpps = %{version}-%{release}
Requires:       %{name}-ppds-postscript = %{version}-%{release}
# hplip3 and hplip3-hpijs existed only in SLE11 as an alternative in addition to hplip:
Obsoletes:      hplip3
Obsoletes:      hplip3-hpijs

%description
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
support for HP printers, scanners, and all-in-one devices.

This is a meta package that pulls in the entire HPLIP software suite.

%package utils
Summary:        HPLIP GUI utilities
Group:          Hardware/Printing
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{pymod dbus-python} >= 0.80
Requires:       %{pymod gobject}
Requires:       %{requires_qt}
%if 0%{?suse_version} >= 1500
Recommends:     python3-reportlab
%endif
# Make sure we obsolete old scan-utils
# in case we're built without scan_utils
%if %{without scan_utils}
Obsoletes:      hplip-scan-utils < %{version}
%endif

%description utils
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
support for HP printers, scanners, and all-in-one devices.

This package contains graphical and command line utilities with extended
functionality, specifically "hp-toolbox". It is not necessary for printing
and scanning with HP devices.

For setting up new devices, install hplip-driver-* or hplip-ppds-* packages.

%package base
Summary:        HPLIP basic utilities
Group:          Hardware/Printing
Requires:       %{name}-cups = %{version}-%{release}
Requires:       %{name}-sane = %{version}-%{release}
# hp-plugin installation fails without /etc/sane/dll.conf
Requires:       sane-backends
Requires:       wget

%description base
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
support for HP printers, scanners, and all-in-one devices.

This package contains basic command line utilities for probing HP printers
and all-in-one devices, and for installing the proprietary HP plugin.

For setting up new devices, install hplip-driver-* or hp-ppds-* packages.

%package common
Summary:        HPLIP common files
Group:          Hardware/Printing
BuildArch:      noarch
Provides:       %{name}-udev-rules = %{version}-%{release}
Obsoletes:      %{name}-udev-rules < %{version}-%{release}

%description common
This package contains common files needed by other hplip packages.

%package -n libhplip0
Summary:        Shared libraries for the HPLIP printing system
Group:          System/Libraries
# rpmlint complains about a versioned dependency here
Requires:       %{name}-common

%description -n libhplip0
This package contains shared libraries needed by other hplip packages.

%package cups
Summary:        HPLIP printing backends and filters for CUPS
Group:          Hardware/Printing
# Require the exact matching version-release of the libhpli0 sub-package.
Requires:       %{name}-common = %{version}-%{release}
Requires:       cups > 1.5
Requires:       libhplip0 = %{version}-%{release}
%if 0%{?suse_version} >= 1500
# Works with either driver-hpcus or ppds-hpcups; driver-hpcups is preferred
Recommends:     (%{name}-driver-hpcups or %{name}-ppds-hpcups)
Suggests:       %{name}-driver-hpcups
Supplements:    (%{name}-common and cups)
%else
# On older distros, prefer ppds for historical reasons
Recommends:     %{name}-ppds-hpcups
%endif
# cups-filters can be provided by the cups-filters2 package
Recommends:     cups-filters
Recommends:     %{name}-base = %{version}
Recommends:     ghostscript
Suggests:       %{name} = %{version}
Suggests:       %{name}-ppds-hpps = %{version}
Suggests:       %{name}-ppds-postscript = %{version}
Suggests:       %{name}-ppds-fax = %{version}

%description cups
This package contains filter programs and backends for the CUPS printing
system which are necessary for printing with HP printers.

%package driver-hpcups
Summary:        Driver for HP printers and all-in-one devices (hpcups)
Group:          Hardware/Printing
BuildArch:      noarch
Requires:       %{name}-cups = %{version}-%{release}
Conflicts:      %{name}-ppds-hpcups
# Until October 2025, the package with the misleading name "hplip-hpijs"
# provided the hpcups driver and PPDs
Provides:       %{name}-hpijs = %{version}-%{release}
Obsoletes:      %{name}-hpijs < %{version}-%{release}

%description driver-hpcups
This package provides printer setup support for most HP printers and all-in-one
devices. It uses CUPS functionality to generate the PPDs for the printers
dynamically.

This package is not necessary for operation of already configured devices.

%package ppds-hpcups
Summary:        PPDs for HP printers and all-in-one devices (hpcups)
Group:          Hardware/Printing
BuildArch:      noarch
Requires:       %{name}-cups = %{version}-%{release}
Conflicts:      %{name}-driver-hpcups
# Until October 2025, the package with the misleading name "hplip-hpijs"
# provided the hpcups driver and PPDs
Provides:       %{name}-hpijs = %{version}-%{release}
Obsoletes:      %{name}-hpijs < %{version}-%{release}

%description ppds-hpcups
This package provides printer setup support for most HP printers and all-in-one
devices. It contains statically compiled PPDs.

This package is not necessary for operation of already configured devices.

%package ppds-postscript
Summary:        PPDs for HP printers (PostScript)
Group:          Hardware/Printing
BuildArch:      noarch
# Also PostScript printers may benefit from HP's special CUPS backend 'hp'
# but normally PostScript printers also work with the generic CUPS backends:
Recommends:     %{name}-cups = %{version}-%{release}

%description ppds-postscript
This package provides printer setup support for HP PostScript printers that need no
CUPS filter.

This package is not necessary for operation of already configured devices.

%package ppds-hpps
Summary:        PPDs for HP printers (PostScript + hpps)
Group:          Hardware/Printing
BuildArch:      noarch
Requires:       %{name}-cups = %{version}-%{release}

%description ppds-hpps
This package provides printer setup support for HP PostScript printers using the
hpps filter, which adds support for model-specific functionality such as
"Secure printing".

This package is not necessary for operation of already configured devices.

%package ppds-fax
Summary:        PPDs for HP Fax devices
Group:          Hardware/Printing
BuildArch:      noarch
Requires:       %{name}-cups = %{version}-%{release}

%description ppds-fax
This package provides support for HP fax devices and multi-function devices.

This package is not necessary for operation of already configured devices.

%package ppds-plugin
Summary:        PPDs for HP printers (proprietary plugin)
Group:          Hardware/Printing
BuildArch:      noarch
Requires:       %{name}-cups = %{version}-%{release}
# Require hplip for the hp-plugin tool
Requires:       %{name}-base = %{version}-%{release}

%description ppds-plugin
This package provides printer setup support for HP printers that need the
proprietary HPLIP plugin. Use the hp-plugin tool from the %{name}-base package
to install the plugin.

This package is not necessary for operation of already configured devices.

%package sane
Summary:        SANE backends for HP scanners and all-in-one devices
Group:          Hardware/Scanner
# Require the exact matching version-release of the libhpli0 sub-package.
Requires:       %{name}-common = %{version}-%{release}
Requires:       libhplip0 = %{version}-%{release}
Recommends:     %{name}-base = %{version}
Suggests:       %{name} = %{version}
Enhances:       sane-backends
# Automatically install this package if hplip-common and sane-backends are
%if 0%{?suse_version} >= 1500
Supplements:    (%{name}-common and sane-backends)
%endif

%description sane
The Hewlett-Packard Linux Imaging and Printing project (HPLIP) provides
support for HP printers, scanners, and all-in-one devices.

This package provides scanning support for HP scanners and all-in-one
devices. Some devices need the proprietary hplip plugin. Use the hp-plugin
tool from the %{name}-base package to install the plugin.

%if %{with scan_utils}
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
%endif

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
This package is only required by developers.

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
%if 0%{?suse_version} >= 1500
# This patch replaces python-config by python3-config, don't apply on SLE12
%patch -P 404 -p1
%endif
%patch -P 405 -p1
%patch -P 500 -p1
%patch -P 601 -p1
%patch -P 602 -p1
%patch -P 603 -p1
%patch -P 604 -p1
%patch -P 605 -p1
%patch -P 606 -p1
%patch -P 607 -p1
%patch -P 608 -p1
%patch -P 610 -p1
%patch -P 611 -p1
%patch -P 612 -p1
%patch -P 651 -p1
%if 0%{?suse_version} < 1500
# python2 compatibility
%patch -P 700 -p1
%patch -P 701 -p1
%endif

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
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} -Wno-error=return-type"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -Wno-error=return-type"
# --disable-pp-build disables parallel port build because parallel port support is deprecated by upstream HPLIP
# and by upstream in general cf. "Parallel port printers" at https://en.opensuse.org/SDB:Installing_a_Printer
# Since version 3.9.6 the default printer driver install changed from hpijs to hpcups.
# According to http://hplipopensource.com/hplip-web/release_notes.html
# all drv installs require CUPSDDK 1.2.3 or higher.
# Otherwise a static PPD install must be performed.
# Because foomatic-rip-hplip has CVE-2011-2697 (bnc#698451) plus a leftover in CVE-2004-0801 (bnc#59233)
# which are fixed up to openSUSE 11.4 with patches, after openSUSE 11.4 (i.e. since openSUSE 12.1)
# foomatic-rip-hplip is no longer installed and because foomatic-rip is a generic security issue
# and only used by 'hpijs' which is dropped via --disable-hpijs-install also foomatic support is dropped
# via --disable-foomatic-drv-install --disable-foomatic-ppd-install --disable-foomatic-rip-hplip-install
# see https://bugzilla.suse.com/show_bug.cgi?id=1250481
# Since HPLIP 3.13.10 --with-htmldir is new but it does not inhertit its value from --with-docdir
# so that --with-htmldir must be explicitly set.
%configure \
            --disable-qt3 \
            %{config_qt_opts} \
            --disable-policykit \
            --enable-doc-build \
            --enable-network-build \
            --disable-pp-build \
            --enable-scan-build \
            --enable-gui-build \
            --enable-fax-build \
            --enable-dbus-build \
            --enable-hpcups-install \
            --enable-cups-drv-install \
            --disable-cups-ppd-install \
            --disable-hpijs-install \
            --disable-imageProcessor-build \
            --disable-foomatic-drv-install \
            --disable-foomatic-ppd-install \
            --disable-foomatic-rip-hplip-install \
            --with-hpppddir=%{_datadir}/cups/model/manufacturer-PPDs/%{name} \
            --with-cupsbackenddir=%{_prefix}/lib/cups/backend \
            --with-cupsfilterdir=%{_prefix}/lib/cups/filter \
            --with-drvdir=%{drvdir} \
            --with-mimedir=%{_sysconfdir}/cups \
            --with-docdir=%{_defaultdocdir}/%{name} \
            --with-htmldir=%{_defaultdocdir}/%{name} \
	    PYTHON=%{pyexe}
%make_build
sed -i 's|ppd/hpcups/\*.ppd.gz ||g' Makefile

%install
%make_install

# Make and install Python compiled bytecode files
%py_compile -O %{buildroot}%{_datadir}/hplip
# Hardlink .pyc and .pyo when they have same content.
# Do not run "fdupes buildroot/_datadir/hplip" because
# fdupes will link any files with same content there
# which can have unexpected side-effects, compare
# https://bugzilla.opensuse.org/show_bug.cgi?id=784670
# E.g. fdupes may create links between files that belong
# to different subpackages.
for pyc in $( find %{buildroot}%{_datadir}/hplip -name '*.pyc' )
do
   pyo="${pyc%.pyc}.opt-1.pyc"
   if test -f "$pyo" && cmp -s "$pyc" "$pyo"
   then
        ln -f "$pyc" "$pyo"
   fi
done

# see https://bugs.launchpad.net/hplip/+bug/1064247 and bnc#783810
chmod a+x %{buildroot}%{_datadir}/hplip/fax/pstotiff
# see https://bugs.launchpad.net/bugs/1018303 and bnc#780413
# using fixed "/var/log/hp" because this is hardcoded in the HPLIP sources
test -d %{buildroot}%{_localstatedir}/lib/hp || install -d %{buildroot}%{_localstatedir}/lib/hp
# Create a /var/log/hp/tmp/ directory that is needed by hp-sendfax
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

# Create appropriate sub-directories for PPDs:
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-ps
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpps
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-plugin
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpcups
install -d %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/%{name}-fax

gunzip *.ppd.gz
for p in *.ppd
do
    # Add a line-feed to the end of all PPDs to fix those PPDs where it is missing.
    # See Novell/Suse Bugzilla bug #309832: Unix/Linux text files must end with a line-feed.
    # Otherwise reading the last line results EOF and then some programs may ignore the last line:
    echo -en '\n' >>"$p"
    # Move PPDs into appropriate sub-directories:
    if grep -q '^\*NickName:.*requires proprietary plugin' "$p"; then
        dir=../%{name}-plugin
    else
	filter=$( grep -m1 cupsFilter "$p" ) || true
	case $filter in
	    *foomatic-rip*)
		# Skip 'hpijs' PPDs which are those that use foomatic-rip as cupsFilter
		# see https://bugzilla.suse.com/show_bug.cgi?id=1250481#c1
		continue;;
	    *hpcupsfax*|*hpcdmfax*)
		dir=../%{name}-fax;;
	    *hpcups*)
		dir=../%{name}-hpcups;;
	    *hpps*)
		dir=../%{name}-hpps;;
	    "")
		dir=../%{name}-ps;;
	esac
   fi
   gzip -n -9 "$p"
   mv -f "$p.gz" "$dir"
done

# Switch back to the usual build log messages:
set -x
# End of "General tests and adjustments for all PPDs":
popd

# Replace the invalid Desktop categories
%if %{with update_desktop}
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/hplip.desktop System HardwareSettings
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/hp-uiscan.desktop System HardwareSettings
%suse_update_desktop_file -i %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop
%endif
# End of "Desktop menue entry stuff".

# Remove libtool archives:
find "%{buildroot}" -type f -name "*.la" -delete -print

# Run fdupes only on the images subdir to avoid broken symlinks in subpackages:
%fdupes -s %{buildroot}%{_datadir}/hplip/data/images

# Ensure we have no unpackaged files if build without scan-util:
%if !%{with scan_utils}
rm -f %{buildroot}%{_bindir}/hp-scan
rm -f %{buildroot}%{_bindir}/hp-uiscan
rm -f %{buildroot}%{python_sitearch}/scanext.so
rm -f %{buildroot}%{_datadir}/applications/hp-uiscan.desktop
%endif

%post common
%udev_rules_update

%postun sane
# Earlier versions of hplip modified /etc/sane.d/dll.conf
# Now we use /etc/sane.d/dll.d (multiple hpaio entries don't hurt).
# If the package was removed (but not if it was updated)
# then remove the hpaio lines in /etc/sane.d/dll.conf.
if [ "$1" = "0" ] && [ -w %{_sysconfdir}/sane.d/dll.conf ]; then
    sed -i -e '/hpaio/d' %{_sysconfdir}/sane.d/dll.conf
fi
exit 0

%post -n libhplip0 -p %{run_ldconfig}
%postun -n libhplip0 -p %{run_ldconfig}

%post base -p %{run_ldconfig}
%postun base -p %{run_ldconfig}

%files
# empty

%files base
%(for _x in %{basic_tools}; do echo "%{_bindir}/hp-$_x"; done)
%(for _x in %{basic_tools}; do echo "%{_datadir}/hplip/$_x.py"; done)
%(for _x in %{basic_tools}; do echo "%{_datadir}/hplip/__pycache__/$_x.*"; done)
%{_datadir}/hplip/base
%exclude %{_datadir}/hplip/base/imageprocessing.py*
%exclude %{_datadir}/hplip/base/__pycache__/imageprocessing.*
%{_datadir}/hplip/fax
%{_datadir}/hplip/installer
%{_datadir}/hplip/prnt
%{_libdir}/python%{pyver}/site-packages/cupsext.*
%{_libdir}/python%{pyver}/site-packages/hpmudext.*
%{_libdir}/python%{pyver}/site-packages/pcardext.*

%files utils
%config %{_sysconfdir}/xdg/autostart/hplip-systray.desktop
# GUI tools (not in the basic_tools list above)
%{_bindir}/hp-check
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-devicesettings
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-faxsetup
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-pqdiag
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-systray
%{_bindir}/hp-toolbox
%{_bindir}/hp-wificonfig
# Fixme: these tools are useless on openSUSE.
%{_bindir}/hp-pkservice
%{_bindir}/hp-uninstall
%{_bindir}/hp-upgrade
%doc %{_defaultdocdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/hplip/
%{expand:%(for _x in %{basic_tools}; do echo "%%exclude %{_datadir}/hplip/$_x.py"; done)}
%{expand:%(for _x in %{basic_tools}; do echo "%%exclude %{_datadir}/hplip/__pycache__/$_x.*"; done)}
%exclude %{_datadir}/hplip/base
%exclude %{_datadir}/hplip/fax
%exclude %{_datadir}/hplip/installer
%exclude %{_datadir}/hplip/prnt
%exclude %{_datadir}/hplip/data/models/models.dat
%exclude %{_datadir}/hplip/base/imageprocessing.py*
%exclude %{_datadir}/hplip/%{ui_dir}/scandialog.py*
%exclude %{_datadir}/hplip/scan
%exclude %{_datadir}/hplip/scan.py*
%exclude %{_datadir}/hplip/uiscan.py*
%exclude %{_datadir}/hplip/__pycache__/uiscan.*
%exclude %{_datadir}/hplip/__pycache__/scan.*
%exclude %{_datadir}/hplip/base/__pycache__/imageprocessing.*
%exclude %{_datadir}/hplip/%{ui_dir}/__pycache__/scandialog.*

%if %{with scan_utils}
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
%if %{pyversion} != 2
%{_datadir}/hplip/%{ui_dir}/scandialog.py*
%{_datadir}/hplip/__pycache__/uiscan.*
%{_datadir}/hplip/__pycache__/scan.*
%{_datadir}/hplip/base/__pycache__/imageprocessing.*
%{_datadir}/hplip/%{ui_dir}/__pycache__/scandialog.*
%endif
%endif

%files common
%config %{_sysconfdir}/hp/
%config %{_sysconfdir}/cups/pstotiff.convs
%config %{_sysconfdir}/cups/pstotiff.types
%{_datadir}/%{name}/data/models/models.dat
%{_udevrulesdir}/56-hpmud.rules
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/manufacturer-PPDs
# Use fixed "/var/log/hp" because this is hardcoded in the HPLIP sources.
# Regarding attr(0775,root,lp) see the comment for /var/log/hp/tmp below:
%dir %attr(0775,root,lp) %{_localstatedir}/log/hp
# Regarding attr(0775,root,lp) for /var/log/hp/tmp
# see https://bugzilla.novell.com/show_bug.cgi?id=800312#c0
# i.e. it is reasonable secure and hp-sendfax works with it:
%dir %attr(0775,root,lp) %{_localstatedir}/log/hp/tmp
# Use fixed "/var/lib/hp" because this is hardcoded in the HPLIP sources:
%dir %{_localstatedir}/lib/hp

%files -n libhplip0
%{_libdir}/libhpip.so.*
%{_libdir}/libhpipp.so.*
%{_libdir}/libhpmud.so.*
%{_libdir}/libhpdiscovery.so.*

%files cups
%dir %{_prefix}/lib/cups/filter
%{_prefix}/lib/cups/filter/hpps
%{_prefix}/lib/cups/filter/hpcups
%{_prefix}/lib/cups/filter/hpcupsfax
%{_prefix}/lib/cups/filter/hpcdmfax
%{_prefix}/lib/cups/filter/pstotiff
%dir %{_prefix}/lib/cups/backend
%{_prefix}/lib/cups/backend/hp
%{_prefix}/lib/cups/backend/hpfax

%files driver-hpcups
%dir %{drvdir}
%{drvdir}/hpcups.drv

%files ppds-hpcups
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpcups

%files ppds-hpps
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-hpps

%files ppds-postscript
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-ps

%files ppds-plugin
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-plugin

%files ppds-fax
%{_datadir}/cups/model/manufacturer-PPDs/%{name}-fax

%files sane
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-hpaio.so.*
%dir %{_sysconfdir}/sane.d
%dir %{_sysconfdir}/sane.d/dll.d
%config %{_sysconfdir}/sane.d/dll.d/hpaio

%files devel
%{_libdir}/libhpip.so
%{_libdir}/libhpipp.so
%{_libdir}/libhpmud.so
%{_libdir}/libhpdiscovery.so
%{_libdir}/sane/libsane-hpaio.so

%changelog
