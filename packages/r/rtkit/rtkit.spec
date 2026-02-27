#
# spec file for package rtkit
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           rtkit
Version:        0.14
Release:        0
Summary:        Realtime Policy and Watchdog Daemon
# The daemon itself is GPL v3 or later, the reference implementation for
# the client is MIT.
License:        GPL-3.0-or-later AND MIT
Group:          System/Base
URL:            https://gitlab.freedesktop.org/pipewire/rtkit
Source:         https://gitlab.freedesktop.org/pipewire/rtkit/-/archive/v%{version}/rtkit-v%{version}.tar.bz2
Source1:        rtkit.sysusers
Patch0:         harden_rtkit-daemon.service.patch
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  vim
BuildRequires:  xz
BuildRequires:  pkgconfig(dbus-1) >= 1.2
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
Requires:       polkit
Requires(pre):  dbus-1
%sysusers_requires

%description
RealtimeKit is a D-Bus system service that changes the scheduling policy of
user processes/threads to SCHED_RR (i.e. realtime scheduling mode) on
request. It is intended to be used as a secure mechanism to allow real-time
scheduling to be used by normal user processes.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%sysusers_generate_pre %{SOURCE1} rtkit rtkit.conf
export CFLAGS="%{optflags} -fPIE -Wno-format-nonliteral -Wno-format-security"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
%meson \
  --libexecdir=%{_libexecdir}/rtkit   \
  -Dsystemd_systemunitdir=%{_unitdir}

%meson_build
%{_host}/rtkit-daemon --introspect >org.freedesktop.RealtimeKit1.xml

%install
%meson_install
%if 0%{?suse_version} < 1600
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcrtkit-daemon
%endif
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/rtkit.conf

%check
%meson_test

%preun
%service_del_preun rtkit-daemon.service

%pre -f rtkit.pre
%service_add_pre rtkit-daemon.service

%post
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :
%service_add_post rtkit-daemon.service

%postun
%service_del_postun rtkit-daemon.service

%files
%license GPL LICENSE
%doc README rtkit.c rtkit.h
%{_sbindir}/rtkitctl
%{_libexecdir}/rtkit/
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%{_datadir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%{_mandir}/man8/rtkitctl.8%{?ext_man}
%if 0%{?suse_version} < 1600
%{_sbindir}/rcrtkit-daemon
%endif
%{_unitdir}/rtkit-daemon.service
%{_sysusersdir}/rtkit.conf

%changelog
