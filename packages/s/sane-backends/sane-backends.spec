#
# spec file for package sane-backends
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


# Cf. https://rpm.org/user_doc/conditional_builds.html
# by default enable support for PWG eSCL network backend
%bcond_without escl
# by default disable support for PWG eSCL network backend
#bcond_with escl

Name:           sane-backends
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libv4l-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig
%if %{with escl}
BuildRequires:  pkgconfig(avahi-client) >= 0.6.24
BuildRequires:  pkgconfig(libcurl)
# since sane-backends 1.0.31 the escl backend requires libpoppler-glib-devel
# cf. https://gitlab.com/sane-project/backends/-/blob/master/INSTALL.linux
BuildRequires:  libpoppler-glib-devel
%endif
BuildRequires:  pkgconfig(libusb-1.0)
# The pixma backend requires libxml2
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
%systemd_requires

%define libname libsane1
# SANE build systems mangles backend SONAMEs to be libsane.so.x
%define __provides_exclude_from %{_libdir}/sane

Summary:        SANE (Scanner Access Now Easy) Scanner Drivers
License:        GPL-2.0-or-later AND SUSE-GPL-2.0+-with-sane-exception AND SUSE-Public-Domain
Group:          Hardware/Scanner
Version:        1.0.31
Release:        0
URL:            http://www.sane-project.org/
# On https://gitlab.com/sane-project/backends/-/releases
# there are two links, the first one is called "Source code (tar.gz)" that pints to
# https://gitlab.com/sane-project/backends/-/archive/1.0.31/backends-1.0.31.tar.gz
# and the second one is called "sane-backends-1.0.31.tar.gz" that pints to
# https://gitlab.com/sane-project/backends/uploads/8bf1cae2e1803aefab9e5331550e5d5d/sane-backends-1.0.31.tar.gz
# The first one "backends-1.0.31.tar.gz" does not build, as it does not contain a prebuilt configure script,
# and autoconf fails as it requires a complete git clone, see https://gitlab.com/sane-project/backends/issues/248
# We use the second one "sane-backends-1.0.31.tar.gz" that is a dist tarball with a prebuilt configure script via
# wget https://gitlab.com/sane-project/backends/uploads/8bf1cae2e1803aefab9e5331550e5d5d/sane-backends-1.0.31.tar.gz
Source0:        sane-backends-1.0.31.tar.gz
# Source100... is SUSE specific stuff:
# Source102 is the OpenSLP registration file for the saned:
Source102:      sane.reg
# Source110 creates our hpaio.desc file directly from the models.dat file of HPLIP:
Source110:      create_hpaio.desc_from_models.dat
# Source111 is the models.dat file of HPLIP:
Source111:      models.dat
# Was initially just dumped in as Source1 to "package baselibs.conf"
# (see the matching explanatory entry in the RPM changelog):
Source190:      baselibs.conf
# Source200... is scanner autoconfiguration stuff:
# Source200 and Source201 generate the 56-sane-backends-autoconfig.rules file
# for automated scanner driver activation via udev ("scanner autoconfiguration").
# Source200 is a copy of /usr/lib/YaST2/bin/create_scanner_database
# to avoid yast2-scanner in BuildRequires which would drag in almost the whole YaST:
Source200:      create_scanner_database
# Source201 actually generates the 56-sane-backends-autoconfig.rules file
# by reading scanner.database which was created before by create_scanner_database
# to extract the needed info from which create_sane-backends-autoconfig.rules
# generates the 56-sane-backends-autoconfig.rules file:
Source201:      create_sane-backends-autoconfig.rules
# Sources 202 and 203 are files to enable socket based service activation which replaced xinetd
Source202:      saned@.service
Source203:      saned.socket
# Patch100... is SUSE specific stuff:
# Patch102 adapt_epkowa.desc_for_yast2-scanner.patch adapts epkowa.desc for yast2-scanner
# (see https://bugzilla.opensuse.org/show_bug.cgi?id=788756#c14).
# It adds "requires DFSG non-free Image Scan software from Avasys" to all comments
# (or adds such a comment if there is not yet a comment) so that yast2-scanner
# (via "requires DFSG non-free" string match in create_scanner_database)
# shows always the info regarding "Image Scan" download from Avasys
# (compare https://bugzilla.novell.com/show_bug.cgi?id=569917
#  and https://bugzilla.novell.com/show_bug.cgi?id=746038).
# Furthermore it removes "unsupported" models from epkowa.desc because
# otherwise there would be confusing model entries shown in yast2-scanner:
Patch102:       adapt_epkowa.desc_for_yast2-scanner.patch
# See https://bugzilla.novell.com/show_bug.cgi?id=437293
%ifarch ppc64
Obsoletes:      sane-64bit
%endif
# Up to SLE10 there was the package name 'sane' for 'sane-backends'.
# Therefore this RPM provides 'sane' and it also obsoletes it.
# The {version} is needed in both Provides and Obsoletes
# to avoid a RPMLINT warning that the package obsoletes itself:
Provides:       sane = %{version}
Obsoletes:      sane < %{version}
# Pull in the same version, not just matching soname
Requires:       %{libname} = %{version}

%description
The software consists of SANE scanner drivers,
"scanimage," and the "saned" daemon.

A SANE scanner driver is used via a SANE front-end.
This package contains the command line front-end "scanimage".
There are graphical front-ends in other packages like
XSane (package xsane), Skanlite for KDE4 (package skanlite),
and Kooka for KDE3 (package kdegraphics3-scan).

The "saned" daemon provides the service "sane-port"
to access scanners that are connected to a server
via network from client hosts that run the "net" meta driver.

%package devel
Summary:        Development files for sane-backends
License:        GPL-2.0-or-later AND SUSE-GPL-2.0+-with-sane-exception AND SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains the development files for sane-backends.

%package -n %{libname}
Summary:        Core SANE library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Public-Domain
Group:          Hardware/Scanner
Conflicts:      sane-backends < %{version}
Recommends:     sane-backends

%description -n %{libname}
This contains the SANE library. Individual scanner backends are provided
by sane-backends or third party packages.

%package autoconfig
Summary:        USB Scanner Autoconfiguration
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Public-Domain
Group:          Hardware/Scanner
Requires:       %{libname} = %{version}
# When sane-backends is already installed, try to install also sane-backends-autoconfig if available:
Supplements:    sane-backends

%description autoconfig
USB scanner autoconfiguration happens via udev.

The file /udev/rules.d/56-sane-backends-autoconfig.rules contains
entries for those USB scanners where the USB IDs are known, which are
supported by a free driver, where the support status is "complete" or
"good", and which do not require firmware upload.

When a USB scanner is connected and its USB IDs match to an entry in
the 56-sane-backends-autoconfig.rules file, the matching scanner driver
is activated (i.e. the driver line in /etc/sane.d/dll.conf is
activated).

It enables scanner drivers but never disables them. The reason is that
enabled drivers do not hurt so that an automated disable would make it
only overcomplicated because when more than one scanner uses the same
driver, a complicated check would be needed to avoid that the driver is
accidentally disabled when only one scanner was disconnected.

If you do not like automated driver activation, do not install this
package or remove it when it is already installed.

%package -n sane-saned
Summary:        Sane network server
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Public-Domain
Group:          Hardware/Scanner
Provides:       sane-backends:%{_sbindir}/saned
Conflicts:      %{name} < %{version}

%description -n sane-saned
Saned allows access to locally attached scanners over the network.

%prep
%setup -q
# Patch100... is SUSE specific stuff:
# Patch102 adapt_epkowa.desc_for_yast2-scanner.patch adapts epkowa.desc for yast2-scanner
# see https://bugzilla.opensuse.org/show_bug.cgi?id=788756#c14
%patch102

# Remove hpoj.desc completely to avoid confusion with its successor hpaio.desc
# because since openSUSE 10.3 the package hp-officeJet (for hpoj.desc) is dropped.
sed -i -e '/descriptions-external\/hpoj.desc / d' doc/Makefile{.am,.in}
rm doc/descriptions-external/hpoj.desc

# For compliance with the other description files in the sane-backends sources
# change the manufacturer name from "Hewlett Packard" to "Hewlett-Packard":
for d in doc/descriptions-external/hp3770.desc doc/descriptions-external/hp8200.desc
do sed -i -e '/^:mfg/s/Hewlett Packard/Hewlett-Packard/' $d
done
# Create our hpaio.desc descriptions-external file
# (use it as bash input because sources may be installed without execute permissions):
bash %{SOURCE110} <%{SOURCE111} >doc/descriptions-external/hpaio.desc
# Copy the create_scanner_database script from the sources directory to the build directory
# to avoid that the original source becomes modified later in the install section
# and ends up in the source RPM, see https://bugzilla.novell.com/show_bug.cgi?id=463464#c11
cp %{SOURCE200} create_scanner_database
chmod u+x create_scanner_database

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE -DGIMP_ENABLE_COMPAT_CRUFT=1 -fno-strict-aliasing"
export LDFLAGS="-L/%_lib $LDFLAGS"
# Enable pthread instead of fork (used in Debian since Feb 2009 and no issues so far),
# see https://bugzilla.novell.com/show_bug.cgi?id=633780
# Disable locking because /var/lock/sane/ would be a world-writable directory.
./configure --prefix=/usr \
            --exec-prefix=/usr \
            --sysconfdir=%{_sysconfdir} \
            --libdir=%{_libdir} \
            --sbindir=%{_sbindir} \
            --mandir=%{_mandir} \
            --datadir=%{_datadir} \
            --docdir=%{_defaultdocdir}/sane-backends \
            --enable-pthread \
            --with-usb \
%if %{with escl}
            --with-avahi \
%endif
            --disable-locking
# Enable locking for backends where "99" is the group of the lockfile path (LOCKPATH_GROUP)
# because "99" is the group of the user who runs the build when norootforbuild is used
# and set localstatedir to have the lock files in /var/lock/sane (see backend/Makefile.in).
# Disabled because locking requires a world-writable /var/lock/sane/ directory:
#            --enable-locking \
#            --with-group=99 \
#            --localstatedir=/var
%make_build

%install
%makeinstall
# The actual driver modules are installed as libsane-<driver>.so.{version}
# and two libsane-<driver>.so.1 and libsane-<driver>.so links point to them.
# Additionally a libsane-<driver>.la libtool archive file is installed
# which could be used to find the correct module file name to dlopen the module.
# Only the dll meta-backend (/usr/lib/libsane.so.1.0.19) links with driver modules.
# The dll meta-backend looks only for libsane-<driver>.so.1 and uses dlopen(3) directly.
# The dll meta-backend needs neither libsane-<driver>.so nor libsane-<driver>.la.
# RPMLINT complains about libsane-<driver>.so with "devel-file-in-non-devel-package".
# Therefore the libsane-<driver>.so and libsane-<driver>.la files are simply removed.
rm %{buildroot}%{_libdir}/sane/libsane-*.so
rm %{buildroot}%{_libdir}/sane/libsane-*.la
# Because of https://bugzilla.novell.com/show_bug.cgi?id=592143 for openSUSE 11.3
# even the /usr/lib/libsane.la file for the dll meta-backend is removed
# regardless that it is unknown how whatever third-party scanning frontend
# may like to link with SANE (i.e. with the dll meta-backend).
# The frontends which are provided by openSUSE /usr/bin/scanimage,
# /usr/bin/xsane, and /usr/bin/skanlite do not need it.
# The /usr/lib/libsane.so link for the dll meta-backend is kept because it is needed
# during build-time by other packages which need sane-backends to build.
rm %{buildroot}%{_libdir}/libsane.la
# Disable all backends in /etc/sane.d/dll.conf to avoid problems when backends are active by default:
perl -pi -e 's/^([^#].*)$/#$1/' %{buildroot}%{_sysconfdir}/sane.d/dll.conf
# Allow all users to write into /var/lock/sane/ so that the backends work for normal users
# and set the sticky bit (i.e. others are not allowed to remove lock files).
# Disabled because package-specific world-writable directories are not allowed:
#chmod 1777 {buildroot}/var/lock/sane/
# Install the descriptions and descriptions-external files.
# These files are the sources to make {_defaultdocdir}/sane/sane-backends/*.html
# but these source files must also exist in the installed sane package
# because YaST needs them to create its scanner database:
for d in descriptions descriptions-external
do install -d -m755 %{buildroot}%{_datadir}/sane/$d
   install -m644 doc/$d/*.desc %{buildroot}%{_datadir}/sane/$d
done
# Add ':firmware "required"' entries for the respective scanners to the descriptions files
# so that YaST can show firmware upload related information to the user of such a scanner.
# This must be done after build because those entries are a SUSE specific extension.
# To determine scanners which require firmware upload, search the man pages
# for backends which provide support for firmware upload.
# Use a command like
#   for m in /usr/share/man/man5/sane-*
#   do man -E ascii -P cat -l $m 2>/dev/null | grep -q -i firmware && echo $m
#   done
# to find backend man pages which mention "firmware".
# In version 1.0.19 the following man pages mention "firmware":
#   sane-agfafocus: mentiones only "firmware revision" (no firmware upload)
#   sane-apple: mentiones only "firmware revision" (no firmware upload)
#   sane-artec: mentiones only "problems with firmware v1.92" (no firmware upload)
#   sane-artec_eplus48u: "you need a firmware file for your scanner" (unconditioned firmware upload)
#   sane-bh: mentiones only "requires RSC firmware level 1.5" (no firmware upload)
#   sane-epjitsu: "these scanners require a firmware file" (unconditioned firmware upload)
#   sane-gt68xx: "you need a firmware file for your scanner" (unconditioned firmware upload)
#   sane-hp: mentiones only "no firmware support for contrast" (no firmware upload)
#   sane-matsushita: mentiones only "scanner with proper firmware" (no firmware upload)
#   sane-microtek2: mentiones only "firmware of the scanner provides" (no firmware upload)
#   sane-sharp: mentiones only "bug in the firmware" (no firmware upload)
#   sane-snapscan: "USB scanners ... scanners that need a firmware upload" (conditioned firmware upload)
#   sane-st400: mentiones only "firmware revision" (no firmware upload)
#   sane-teco2: mentiones only "firmware 1.09" (no firmware upload)
# As far as we know all scanners which use
# the backend gt68xx and the related backend artec_eplus48u
# or the backend epjitsu require a firmware upload,
# see "man sane-gt68xx" and http://www.meier-geinitz.de/sane/gt68xx-backend/
# and see "man sane-artec_eplus48u" and "man sane-epjitsu":
for b in gt68xx artec_eplus48u epjitsu
do sed -i -e 's/^:model.*$/&\n:firmware "required"/' %{buildroot}%{_datadir}/sane/descriptions/$b.desc
done
# As far as we know (almost) all USB scanners (but not the SCSI scanners)
# which use the backend snapscan require a firmware upload,
# see "man sane-snapscan" and http://snapscan.sourceforge.net/:
sed -i -e 's/^:interface "USB".*$/&\n:firmware "required"/' %{buildroot}%{_datadir}/sane/descriptions/snapscan.desc
# Only the "SnapScan 1236u" needs no firmware upload (see Suse/Novell bug #73960):
sed -i -e '/:model "SnapScan 1236u"/,/:firmware "required"/s/required//' %{buildroot}%{_datadir}/sane/descriptions/snapscan.desc
# Scanner autoconfiguration stuff (packaged in sane-backends-autoconfig):
# It must be done before the udev libsane.rules stuff because the scanner database is needed there.
# This requires the installed descriptions and descriptions-external files
# because create_scanner_database reads the description files to extract the needed info
# to create the scanner database from which create_sane-backends-autoconfig.rules
# extracts the needed info to generate the 56-sane-backends-autoconfig.rules file
# for automated scanner driver activation via udev.
# Note that driver activation alone is not sufficient
# to have a usable "scanner autoconfiguration" for the user.
# What is also needed are appropriate USB device file permissions
# so that the user's scanning software can access the device.
# But this is already in place via the the udev libsane.rules file
# which contains a superset of USB scanner IDs (all known USB scanner IDs)
# compared to the USB scanner IDs in 56-sane-backends-autoconfig.rules,
# see create_sane-backends-autoconfig.rules for which USB scanners
# automated driver activation is done (basically only those scanners
# which are supported by a free driver, which do not require firmware upload,
# and where the support status is "complete" or "good").
# Modify create_scanner_database to find the description files in the BuildRoot directory
# (the usual delimiter '/' cannot be used because buildroot contains it too):
sed -i -e 's|/usr/share/sane/descriptions|%{buildroot}/usr/share/sane/descriptions|' create_scanner_database
# Create the scanner database and store it because it is also needed later
# to disable "unsupported" model entries in the udev libsane.rules file.
# The file name "scanner.database" is used hardcoded in create_sane-backends-autoconfig.rules.
./create_scanner_database >scanner.database
# Run create_sane-backends-autoconfig.rules which reads scanner.database
# (use it as bash input because sources may be installed without execute permissions):
bash %{SOURCE201} >autoconfig.rules
# Install the scanner autoconfiguration udev rules file:
install -d %{buildroot}%{_udevrulesdir}
install -m644 autoconfig.rules %{buildroot}%{_udevrulesdir}/56-sane-backends-autoconfig.rules
# Regarding udev:
# Modify the generated tools/udev/libsane.rules file as follows:
# All GROUP="scanner" are replaced by GROUP="lp".
# There is no group "scanner" in /etc/group for openSUSE.
# For all-in-one devices (i.e. printer + scanner, e.g. "EPSON Stylus" devices)
# the group must be "lp" so that the CUPS usb backend which runs
# as user "lp" (who is member of the group "lp") can send printing data
# to the printer unit (i.e. the printer interface of the USB device).
# It is sufficiently secure and reasonable easy to use by default
# the same group "lp" for printers and scanners because both kind of devices
# usually require physical user access (to get the printed paper or
# to place a paper on the scanner) so that both kind of devices
# should usually require the same kind of security.
sed -i -e 's/GROUP="scanner"/GROUP="lp"/' tools/udev/libsane.rules
# Regarding ATTRS{} (formerly SYSFS{}) versus ATTR{} see the Novell/Suse Bugzilla bug
# https://bugzilla.novell.com/show_bug.cgi?id=436085#c0
# but for SCSI scanners "ATTRS" is mandatory see the Novell/Suse Bugzilla bug
# https://bugzilla.novell.com/show_bug.cgi?id=681146#c20
# so that "ATTRS" is replaced by "ATTR" only for USB scanners.
# Upstream: https://gitlab.com/sane-project/backends/-/issues/341
sed -i -e '/^LABEL="libsane_usb_rules_begin"/,/^LABEL="libsane_usb_rules_end"/s/ATTRS/ATTR/g' tools/udev/libsane.rules
# Disable entries for USB scanners which are "unsupported"
# but keep the entries for models for which the support status
# is "complete", "good", "basic", "minimal", "untested"
# because libsane.rules disables USB autosuspend
# which is needed as safe default for any scanner
# (regardless to what extent it is actually supported).
# The only exception are unsupported models
# because it seems to be wrong to have "known but unsupported" devices
# listed in the libsane.rules file because it seems not to make sense
# to set owner, group, and permissions for devices which are not
# supported by SANE which would even cause conflicts if such a
# device is supported by whatever other software,
# see https://bugzilla.novell.com/show_bug.cgi?id=439193
# Extract a list of USB IDs for "unsupported" scanners and store them in unsupportedUSBIDs.
# It can happen that there is a status "unsupported" entry for a backend
# for a model which is actually supported by another backend, for example
# the "Epson Perfection 1670" is "unsupported" by the "epkowa" backend
# but works "good" with the "snapscan" backend
# see https://bugzilla.novell.com/show_bug.cgi?id=439193#c6
cat /dev/null >unsupportedUSBIDs
for USBID in $( grep '||[^|]*|0x[0-9A-Fa-f][0-9A-Fa-f]*:0x[0-9A-Fa-f][0-9A-Fa-f]*|unsupported|' scanner.database | cut -s -d '|' -f 7 | sort -f -u )
do grep -o "|$USBID|.*|" scanner.database | grep -E -q 'complete|good|basic|minimal|untested' || echo $USBID >>unsupportedUSBIDs
done
# Ignore case when using sed to avoid possible problems
# with upper case letters in the USB IDs:
for m in $( sed -e 's/0x/./ig' -e 's/:/.,.ATTR.idProduct.==/' unsupportedUSBIDs )
do if grep -q "^ATTR.idVendor.==$m" tools/udev/libsane.rules
   then echo "Disabling unsupported model matching ATTR.idVendor.==$m"
        sed -i -e "/^ATTR.idVendor.==$m/Is/^ATTR/# ATTR/" tools/udev/libsane.rules
   fi
done
# Add an entry for "SCSI processor EPSON Perfection1640",
# see https://bugzilla.novell.com/show_bug.cgi?id=681146#c43
sed -i -e '/^# Epson Perfection 636S /i# Epson Perfection 1640\nKERNEL=="sg[0-9]*", ATTRS{type}=="3", ATTRS{vendor}=="EPSON", ATTRS{model}=="Perfection1640", MODE="0664", GROUP="lp", ENV{libsane_matched}="yes"' tools/udev/libsane.rules
# Install the udev rules file:
install -m644 tools/udev/libsane.rules %{buildroot}%{_udevrulesdir}/55-libsane.rules
# Service files:
# Sources 202 and 203 are files to enable socket based service activation which replaced xinetd
# Source202 is saned@.service and Source203 is saned.socket
# see https://bugzilla.opensuse.org/show_bug.cgi?id=1074054#c5
# and https://bugzilla.opensuse.org/attachment.cgi?id=760460
install -d -m755 %{buildroot}%{_unitdir}
install -m644 %{SOURCE202} %{buildroot}%{_unitdir}
install -m644 %{SOURCE203} %{buildroot}%{_unitdir}
# OpenSLP registration stuff:
install -d -m755 %{buildroot}%{_sysconfdir}/slp.reg.d
install -m644 %{SOURCE102} %{buildroot}%{_sysconfdir}/slp.reg.d
# Delete documentation files for non-Linux platforms:
rm %{buildroot}%{_defaultdocdir}/sane-backends/{README.aix,README.beos,README.darwin,README.djpeg,README.freebsd,README.hp-ux,README.netbsd,README.openbsd,README.os2,README.solaris,README.unixware2,README.unixware7,README.windows,README.zeta}
# Mark locale-dependent files with the respective 'lang' tag in the file list, see
# https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros#.25find_lang
%find_lang sane-backends

%pre -n sane-saned
if [ $1 = 2 ] ; then
    # In case of an upgrade the erroneously created as directories saned.socket and saned@.service
    # must be removed, otherwise the upgrade will fail,
    # see https://bugzilla.opensuse.org/show_bug.cgi?id=1074054#c5
    # and https://bugzilla.opensuse.org/attachment.cgi?id=760460
    if [ -d /usr/lib/systemd/system/saned.socket ] ; then
        /usr/bin/rmdir /usr/lib/systemd/system/saned.socket
    fi
    if [ -d /usr/lib/systemd/system/saned@.service ] ; then
        /usr/bin/rmdir /usr/lib/systemd/system/saned@.service
    fi
fi
%service_add_pre saned.socket

%post -n sane-saned
%service_add_post saned.socket

%preun -n sane-saned
%service_del_preun saned.socket

%postun -n sane-saned
%service_del_postun saned.socket

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n sane-saned
%dir %{_sysconfdir}/slp.reg.d
%config(noreplace) %{_sysconfdir}/slp.reg.d/*
%{_sbindir}/saned
%{_unitdir}/saned@.service
%{_unitdir}/saned.socket
%doc %{_mandir}/man8/saned.8.gz

%files -f sane-backends.lang
%dir %{_sysconfdir}/sane.d
%config(noreplace) %{_sysconfdir}/sane.d/*.conf
%{_udevrulesdir}/55-libsane.rules
%{_bindir}/scanimage
%{_bindir}/sane-find-scanner
%{_bindir}/gamma4scanimage
%{_bindir}/umax_pp
%{_datadir}/sane/
%{_libdir}/sane/
%exclude %{_libdir}/sane/libsane-dll.so.*
#dir /var/lock/sane
%doc %{_defaultdocdir}/sane-backends/
%doc %{_mandir}/man1/scanimage.1.gz
%doc %{_mandir}/man1/sane-find-scanner.1.gz
%doc %{_mandir}/man1/gamma4scanimage.1.gz
%doc %{_mandir}/man5/sane-*.5.gz
%doc %{_mandir}/man7/sane.7.gz

%files -n %{libname}
%dir %{_libdir}/sane/
%dir %{_sysconfdir}/sane.d
%dir %{_sysconfdir}/sane.d/dll.d/
%{_libdir}/sane/libsane-dll.so.*
%{_libdir}/libsane.so.*

%files devel
%{_bindir}/sane-config
%{_includedir}/sane/
%{_libdir}/libsane.so
%{_libdir}/pkgconfig/sane-backends.pc
%doc %{_mandir}/man1/sane-config.1.gz

%files autoconfig
%{_udevrulesdir}/56-sane-backends-autoconfig.rules

%changelog
