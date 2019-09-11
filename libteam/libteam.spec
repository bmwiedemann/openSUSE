#
# spec file for package libteam
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without python2
Name:           libteam
Version:        1.29
Release:        0
Summary:        Utilities for controlling 802.1AX team network device
License:        LGPL-2.1+
Group:          System/Kernel
URL:            http://libteam.org/

#Git-Clone:	https://github.com/jpirko/libteam
Source:         http://libteam.org/files/%name-%version.tar.gz
Patch1:         check_if_psr_ops_were_initialized.patch
Patch2:         start_teamd_from_usr_sbin.patch
Patch3:         ignore_ebusy_for_team_hwaddr_set.patch
Patch4:         0001-allow-send_interface-dbus.patch
BuildRequires:  doxygen
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  swig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.2.0
BuildRequires:  pkgconfig(libnl-cli-3.0) >= 3.2.0
BuildRequires:  pkgconfig(libnl-genl-3.0) >= 3.2.0
BuildRequires:  pkgconfig(libnl-route-3.0) >= 3.2.0
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif
%if 0%{?suse_version} >= 1220
BuildRequires:  systemd-rpm-macros
%endif
%define teamd_user			teamd
%define teamd_group			daemon
%define teamd_daemon_directory		/run/teamd
%define teamd_dbus_policy_directory	%_sysconfdir/dbus-1/system.d
%define teamd_dbus_policy_name		org.libteam.teamd.conf

%description
A library which is the user-space counterpart for the team network
driver, and provides an API to control them.

Linux kernel 3.3 and above offer a so-called "team" network driver -
a lightweight mechanism for bonding multiple interfaces together.
It is a userspace-driven alternative to the existing bonding driver.

%package -n libteam5
Summary:        Library for controlling 802.1AX team network device
Group:          System/Libraries

%description -n libteam5
A library which is the user-space counterpart for the team network
driver, and provides an API to control them.

Linux kernel 3.3 and above offer a so-called "team" network driver -
a lightweight mechanism for bonding multiple interfaces together.
It is a userspace-driven alternative to the existing bonding driver.

%package -n libteamdctl0
Summary:        Library for controlling the team network device daemon
Group:          System/Libraries

%description -n libteamdctl0
Linux kernel 3.3 and above offer a so-called "team" network driver -
a lightweight mechanism for bonding multiple interfaces together.
It is a userspace-driven alternative to the existing bonding driver.

%package devel
Summary:        Development files for libteam
Group:          Development/Libraries/C and C++
Requires:       libteam5 = %version
Requires:       libteamdctl0 = %version

%description devel
A library which is the user-space counterpart for the team network
driver, and provides an API to control them.

This package contains the development headers for the libteam and
libteamdctl libraries.

%package tools
Summary:        Utilities for controlling team network devices
Group:          System/Daemons

%description tools
This package contains frontends to libteam that allow changing
the (team-specific) properties of team devices.
(The general configuration of network devices can be done
through using iproute.)

Linux kernel 3.3 and above offer a so-called "team" network driver -
a lightweight mechanism for bonding multiple interfaces together.
It is a userspace-driven alternative to the existing bonding driver.

%package -n python-libteam
Summary:        Python bindings for libteam
Group:          Development/Languages/Python

%description -n python-libteam
This package should be installed if you want to develop Python
programs that will manipulate team network devices.

%prep
%autosetup -p1

%build
%configure --includedir="%_includedir/%name" --bindir="%_sbindir" \
	--disable-silent-rules --disable-static \
	--with-run-dir="%teamd_daemon_directory" \
	--with-user="%teamd_user" --with-group=%teamd_group
# Use CFLAGS= to kill -Werror
make %{?_smp_mflags} CFLAGS="%optflags"
%if %{with python2}
pushd binding/python/
python ./setup.py build
popd
%endif

%install
b="%buildroot"
%make_install
%if %{with python2}
pushd binding/python/
python ./setup.py install --root="$b" --prefix="%_prefix"
popd
%endif

rm -f "$b/%_libdir"/*.la
%if 0%{?_unitdir:1}
mkdir -p "$b/%_unitdir"
install -pm0644 teamd/redhat/systemd/*.service "$b/%_unitdir/"
%endif
mkdir -p "$b/%teamd_dbus_policy_directory/"
install -pm0644 teamd/dbus/teamd.conf "$b/%teamd_dbus_policy_directory/%teamd_dbus_policy_name"

%check
make check

%pre tools
getent group daemon >/dev/null || %_sbindir/groupadd -r %teamd_group
getent passwd %teamd_user >/dev/null || \
	%_sbindir/useradd -r -g %teamd_group -s /bin/false \
	-c "Teamd daemon user" -d %_localstatedir/lib/empty %teamd_user
%_sbindir/usermod -g %teamd_group %teamd_user 2>/dev/null
test -L %teamd_daemon_directory  || rm -rf %teamd_daemon_directory && :
%if 0%{?_unitdir:1}
%service_add_pre teamd@.service
%endif

%post tools
# reload dbus to apply new teamd's policy
systemctl reload dbus.service 2>/dev/null || :
%if 0%{?_unitdir:1}
%service_add_post teamd@.service
%endif

%preun tools
%if 0%{?_unitdir:1}
%service_del_preun teamd@.service
%endif

%postun tools
%if 0%{?_unitdir:1}
%service_del_postun teamd@.service
%endif
# reload dbus to forget teamd's policy
if [ $1 -eq 0 ]; then
        systemctl reload dbus.service 2>/dev/null || :
fi

%post   -n libteam5 -p /sbin/ldconfig
%postun -n libteam5 -p /sbin/ldconfig
%post   -n libteamdctl0 -p /sbin/ldconfig
%postun -n libteamdctl0 -p /sbin/ldconfig

%files -n libteam5
%_libdir/libteam.so.5*

%files -n libteamdctl0
%_libdir/libteamdctl.so.0*

%files devel
%_includedir/*
%_libdir/libteam.so
%_libdir/libteamdctl.so
%_libdir/pkgconfig/libteam*.pc

%files tools
%_sbindir/bond2team
%_sbindir/team*
%dir %_sysconfdir/dbus-1
%dir %teamd_dbus_policy_directory
%config %teamd_dbus_policy_directory/%teamd_dbus_policy_name
%_mandir/man1/*
%_mandir/man5/*
%_mandir/man8/*
%if 0%{?_unitdir:1}
%_unitdir
%endif

%if %{with python2}
%files -n python-libteam
%python_sitearch/*
%endif

%changelog
