#
# spec file for package rtkit
#
# Copyright (c) 2025 SUSE LLC
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
Version:        0.13
Release:        0
Summary:        Realtime Policy and Watchdog Daemon
# The daemon itself is GPL v3 or later, the reference implementation for
# the client BSD-3-Clause
License:        BSD-3-Clause AND GPL-3.0-or-later
Group:          System/Base
URL:            https://github.com/heftig/rtkit
Source:         https://github.com/heftig/rtkit/releases/download/v%{version}/rtkit-%{version}.tar.xz
Source1:        rtkit.sysusers
Patch0:         harden_rtkit-daemon.service.patch
Patch1:         rtkit-silent-debug-messages-by-default.patch
BuildRequires:  automake
BuildRequires:  libcap-devel
BuildRequires:  pkg-config
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
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE1} rtkit rtkit.conf
autoreconf -fiv
export CFLAGS="%{optflags} -fPIE -Wno-format-nonliteral -Wno-format-security"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
%configure \
  --disable-silent-rules \
  --with-systemdsystemunitdir=%{_unitdir} \
  --libexecdir=%{_libexecdir}/rtkit

make %{?_smp_mflags}
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%if 0%{?suse_version} < 1600
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcrtkit-daemon
%endif
install -D -m 0644 org.freedesktop.RealtimeKit1.xml %{buildroot}/%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/rtkit.conf

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
%defattr(0644,root,root,0755)
%license GPL LICENSE
%doc README rtkit.c rtkit.h
%attr(0755,root,root) %{_sbindir}/rtkitctl
%dir %{_libexecdir}/rtkit
%dir %{_libexecdir}/rtkit/installed-tests
%dir %{_libexecdir}/rtkit/installed-tests/rtkit
%attr(0755,root,root) %{_libexecdir}/rtkit/rtkit-daemon
%{_libexecdir}/rtkit/installed-tests/rtkit/rtkit-test
%{_datadir}/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%{_datadir}/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%{_mandir}/man8/rtkitctl.8%{ext_man}
%if 0%{?suse_version} < 1600
%{_sbindir}/rcrtkit-daemon
%endif
%{_unitdir}/rtkit-daemon.service
%{_sysusersdir}/rtkit.conf

%changelog
