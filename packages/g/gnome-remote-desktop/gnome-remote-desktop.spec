#
# spec file for package gnome-remote-desktop
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


%global systemd_unit       gnome-remote-desktop.service gnome-remote-desktop-configuration.service
%define freerdp_version    3.15.0
%define glib_version       2.75.0
%define gstreamer_version  1.10.0
%define polkit_req >= 122

Name:           gnome-remote-desktop
Version:        49.3
Release:        0
Summary:        GNOME Remote Desktop screen sharing service
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://gitlab.gnome.org/GNOME/gnome-remote-desktop
Source0:        %{name}-%{version}.tar.zst
# PATCH-FIX-UPSTREAM 0001-control-Allow-controlling-all-daemon-types.patch bsc#1244053 mgorse@suse.com -- allow controlling all daemon types.
Patch0:         0001-control-Allow-controlling-all-daemon-types.patch
# PATCH-FIX-UPSTREAM 0002-daemon-Use-GError-auto-pointer.patch bsc#1244053 mgorse@suse.com -- daemon: Use GError auto-pointer.
Patch1:         0002-daemon-Use-GError-auto-pointer.patch
# PATCH-FIX-UPSTREAM 0004-rdp-sam-Dup-fd-kept-in-struct.patch bsc#1244053 mgorse@suse.com -- rdp-sam: Dup fd kept in struct.
Patch2:         0004-rdp-sam-Dup-fd-kept-in-struct.patch
# PATCH-FIX-UPSTREAM 0005-rdp-server-Set-socket-backlog-count-to-5.patch bsc#1244053 mgorse@suse.com -- rdp-server: Set socket backlog count to 5.
Patch3:         0005-rdp-server-Set-socket-backlog-count-to-5.patch
# PATCH-FIX-UPSTREAM 0006-utils-Add-some-time-conversion-helpers.patch bsc#1244053 mgorse@suse.com -- add some time conversion helpers.
Patch4:         0006-utils-Add-some-time-conversion-helpers.patch
# PATCH-FIX-UPSTREAM 0007-utils-Add-helper-to-close-connection-and-notify.patch bsc#1244053 mgorse@suse.com -- add helper to close connection and notify.
Patch5:         0007-utils-Add-helper-to-close-connection-and-notify.patch
# PATCH-FIX-UPSTREAM 0008-Introduce-throttler-class.patch bsc#1244053 mgorse@suse.com -- introduce throttler class.
Patch6:         0008-Introduce-throttler-class.patch
# PATCH-FIX-UPSTREAM 0009-rdp-server-Throttle-connections-using-GrdThrottler.patch bsc#1244053 mgorse@suse.com -- throttle connections using GrdThrottler.
Patch7:         0009-rdp-server-Throttle-connections-using-GrdThrottler.patch
# PATCH-FIX-UPSTREAM 0010-throttler-Introduce-limits-struct.patch bsc#1244053 mgorse@suse.com -- introduce limits struct.
Patch8:         0010-throttler-Introduce-limits-struct.patch
# PATCH-FIX-UPSTREAM 0011-vnc-server-Hook-up-VNC-server-to-the-throttler.patch bsc#1244053 mgorse@suse.com -- hook up VNC server to the throttler.
Patch9:         0011-vnc-server-Hook-up-VNC-server-to-the-throttler.patch
# PATCH-FIX-UPSTREAM 0013-throttler-Allow-overriding-hard-coded-parallel-conne.patch bsc#1244053 mgorse@suse.com -- allow overriding hard coded parallel connections limit.
Patch10:        0013-throttler-Allow-overriding-hard-coded-parallel-conne.patch

%if 0%{?sle_version} && 0%{?sle_version} < 160000
BuildRequires:  gcc13
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%endif
BuildRequires:  /usr/bin/dbus-run-session
BuildRequires:  asciidoc
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  spirv-tools
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.0
BuildRequires:  pkgconfig(freerdp-client3) >= %{freerdp_version}
BuildRequires:  pkgconfig(freerdp-server3) >= %{freerdp_version}
BuildRequires:  pkgconfig(freerdp3) >= %{freerdp_version}
BuildRequires:  pkgconfig(fuse3) >= 3.9.1
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libei-1.0) >= 1.3.901
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libvncclient)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libvncserver) >= 0.9.10
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(polkit-gobject-1) %polkit_req
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-tctildr)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(winpr3) >= %{freerdp_version}
BuildRequires:  pkgconfig(xkbcommon) >= 1.0.0
%{?systemd_ordering}
%sysusers_requires

Requires:       fuse3 >= 3.9.1
Requires:       pipewire >= 0.3.0

%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?sle_version} && 0%{?sle_version} < 160000
export CC=gcc-13
%endif
%meson \
	-D vnc=true \
	-D tests=false \
	%{nil}
%meson_build
%sysusers_generate_pre %{_vpath_builddir}/data/gnome-remote-desktop-sysusers.conf gnome-remote-desktop gnome-remote-desktop-sysusers.conf

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%pre -f gnome-remote-desktop.pre
%service_add_pre %{systemd_unit}

%post
%tmpfiles_create %{_tmpfilesdir}/gnome-remote-desktop-tmpfiles.conf
%service_add_post %{systemd_unit}
%systemd_user_post %{systemd_unit}

%preun
%service_del_preun %{systemd_unit}
%systemd_user_preun %{systemd_unit}

%postun
%service_del_postun %{systemd_unit}

%files
%license COPYING
%doc README.md
%{_bindir}/grdctl
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.RemoteDesktop.Handover.desktop
%{_datadir}/dbus-1/system-services/org.gnome.RemoteDesktop.Configuration.service
%{_libexecdir}/gnome-remote-desktop-configuration-daemon
%{_datadir}/dbus-1/system.d/org.gnome.RemoteDesktop.conf
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/polkit-1/actions/org.gnome.remotedesktop.configure-system-daemon.policy
%{_datadir}/polkit-1/actions/org.gnome.remotedesktop.enable-system-daemon.policy
%{_datadir}/polkit-1/rules.d/20-gnome-remote-desktop.rules
%{_libexecdir}/gnome-remote-desktop-daemon
%{_libexecdir}/gnome-remote-desktop-enable-service
%{_mandir}/man1/grdctl.1%{ext_man}
%{_sysusersdir}/gnome-remote-desktop-sysusers.conf
%{_tmpfilesdir}/gnome-remote-desktop-tmpfiles.conf
%ghost %attr(0700,gnome-remote-desktop,gnome-remote-desktop) %dir %{_localstatedir}/lib/gnome-remote-desktop
%ghost %attr(0755,gnome-remote-desktop,gnome-remote-desktop) %dir %{_sysconfdir}/gnome-remote-desktop
%ghost %attr(0644,gnome-remote-desktop,gnome-remote-desktop) %{_sysconfdir}/gnome-remote-desktop/grd.conf
%{_unitdir}/gnome-remote-desktop.service
%{_unitdir}/gnome-remote-desktop-configuration.service
%{_userunitdir}/gnome-remote-desktop-handover.service
%{_userunitdir}/gnome-remote-desktop-headless.service
%{_userunitdir}/gnome-remote-desktop.service

%files lang -f %{name}.lang

%changelog
