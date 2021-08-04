#
# spec file for package oddjob-gpupdate
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.2.0+git.3.85c13a8
Release:        0
Summary:        An oddjob helper which applies group policy objects
License:        BSD-3-Clause
URL:            https://github.com/altlinux/oddjob-gpupdate.git
Source:         %{name}-%{version}.tar.bz2
Group:          System/Servers
Requires:       oddjob

BuildRequires:  oddjob
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  xmlto
BuildRequires:  dbus-1-devel
BuildRequires:  libxml2-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel

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

mkdir -p %buildroot/%_lib/security
mv %buildroot%_libdir/security/pam_oddjob_gpupdate.so \
%buildroot/%_lib/security/
rm %buildroot%_libdir/security/pam_oddjob_gpupdate.la

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
/%_lib/security/pam_oddjob_gpupdate.so
%_mandir/*/pam_oddjob_gpupdate.*
%_mandir/*/oddjob-gpupdate.*
%_mandir/*/oddjobd-gpupdate.*
%config(noreplace) %_sysconfdir/dbus-*/system.d/oddjob-gpupdate.conf
%config(noreplace) %_sysconfdir/oddjobd.conf.d/oddjobd-gpupdate.conf

%changelog
