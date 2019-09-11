#
# spec file for package pam_dbus
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define         commit 1d32154
Name:           pam_dbus
Version:        0.2.1.3
Release:        0
License:        GPL-2.0+
Summary:        PAM module asking the logged in user for confirmation
Url:            http://git.nomeata.de/?p=darcs-mirror-pam-dbus.debian.git;a=summary
Group:          Productivity/Networking
Source0:        http://git.nomeata.de/?p=darcs-mirror-pam-dbus.debian.git;a=snapshot;h=1d32154;sf=tgz#/%{name}-%{version}.tar.gz
Source1:        pam_dbus.8
Source2:        pam_dbus-rpmlintrc
Patch0:         pam_dbus-0.2.1.3.dif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  dbus-1-python
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
Requires:       python
Requires:       python-base
Requires:       python-gtk
Requires:       python-notify
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This PAM module will, when being used to authenticate a
(typically remote) user, use D-Bus to ask any currently logged
in (typically local) user to accept or deny the authentication request.

%prep
test -h %{name}-%{version} || ln -sf darcs-mirror-pam-dbus.debian-%{commit} %{name}-%{version}
%setup -q -D
%patch0
sed -ri '/^PAM_MODDIR/{ s@/lib/@/%{_lib}/@p }' configure.ac
autoreconf -fis

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -vf %{buildroot}/%{_lib}/security/*.la
install -d %{buildroot}%{_mandir}/man8
install -m 0644 %{S:1} %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%doc README LICENSE
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/xdg/autostart/pam-dbus-notify.desktop
%attr(0755, root, root) /%{_lib}/security/%{name}.so
%dir %{_datadir}/%{name}/
%attr(0755, root, root) %{_datadir}/%{name}/pam-dbus-notify
%{_mandir}/man8/%{name}.8*

%changelog
