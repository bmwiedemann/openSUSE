#
# spec file for package spice-vdagent
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 B1 Systems GmbH, Vohburg, Germany.
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


Name:           spice-vdagent
Version:        0.19.0
Release:        0
Summary:        Agent for Spice guests
License:        GPL-3.0-or-later
Group:          System/Daemons
Url:            http://spice-space.org/
Source:         http://spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Source1:        http://spice-space.org/download/releases/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Patch0:         spice-vdagent-var_run.patch
BuildRequires:  alsa-devel  >= 1.0.22
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libtool
BuildRequires:  spice-protocol-devel >= 0.12.8
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34
BuildRequires:  pkgconfig(udev)
Supplements:    modalias(xorg-x11-server:virtio:d00000003v*)
%{?systemd_requires}

%description
Spice agent for Linux guests offering the following features:

Features:
* Client mouse mode (no need to grab mouse by client, no mouse lag)
  this is handled by the daemon by feeding mouse events into the kernel
  via uinput. This will only work if the active X-session is running a
  spice-vdagent process so that its resolution can be determined.
* Automatic adjustment of the X-session resolution to the client resolution
* Support of copy and paste (text and images) between the active X-session
  and the client

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --with-session-info=systemd \
  --with-init-script=systemd
make %{?_smp_mflags} V=2

%install
make install DESTDIR=%{buildroot} V=2
# remove rsyslogd config
rm -rf %{buildroot}%{_sysconfdir}/rsyslog.d
# create rc symlink
ln -s  service %{buildroot}%{_sbindir}/rcspice-vdagentd

mkdir -p %{buildroot}%{_datadir}/gdm/greeter/autostart

mv %{buildroot}%{_datadir}/gdm/autostart/LoginWindow/*.desktop %{buildroot}%{_datadir}/gdm/greeter/autostart
rm -fr %{buildroot}%{_datadir}/gdm/autostart

%pre
%service_add_pre spice-vdagentd.service
%service_add_pre spice-vdagentd.socket

%post
%service_add_post spice-vdagentd.service
if [ "$1" -eq 1 ]; then
    systemctl -q enable spice-vdagentd.service || :
fi
%service_add_post spice-vdagentd.socket
%tmpfiles_create %_tmpfilesdir/spice-vdagentd.conf

%preun
%service_del_preun spice-vdagentd.service
%service_del_preun spice-vdagentd.socket

%postun
%service_del_postun spice-vdagentd.service
%service_del_postun spice-vdagentd.socket

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%license COPYING
%dir %{_libexecdir}/udev
%dir %{_libexecdir}/udev/rules.d
%ghost /run/spice-vdagentd
%{_libexecdir}/udev/rules.d/70-spice-vdagentd.rules
%{_unitdir}/spice-vdagentd.service
%{_unitdir}/spice-vdagentd.socket
%{_libexecdir}/tmpfiles.d/spice-vdagentd.conf
%{_bindir}/spice-vdagent
%{_sbindir}/spice-vdagentd
%{_sbindir}/rcspice-vdagentd
%{_sysconfdir}/xdg/autostart/spice-vdagent.desktop
# For /usr/share/gdm/autostart/LoginWindow/spice-vdagent.desktop
# We own the dir too, otherwise we must Require gdm
%{_datadir}/gdm
%{_mandir}/man1/%{name}*.1*

%changelog
