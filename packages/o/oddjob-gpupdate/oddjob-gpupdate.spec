#
# spec file for package oddjob-gpupdate
#
# Copyright (c) 2022 SUSE LLC
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


Name:           oddjob-gpupdate
Version:        0.2.0+git.5.ed70836
Release:        0
Summary:        An oddjob helper which applies group policy objects
License:        BSD-3-Clause
URL:            https://github.com/openSUSE/oddjob-gpupdate.git
Source:         %{name}-%{version}.tar.bz2
Group:          System/Servers
Requires:       oddjob

BuildRequires:  autoconf
BuildRequires:  dbus-1-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  oddjob
BuildRequires:  pam-devel
BuildRequires:  xmlto

%description
This package contains the oddjob helper which can be used by the
pam_oddjob_gpupdate module to apply group policy objects at login-time.

%prep
%setup

%build
autoreconf -if
%configure \
    --disable-static \
    --enable-pie \
    --enable-now \
    --with-selinux-acls \
    --with-selinux-labels
%make_build

%install
%makeinstall

%post
if test $1 -eq 1 ; then
	killall -HUP dbus-daemon 2>&1 > /dev/null
fi
if [ -f /var/lock/subsys/oddjobd ] ; then
	/bin/dbus-send --system --dest=com.redhat.oddjob /com/redhat/oddjob com.redhat.oddjob.reload
fi

%files
%doc COPYING src/gpupdatefor src/gpupdateforme
%_libexecdir/oddjob/gpupdate
%_pam_moduledir/pam_oddjob_gpupdate.so
%exclude %_pam_moduledir/pam_oddjob_gpupdate.la
%_mandir/*/pam_oddjob_gpupdate.*
%_mandir/*/oddjob-gpupdate.*
%_mandir/*/oddjobd-gpupdate.*
%config(noreplace) %_sysconfdir/dbus-*/system.d/oddjob-gpupdate.conf
%config(noreplace) %_sysconfdir/oddjobd.conf.d/oddjobd-gpupdate.conf

%changelog
