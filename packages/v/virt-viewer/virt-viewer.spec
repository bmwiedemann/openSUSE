#
# spec file for package virt-viewer
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


# Enabled for Tumbleweed
%if 0%{?suse_version} >= 1550
%define with_govirt 0
%else
%define with_govirt 0
%endif

Name:           virt-viewer
Summary:        Virtual Machine Viewer
License:        GPL-2.0-or-later
Group:          System/Monitoring
Version:        11.0
Release:        0
URL:            http://www.virt-manager.org
Source:         https://releases.pagure.org/virt-viewer/virt-viewer-%{version}.tar.xz
Source1:        https://releases.pagure.org/virt-viewer/virt-viewer-%{version}.tar.xz.asc
Patch1:         001-Update-src-virt-viewer-app.c.patch
Patch2:         002-Use-less-memory.patch
Patch3:         003-Fix-ssh-tunnel-with-non-POSIX-remote-shells.patch
Patch4:         004-Add-support-for-usb-redirect-on-connect-in-vv-files.patch
Patch5:         005-session-vnc-Plug-leak-in-error-path.patch
Patch50:        netcat.patch
Patch51:        virtview-desktop.patch
Patch52:        virtview-dont-show-Domain-0.patch
Patch53:        virtview-fix-build-with-meson-0.61.patch
Patch100:       gcc-warnings-as-errors.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  bash-completion-devel
BuildRequires:  cmake
BuildRequires:  gtk-vnc-devel >= 0.3.8
BuildRequires:  intltool
%if %{with_govirt}
BuildRequires:  libgovirt-devel
%endif
BuildRequires:  libpixman-1-0-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
%if 0%{?suse_version} < 1600 || 0%{?suse_version} >= 1699
BuildRequires:  spice-gtk-devel
%endif
BuildRequires:  vte-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-vnc-2.0)
BuildRequires:  pkgconfig(libvirt) >= 1.2.8
BuildRequires:  pkgconfig(libvirt-glib-1.0) >= 1.2.8
%if %{with_govirt}
BuildRequires:  pkgconfig(rest-0.7)
%endif
# Our Runtime requirements
Requires:       netcat

%description
Virtual Machine Viewer provides a graphical console client for
connecting to virtual machines. It uses the GTK-VNC widget to provide
the display, and libvirt for looking up VNC server details.

%prep
%autosetup -p1

%if 0%{?suse_version} < 1600 || 0%{?suse_version} >= 1699
%define have_spice -Dspice=enabled
%else
%define have_spice -Dspice=disabled
%endif
%if ! %{with_govirt}
%define govirt_arg -Dovirt=disabled
%else
%define govirt_arg -Dovirt=enabled
%endif

%build
%meson \
    %{have_spice} \
    %{govirt_arg} \
    %{nil}
%meson_build

%install
%meson_install
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS
%license COPYING
%dir %{_datadir}/metainfo
%dir %{_datadir}/bash-completion/completions
%{_bindir}/%{name}
%{_bindir}/remote-viewer
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/virt-viewer.1*
%{_mandir}/man1/remote-viewer.1*
%{_datadir}/applications/remote-viewer.desktop
%{_datadir}/mime/packages/virt-viewer-mime.xml
%{_datadir}/bash-completion/completions/virt-viewer
%{_datadir}/metainfo/remote-viewer.appdata.xml

%changelog
