#
# spec file for package cups
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


# _tmpfilesdir is not defined in systemd macros up to openSUSE 13.2
%{!?_tmpfilesdir: %global _tmpfilesdir /usr/lib/tmpfiles.d }
Name:           cups
# CUPS beta version numbers like "2.3b6" can be used as is because
# "zypper vcmp 2.3.b99 2.3.0" shows "2.3.b99 is older than 2.3.0" and
# "zypper vcmp 2.2.99 2.3b6" show "2.2.99 is older than 2.3b6" so that
# version upgrades from 2.2.x via 2.3.b* to 2.3.0 work:
Version:        2.3.3
Release:        0
Summary:        The Common UNIX Printing System
License:        Apache-2.0
Group:          Hardware/Printing
URL:            http://www.cups.org/
# To get Source0 go to https://www.cups.org/software.html or https://github.com/apple/cups/releases or use e.g.
# wget --no-check-certificate -O cups-2.3.3-source.tar.gz https://github.com/apple/cups/releases/download/v2.3.3/cups-2.3.3-source.tar.gz
Source0:        https://github.com/apple/cups/releases/download/v2.3.3/cups-2.3.3-source.tar.gz
# To get Source1 go to https://www.cups.org/software.html or https://github.com/apple/cups/releases or use e.g.
# wget --no-check-certificate -O cups-2.3.3-source.tar.gz.sig https://github.com/apple/cups/releases/download/v2.3.3/cups-2.3.3-source.tar.gz.sig
Source1:        https://github.com/apple/cups/releases/download/v2.3.3/cups-2.3.3-source.tar.gz.sig
# To get Source2 go to https://www.cups.org/pgp.html
Source2:        cups.keyring
# To manually verify Source0 with Source1 and Source2 do e.g.
#   gpg --import cups.keyring
#   gpg --list-keys | grep -1 'CUPS.org' | grep -v 'expired'
#   gpg --verify cups-2.3.3-source.tar.gz.sig cups-2.3.3-source.tar.gz
Source102:      Postscript.ppd.gz
Source105:      Postscript-level1.ppd.gz
Source106:      Postscript-level2.ppd.gz
Source108:      cups-client.conf
Source109:      baselibs.conf
# Patch0...Patch9 is for patches from upstream:
# Source10...Source99 is for sources from SUSE which are intended for upstream:
# Patch10...Patch99 is for patches from SUSE which are intended for upstream:
# Patch10 cups-2.1.0-choose-uri-template.patch adds 'smb://...' URIs to templates/choose-uri.tmpl:
Patch10:        cups-2.1.0-choose-uri-template.patch
# Patch11 cups-2.1.0-default-webcontent-path.patch changes the default path whereto the
# web content is installed from /usr/share/doc/cups to /usr/share/cups/webcontent
# because the files of the CUPS web content are no documentation, see CUPS STR #3578
# and http://bugzilla.novell.com/show_bug.cgi?id=546023#c6 and subsequent comments:
Patch11:        cups-2.1.0-default-webcontent-path.patch
# Patch12 cups-2.1.0-cups-systemd-socket.patch Use systemd socket activation properly:
Patch12:        cups-2.1.0-cups-systemd-socket.patch
# Patch42 Let cupsd start after possible network connection (boo#1111351)
Patch42:        let-cupsd-start-after-network.patch
# Patch100...Patch999 is for private patches from SUSE which are not intended for upstream:
# Patch100 cups-pam.diff adds conf/pam.suse regarding support for PAM for SUSE:
Patch100:       cups-pam.diff
# Patch101 cups-2.0.3-additional_policies.patch adds the 'allowallforanybody' policy to cupsd.conf
# see https://fate.novell.com/303515 and https://bugzilla.suse.com/show_bug.cgi?id=936309
Patch101:       cups-2.0.3-additional_policies.patch
# Patch103 cups-1.4-do_not_strip_recommended_from_PPDs.patch
# reverts the change which was added by Michael Sweet in Jan 2007
# which strips the word "recommended" from NickName in PPDs because
# at least yast2-printer in SUSE needs it, compare the
# 'Why not "recommend" PPDs in the NickName?' and the subsequent
# 'RFC: New Driver Rating/Information Attributes' mail thread on cups@easysw.com:
Patch103:       cups-1.4-do_not_strip_recommended_from_PPDs.patch
# Patch104 cups-config-libs.patch fixes option --libs in cups-config script:
Patch104:       cups-config-libs.patch
# Build Requirements:
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libavahi-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if 0%{?suse_version} >= 1315
BuildRequires:  pkgconfig(krb5)
%else
BuildRequires:  krb5-devel
%endif
%if 0%{?suse_version} > 1310
BuildRequires:  pkgconfig(libsystemd)
%else
BuildRequires:  pkgconfig(libsystemd-daemon)
%endif
BuildRequires:  pkgconfig(systemd)
# Require the exact matching version-release of the cups-client sub-package
# (that requires all native CUPS libraries i.e. the libcups* sub-packages)
# and the cups-config sub-package.
# The exact matching version-release of each sub-package is available
# on the same package repository where the cups package is because
# all are built simulaneously from the same cups source package
# and all required packages are provided on the same repository:
Requires:       cups-client = %{version}-%{release}
Requires:       cups-config = %{version}-%{release}
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  coreutils
# Cf. https://en.opensuse.org/openSUSE:Systemd_packaging_guidelines
# versus https://lists.opensuse.org/opensuse-factory/2015-03/msg00218.html
%{?systemd_requires}
# Since CUPS 1.6 all non-Mac filters are dropped from CUPS
# and provided in the separated cups-filters software from OpenPrinting.org:
Recommends:     cups-filters
# Our Source105 PSLEVEL1.PPD.bz2 and Source106 PSLEVEL2.PPD.bz2 need foomatic-rip
# but this does not justify a RPM Requires so that a weak Recommends is sufficient:
Recommends:     foomatic-filters
# The Ghostscript device "cups" is needed by several CUPS filters
# (in particular the "rasterto..." filters) which might justify a RPM Requires.
# But a RPM requirement for ghostscript would cause a build dependency cycle because
# cups Requires ghostscript which BuildRequires cups-devel which Requires libcups2
# and libcups2 is a sub-package of cups so that there is an implicit build dependency
# cycle between the main-packages cups and ghostscript.
# Furthermore, Ghostscript is not needed on a system where those CUPS filters are not used
# (e.g. on client systems in the network where the filtering hapens on a CUPS server
# or on a CUPS server with only "raw" queues), so that a weak Recommends fits better:
Recommends:     ghostscript
# Install into this non-root directory (required when it is built as non-root user):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Conflicts with other print spoolers which provide same binaries like
# /usr/bin/lp and so on or which may listen on the same port (e.g. cups-lpd
# versus traditional lpd on port 515):
Conflicts:      lprng
Conflicts:      lprold
Conflicts:      plp

%description
CUPS is a modular printing system which allows a computer to act as a
print server. A computer running CUPS is a host that can accept print
jobs from client computers, process them, and send them to the
appropriate printer.

CUPS consists of a print spooler and scheduler, a filter system that
converts the print data to a format that the printer will understand,
and a backend system that sends this data to the print device. CUPS
uses the Internet Printing Protocol (IPP) as the basis for managing
print jobs and queues. It also provides the traditional command line
interfaces for the System V and Berkeley print systems, and provides
support for the Berkeley print system's Line Printer Daemon protocol
and limited support for the server message block (SMB) protocol.

CUPS comes with a built-in web-based interface.

%package -n libcups2
Summary:        HTTP/IPP communication and printer queue and job library
Group:          System/Libraries
Requires:       cups-config
Obsoletes:      cups-libs < %{version}-%{release}
Provides:       cups-libs = %{version}-%{release}

%description -n libcups2
The CUPS library contains all of the core HTTP and IPP communications
code as well as convenience functions for queuing print jobs, getting
printer information, accessing resources via HTTP and IPP, and
manipulating PPD files. The scheduler and all commands, filters, and
backends use this library.

%package -n libcupsimage2
Summary:        CUPS library for working with large images
Group:          System/Libraries

%description -n libcupsimage2
The CUPS imaging library provides functions for managing large
images, doing colorspace conversion and color management, scaling
images for printing, and managing raster page streams. It is used by
the CUPS image file filters, the PostScript RIP, and all raster
printers drivers.

%package config
Summary:        CUPS library configuration files
Group:          Hardware/Printing
%if 0%{?suse_version} >= 1330
Requires(pre):	user(lp)
Requires(pre):	group(lp)
%endif

%description config
CUPS is a modular printing system which allows a computer to act as a
print server.

This subpackage contains some basic configuration files for its
operation.

%package client
Summary:        CUPS Client Programs
# Require the exact matching version-release of the libcups* sub-packages because
# non-matching CUPS libraries may let CUPS software crash (e.g. segfault)
# because all CUPS software is provided as one single CUPS source tarball
# and there are CUPS-internal dependencies via CUPS private API calls
# (which do not happen for third-party software which uses only the CUPS public API).
# The exact matching version-release of each libcups* sub-package is available
# on the same package repository where the cups package is because
# all are built simultaneously from the same cups source package
# and all required packages are provided on the same repository:
Group:          Hardware/Printing
Requires:       libcups2 = %{version}-%{release}
Requires:       libcupsimage2 = %{version}-%{release}
# Conflicts with other print spoolers which provide same binaries like /usr/bin/lp and so on:
Conflicts:      lprng
Conflicts:      lprold
Conflicts:      plp

%description client
CUPS is a modular printing system which allows a computer to act as a
print server. A computer running CUPS is a host that can accept print
jobs from client computers, process them, and send them to the
appropriate printer.

This package contains the traditional command line interfaces for the
System V and Berkeley print systems.

%package devel
Summary:        Development Environment for CUPS
# Do not require the exact matching version-release
# of the native CUPS libraries (i.e. the libcups* sub-packages)
# but only CUPS libraries with matching version because
# for building third-party software which uses only the CUPS public API
# there are no CUPS-internal dependencies via CUPS private API calls
# (the latter would require the exact matching CUPS libraries version-release):
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcups2 = %{version}
Requires:       libcupsimage2 = %{version}
# make sure printer drivers benefit from automatic provides
%if 0%{?suse_version} >= 1500
Requires:       cups-rpm-helper
%endif

%description devel
CUPS is a modular printing system which allows a computer to act as a
print server.

This subpackage contains the header files for developing applications
that want to make use of libcups for adding print support.

%package ddk
Summary:        CUPS Driver Development Kit
Group:          Hardware/Printing
Requires:       cups = %{version}
Requires:       cups-devel = %{version}
# Since CUPS 1.4 the CUPS Driver Development Kit (DDK) is bundled with CUPS.
# For CUPS 1.2.x and 1.3.x, the DDK was separated software
# which we provided (up to openSUSE 11.1 / SLE11) in our cupsddk package:
Provides:       cupsddk = %{version}
Obsoletes:      cupsddk < %{version}

%description ddk
The CUPS Driver Development Kit (DDK) provides
a suite of standard drivers, a PPD file compiler,
and other utilities that can be used to develop
printer drivers for CUPS.

%prep
%setup -q
# Patch0...Patch9 is for patches from upstream:
# Patch10...Patch99 is for patches from SUSE which are intended for upstream:
# Patch10 cups-2.1.0-choose-uri-template.patch adds 'smb://...' URIs to templates/choose-uri.tmpl:
%patch10 -b choose-uri-template.orig
# Patch11 cups-2.1.0-default-webcontent-path.patch changes the default path whereto the
# web content is installed from /usr/share/doc/cups to /usr/share/cups/webcontent
# because the files of the CUPS web content are no documentation, see CUPS STR #3578
# and http://bugzilla.novell.com/show_bug.cgi?id=546023#c6 and subsequent comments:
%patch11 -b default-webcontent-path.orig
# Patch12 cups-2.1.0-cups-systemd-socket.patch Use systemd socket activation properly:
#patch12 -b cups-systemd-socket.orig
# Patch42 Let cupsd start after possible network connection (boo#1111351)
%patch42 -p0
# Patch100...Patch999 is for private patches from SUSE which are not intended for upstream:
# Patch100 cups-pam.diff adds conf/pam.suse regarding support for PAM for SUSE:
%patch100 -b cups-pam.orig
# Patch101 cups-2.0.3-additional_policies.patch adds the 'allowallforanybody' policy to cupsd.conf
# see https://fate.novell.com/303515 and https://bugzilla.suse.com/show_bug.cgi?id=936309
%patch101 -b additional_policies.orig
# Patch103 cups-1.4-do_not_strip_recommended_from_PPDs.patch
# reverts the change which was added by Michael Sweet in Jan 2007
# which strips the word "recommended" from NickName in PPDs because
# at least yast2-printer in SUSE needs it, compare the
# 'Why not "recommend" PPDs in the NickName?' and the subsequent
# 'RFC: New Driver Rating/Information Attributes' mail thread on cups@easysw.com:
%patch103 -b do_not_strip_recommended_from_PPDs.orig
# Patch104 cups-config-libs.patch fixes option --libs in cups-config script:
%patch104 -b cups-config-libs.orig

%build
# Remove ".SILENT" rule for verbose build output
sed 's#^.SILENT:##g' -i Makedefs.in
aclocal -I config-scripts
autoconf -I config-scripts
# Export the build options we desire
export CXXFLAGS="$CXXFLAGS %{optflags} -O2 -fstack-protector -fPIE -fPIC"
export CFLAGS="$CFLAGS %{optflags} -fstack-protector -fPIE -fPIC"
export LDFLAGS="-pie"
export CXX=c++
export CC=cc
# As long as cups-2.1.0-default-webcontent-path.patch is applied
# configure --with-docdir=... would be no longer needed
# because cups-2.1.0-default-webcontent-path.patch changes the
# default with-docdir path whereto the web content is installed
# from /usr/share/doc/cups to /usr/share/cups/webcontent because the
# files of the CUPS web content are no documentation, see CUPS STR #3578
# and http://bugzilla.novell.com/show_bug.cgi?id=546023#c6 and subsequent comments
# so that the new default could be used as is but upstream may accept
# cups-2.1.0-default-webcontent-path.patch in general but change its default
# so that with-docdir is explicitly set here to be future proof.
# Regarding --with-rundir and --with-domainsocket
# see https://www.cups.org/str.php?L4306 and
# http://lists.opensuse.org/opensuse-factory/2013-01/msg00578.html
# --without-perl/php - neither actually work correctly so rather disable
# --without-xinetd - socket activation from systemd works better
# --enable-debug - avoids stripping of binaries
# --enable-relro - force relro sections in binaries/libs
%configure \
        --enable-option-checking \
        --with-docdir=%{_datadir}/cups/webcontent \
        --with-cups-user=lp \
        --with-cups-group=lp \
        --with-system-groups=root \
        --enable-debug \
        --enable-debug-printfs \
        --enable-relro \
        --enable-gssapi \
        --enable-libusb \
        --disable-static \
        --without-rcdir \
        --with-cachedir=%{_localstatedir}/cache/cups \
        --with-rundir=/run/cups \
        --with-domainsocket=/run/cups/cups.sock \
        --enable-dbus \
        --enable-pam \
        --enable-threads \
        --enable-gnutls \
        --enable-systemd \
        --enable-avahi --disable-dnssd \
        --enable-libpaper \
        --without-perl \
        --without-php \
        --with-xinetd=no \
        --enable-webif \
        localedir=%{_datadir}/locale
make %{?_smp_mflags}

%install
make BUILDROOT=%{buildroot} install
# Make directory for ssl files:
mkdir -p %{buildroot}%{_sysconfdir}/cups/ssl
# Add a client.conf as template (Source108: cups-client.conf):
install -m644 %{SOURCE108} %{buildroot}%{_sysconfdir}/cups/client.conf
# Make the libraries accessible also via generic named links:
ln -sf libcupsimage.so.2 %{buildroot}%{_libdir}/libcupsimage.so
ln -sf libcups.so.2 %{buildroot}%{_libdir}/libcups.so
# Add missing usual directories:
install -d -m755 %{buildroot}%{_datadir}/cups/drivers
install -d -m755 %{buildroot}%{_localstatedir}/cache/cups
# Add conf/pam.suse regarding support for PAM (see Patch100: cups-pam.diff):
install -m 644 -D conf/pam.suse %{buildroot}%{_sysconfdir}/pam.d/cups
# Add missing usual documentation.
install -d -m755 %{buildroot}/%{_defaultdocdir}/cups
for f in CHANGES.md CREDITS.md INSTALL.md LICENSE README.md
do install -m 644 "$f" %{buildroot}%{_defaultdocdir}/cups/
done
# Add generic PostScript printer PPDs:
# Source102: Postscript.ppd.gz
install -m 644 %{SOURCE102} %{buildroot}%{_datadir}/cups/model/Postscript.ppd.gz
# Source105: Postscript-level1.ppd,gz
install -m 644 %{SOURCE105} %{buildroot}%{_datadir}/cups/model/Postscript-level1.ppd.gz
# Source106: Postscript-level2.ppd.gz
install -m 644 %{SOURCE106} %{buildroot}%{_datadir}/cups/model/Postscript-level2.ppd.gz
# Rm files for desktop menu:
rm -f %{buildroot}%{_datadir}/applications/cups.desktop
rm -rf %{buildroot}%{_datadir}/icons
# Save /etc/cups/cupsd.conf and /etc/cups/cupsd.conf.default from becoming hardlinked
# via the fdupes run below, see https://bugzilla.novell.com/show_bug.cgi?id=773971
# by making their content different and at the same time fix the misleading comment.
# Intentionally let the build fail if 'grep' does not find what 'sed' should change
# because if upstream changed it 'sed' would silently no longer change the files:
grep -q '^# Configuration ' %{buildroot}/%{_sysconfdir}/cups/cupsd.conf.default
sed -i -e 's/^# Configuration /# Default configuration /' %{buildroot}/%{_sysconfdir}/cups/cupsd.conf.default
# Install the systemd control files:
mv %{buildroot}%{_unitdir}/org.cups.cupsd.path %{buildroot}%{_unitdir}/cups.path
mv %{buildroot}%{_unitdir}/org.cups.cupsd.service %{buildroot}%{_unitdir}/cups.service
mv %{buildroot}%{_unitdir}/org.cups.cupsd.socket %{buildroot}%{_unitdir}/cups.socket
mv %{buildroot}%{_unitdir}/org.cups.cups-lpd.socket %{buildroot}%{_unitdir}/cups-lpd.socket
mv %{buildroot}%{_unitdir}/org.cups.cups-lpd@.service %{buildroot}%{_unitdir}/cups-lpd@.service
sed -i -e "s,org.cups.cupsd,cups,g" %{buildroot}%{_unitdir}/cups.service
# rcbla aliases:
ln -s service %{buildroot}%{_sbindir}/rccups
ln -s service %{buildroot}%{_sbindir}/rccups-lpd
# Install /usr/lib/tmpfiles.d/cups.conf
# According to
# https://developers.redhat.com/blog/2016/09/20/managing-temporary-files-with-systemd-tmpfiles-on-rhel7/
#   d /var/spool/cups/tmp - - - 30d
# results that each file older than 30 days on /var/spool/cups/tmp will be deleted where a file
# will be considered unused only if atime, mtime and ctime are all older than the specified time.
# We use group 'root' for /run/cups/certs (instead of 'sys')
#   d /run/cups/certs 0511 lp root -
# because of https://bugzilla.opensuse.org/show_bug.cgi?id=1042916
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/cups.conf <<EOF
# See tmpfiles.d(5) for details
# Type(d=directory) Path Mode UID GID Age(until delete when cleaning)
d /run/cups 0755 root lp -
d /run/cups/certs 0511 lp root -
d %{_localstatedir}/spool/cups/tmp - - - 30d
EOF
# Never run fdupes carelessly over the whole buildroot directory
# because in older openSUSE and SLE11 versions fdupes
# links files with different owner, group, or permissions
# see https://bugzilla.novell.com/show_bug.cgi?id=784670
# and even in current openSUSE versions fdupes links across sub-package
# boundaries, compare https://bugzilla.novell.com/show_bug.cgi?id=784869
%fdupes -s %{buildroot}/%{_datadir}/cups/templates

%pre -p /bin/bash
getent group ntadmin >/dev/null || %{_sbindir}/groupadd -g 71 -o -r ntadmin
%service_add_pre cups.service cups-lpd.socket cups.socket

%post -p /bin/bash
%service_add_post cups.service cups-lpd.socket cups.socket
# Use %%tmpfiles_create when 13.2 is oldest in support scope
/usr/bin/systemd-tmpfiles --create %{_tmpfilesdir}/cups.conf || :

%preun -p /bin/bash
%service_del_preun cups.service cups-lpd.socket cups.socket

%postun -p /bin/bash
%service_del_postun cups.service cups-lpd.socket cups.socket

%posttrans -p /bin/bash
# Use a real bash script with an explicit "exit 0" at the end to be by default fail safe
# an explicit "exit 1" must be use to enforce package install/upgrade/erase failure where needed
# see the "Shared_libraries" section in http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Begin refresh systemd units and clean up possibly obsolete systemd units
# The following is a generic way how to refresh and/or clean up systemd units.
# A systemd unit may need a refresh after updating a package when the new package
# had installed a changed systemd unit file for an enabled systemd unit.
# A systemd unit may become obsolete by updating a package (see bnc#904215).
# A systemd unit is considered to have become obsolete when the systemd
# symlink /etc/systemd/system/.../unit_name -> /path/to/unit_file is broken.
# When during package update the new package does no longer provide a unit file
# then the systemd symlink becomes broken after the files of the old package
# had been actually removed by RPM.
# According to /usr/share/doc/packages/rpm/manual/triggers and according
# to https://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets#Scriptlet_Ordering
# and http://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Scriptlet_Ordering
# from the new package only "posttrans of new package" is run after "removal of old package"
# so that the new package must do the clean up as RPM posttrans scriptlet.
for u in cups.service cups.socket cups.path; do
   if systemctl --quiet is-enabled $u 2>/dev/null
   then # Refresh still valid enabled systemd units and clean up possibly obsoleted systemd units:
        # Enforce systemd to use the current unit file which is usually the unit file of the new package
        # but also in case of custom units (that use other unit files) a "reenable" won't hurt because
        # "reenable" does not implicitly stop a running service which is "the right thing" because
        # a RPM package installation must not automatically disrupt (restart) a running service.
        # Using "--force reenable" is essential to clean up possibly conflicting/broken symlinks.
        # (without "|| :" build fails with "Failed to get D-Bus connection: No connection to service manager. posttrans script ... failed"):
        systemctl --quiet --force reenable $u 2>/dev/null || :
   else # Refresh still valid disabled systemd units and clean up possibly obsoleted systemd units:
        # First using "--force reenable" is essential to clean up possibly conflicting/broken symlinks
        # because there is no "--force disable" that would clean up possibly conflicting/broken symlinks
        # see https://bugzilla.opensuse.org/show_bug.cgi?id=904215#c34
        # so that first the unit has a clean state and then it is set back to disabled (as it was before).
        # If a disabled systemd unit has become obsoleted, "systemctl --force reenable" will clean it up
        # which means the unit gets removed and the subsequent "systemctl disable" will do nothing.
        # (without "|| :" build fails with "Failed to get D-Bus connection: No connection to service manager. posttrans script ... failed"):
        systemctl --quiet --force reenable $u 2>/dev/null || :
        systemctl --quiet disable $u 2>/dev/null || :
   fi
done
exit 0

%post   -n libcups2 -p /sbin/ldconfig
%postun -n libcups2 -p /sbin/ldconfig
%post   -n libcupsimage2 -p /sbin/ldconfig
%postun -n libcupsimage2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
# In particular all executables are listed explicitly.
# This avoids that CUPS' configure magic might silently
# not build and install an executable when whatever condition
# for configure's automated tests is not fulfilled in the build system.
# See https://bugzilla.novell.com/show_bug.cgi?id=526847#c9
%config(noreplace) %attr(640,root,lp) %{_sysconfdir}/cups/cups-files.conf
%config(noreplace) %attr(640,root,lp) %{_sysconfdir}/cups/cupsd.conf
%config(noreplace) %attr(640,root,lp) %{_sysconfdir}/cups/snmp.conf
%config %{_sysconfdir}/pam.d/cups
%config %{_sysconfdir}/dbus-1/system.d/cups.conf
%config %{_sysconfdir}/cups/cupsd.conf.default
%config %{_sysconfdir}/cups/cups-files.conf.default
%config %{_sysconfdir}/cups/snmp.conf.default
%dir %attr(755,root,lp) %{_sysconfdir}/cups/ppd
%dir %attr(700,root,lp) %{_sysconfdir}/cups/ssl
%{_unitdir}/cups.service
%{_unitdir}/cups.socket
%{_unitdir}/cups.path
%{_unitdir}/cups-lpd.socket
%{_unitdir}/cups-lpd@.service
%{_tmpfilesdir}/cups.conf
%{_bindir}/cupstestppd
%{_sbindir}/cupsctl
%{_sbindir}/cupsd
%{_sbindir}/cupsfilter
%{_sbindir}/rccups
%{_sbindir}/rccups-lpd
%dir /usr/lib/cups
%dir /usr/lib/cups/backend
/usr/lib/cups/backend/dnssd
/usr/lib/cups/backend/http
/usr/lib/cups/backend/https
/usr/lib/cups/backend/ipp
/usr/lib/cups/backend/ipps
/usr/lib/cups/backend/lpd
/usr/lib/cups/backend/snmp
/usr/lib/cups/backend/socket
/usr/lib/cups/backend/usb
%dir /usr/lib/cups/cgi-bin
/usr/lib/cups/cgi-bin/admin.cgi
/usr/lib/cups/cgi-bin/classes.cgi
/usr/lib/cups/cgi-bin/help.cgi
/usr/lib/cups/cgi-bin/jobs.cgi
/usr/lib/cups/cgi-bin/printers.cgi
%dir /usr/lib/cups/command
/usr/lib/cups/command/ippevepcl
/usr/lib/cups/command/ippeveps
%dir /usr/lib/cups/daemon
/usr/lib/cups/daemon/cups-deviced
/usr/lib/cups/daemon/cups-driverd
/usr/lib/cups/daemon/cups-exec
/usr/lib/cups/daemon/cups-lpd
%dir /usr/lib/cups/driver
%dir /usr/lib/cups/filter
/usr/lib/cups/filter/commandtops
/usr/lib/cups/filter/gziptoany
/usr/lib/cups/filter/pstops
/usr/lib/cups/filter/rastertoepson
/usr/lib/cups/filter/rastertohp
/usr/lib/cups/filter/rastertolabel
/usr/lib/cups/filter/rastertopwg
%dir /usr/lib/cups/monitor
/usr/lib/cups/monitor/bcp
/usr/lib/cups/monitor/tbcp
%dir /usr/lib/cups/notifier
/usr/lib/cups/notifier/dbus
/usr/lib/cups/notifier/mailto
/usr/lib/cups/notifier/rss
%dir %attr(0775,root,ntadmin) %{_datadir}/cups/drivers
%doc %{_defaultdocdir}/cups
%doc %{_mandir}/man1/cups.1.gz
%doc %{_mandir}/man1/cupstestppd.1.gz
%doc %{_mandir}/man1/ippeveprinter.1.gz
%doc %{_mandir}/man5/classes.conf.5.gz
%doc %{_mandir}/man5/client.conf.5.gz
%doc %{_mandir}/man5/cups-snmp.conf.5.gz
%doc %{_mandir}/man5/cups-files.conf.5.gz
%doc %{_mandir}/man5/cupsd-logs.5.gz
%doc %{_mandir}/man5/cupsd.conf.5.gz
%doc %{_mandir}/man5/mailto.conf.5.gz
%doc %{_mandir}/man5/mime.convs.5.gz
%doc %{_mandir}/man5/mime.types.5.gz
%doc %{_mandir}/man5/printers.conf.5.gz
%doc %{_mandir}/man5/subscriptions.conf.5.gz
%doc %{_mandir}/man7/backend.7.gz
%doc %{_mandir}/man7/filter.7.gz
%doc %{_mandir}/man7/ippevepcl.7.gz
%doc %{_mandir}/man7/ippeveps.7.gz
%doc %{_mandir}/man7/notifier.7.gz
%doc %{_mandir}/man8/cups-deviced.8.gz
%doc %{_mandir}/man8/cups-driverd.8.gz
%doc %{_mandir}/man8/cups-exec.8.gz
%doc %{_mandir}/man8/cups-lpd.8.gz
%doc %{_mandir}/man8/cups-snmp.8.gz
%doc %{_mandir}/man8/cupsctl.8.gz
%doc %{_mandir}/man8/cupsd.8.gz
%doc %{_mandir}/man8/cupsd-helper.8.gz
%doc %{_mandir}/man8/cupsfilter.8.gz
%{_datadir}/cups/
%exclude %{_datadir}/cups/ppdc/

%files client
%defattr(-,root,root)
%{_bindir}/cancel
%{_bindir}/ippeveprinter
%{_bindir}/ippfind
%{_bindir}/ipptool
%{_bindir}/lp
%{_bindir}/lpoptions
%{_bindir}/lpq
%{_bindir}/lpr
%{_bindir}/lprm
%{_bindir}/lpstat
%{_sbindir}/cupsaccept
%{_sbindir}/cupsdisable
%{_sbindir}/cupsenable
%{_sbindir}/cupsreject
%{_sbindir}/lpadmin
%{_sbindir}/lpc
%{_sbindir}/lpinfo
%{_sbindir}/lpmove
%doc %{_mandir}/man1/cancel.1.gz
%doc %{_mandir}/man1/ippfind.1.gz
%doc %{_mandir}/man1/ipptool.1.gz
%doc %{_mandir}/man1/lp.1.gz
%doc %{_mandir}/man1/lpoptions.1.gz
%doc %{_mandir}/man1/lpq.1.gz
%doc %{_mandir}/man1/lpr.1.gz
%doc %{_mandir}/man1/lprm.1.gz
%doc %{_mandir}/man1/lpstat.1.gz
%doc %{_mandir}/man5/ipptoolfile.5.gz
%doc %{_mandir}/man8/cupsaccept.8.gz
%doc %{_mandir}/man8/cupsdisable.8.gz
%doc %{_mandir}/man8/cupsenable.8.gz
%doc %{_mandir}/man8/cupsreject.8.gz
%doc %{_mandir}/man8/lpadmin.8.gz
%doc %{_mandir}/man8/lpc.8.gz
%doc %{_mandir}/man8/lpinfo.8.gz
%doc %{_mandir}/man8/lpmove.8.gz

%files devel
%defattr(-,root,root)
%{_includedir}/cups/
%{_libdir}/libcups.so
%{_libdir}/libcupsimage.so
%{_datadir}/cups/ppdc/

%files ddk
%defattr(-,root,root)
%{_bindir}/ppdc
%{_bindir}/ppdhtml
%{_bindir}/ppdi
%{_bindir}/ppdmerge
%{_bindir}/ppdpo
%doc %{_mandir}/man1/ppdc.1.gz
%doc %{_mandir}/man1/ppdhtml.1.gz
%doc %{_mandir}/man1/ppdi.1.gz
%doc %{_mandir}/man1/ppdmerge.1.gz
%doc %{_mandir}/man1/ppdpo.1.gz
%doc %{_mandir}/man5/ppdcfile.5.gz

%files -n libcups2
%defattr(-,root,root)
%{_libdir}/libcups.so.2

%files -n libcupsimage2
%defattr(-,root,root)
%{_libdir}/libcupsimage.so.2

%files config
%defattr(-,root,root)
%if 0%{?suse_version} >= 1330
%dir %attr(0755,root,lp) /etc/cups
%endif
%config(noreplace) %{_sysconfdir}/cups/client.conf
%dir %attr(0710,root,lp) %{_var}/spool/cups
%dir %attr(1770,root,lp) %{_var}/spool/cups/tmp
%dir %attr(0755,lp,lp) %{_var}/log/cups/
%dir %attr(0775,lp,lp) %{_var}/cache/cups
%{_bindir}/cups-config
%{_datadir}/locale/*/cups_*
%doc %{_mandir}/man1/cups-config.1.gz

%changelog
