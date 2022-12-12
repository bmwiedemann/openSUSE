#
# spec file for package gnome-remote-desktop
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


%global systemd_unit       gnome-remote-desktop.service
%define freerdp_version    2.8.0
%define glib_version       2.68
%define gstreamer_version  1.10.0

Name:           gnome-remote-desktop
Version:        43.2
Release:        0
Summary:        GNOME Remote Desktop screen sharing service
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://gitlab.gnome.org/GNOME/gnome-remote-desktop
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  asciidoc
BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(epoxy) >= 1.4
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.0
BuildRequires:  pkgconfig(freerdp-client2) >= %{freerdp_version}
BuildRequires:  pkgconfig(freerdp-server2) >= %{freerdp_version}
BuildRequires:  pkgconfig(freerdp2) >= %{freerdp_version}
BuildRequires:  pkgconfig(fuse3) >= 3.9.1
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= %{gstreamer_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libvncclient)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libvncserver) >= 0.9.10
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-tctildr)
BuildRequires:  pkgconfig(winpr2) >= %{freerdp_version}
BuildRequires:  pkgconfig(xkbcommon) >= 1.0.0
%{?systemd_ordering}

Requires:       pipewire >= 0.3.0

%description
GNOME Remote Desktop is a remote desktop and screen sharing service for the
GNOME desktop environment.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D vnc=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%post
%systemd_user_post %{systemd_unit}

%preun
%systemd_user_preun %{systemd_unit}

%postun
%systemd_user_postun_with_restart %{systemd_unit}

%files
%license COPYING
%doc README.md
%{_bindir}/grdctl
%{_libexecdir}/gnome-remote-desktop-daemon
%{_userunitdir}/gnome-remote-desktop.service
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.remote-desktop.enums.xml
%{_datadir}/%{name}/
%{_mandir}/man1/grdctl.1%{ext_man}

%files lang -f %{name}.lang

%changelog
