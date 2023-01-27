#
# spec file for package remmina
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?is_opensuse}
%bcond_without  remmina_kwallet
%else
%bcond_with     remmina_kwallet
%endif
Name:           remmina
Version:        1.4.29
Release:        0
Summary:        Versatile Remote Desktop Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://www.remmina.org/
Source0:        https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-v%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libsodium-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp2) >= 2.1.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gvnc-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsecret-1)
%if 0%{?sle_version} && 0%{?sle_version} <= 150500
BuildRequires:  pkgconfig(libsoup-2.4)
%else
BuildRequires:  pkgconfig(libsoup-3.0)
%endif
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(spice-client-gtk-3.0)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(winpr2)
BuildRequires:  pkgconfig(xkbfile)
Recommends:     %{name}-plugin-rdp
Recommends:     %{name}-plugin-secret
Recommends:     %{name}-plugin-vnc
Provides:       %{name}-plugins-common = %{version}
Obsoletes:      %{name}-plugins-common < 1.0.0
%if %{with remmina_kwallet}
BuildRequires:  cmake(KF5Wallet)
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(wayland-client)
%endif

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travellers, who need to work with lots of remote
computers in front of either large monitors or tiny netbooks. Remmina supports
multiple network protocols such as RDP, VNC, NX, XDMCP and SSH via separate
plugins in an integrated and consistant user interface.

%package kiosk
Summary:        Login manager extension for a Remmina kiosk mode
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description kiosk
This package installs a Remmina Kiosk mode to the list of the
available sessions for all freedesktop compliant login managers.

%package devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains header files needed for developing plugins for
Remmina.

%package plugin-exec
Summary:        Plugin for Remmina to allow execution of local commands
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-exec
This package provides a plugin for Remmina allowing the execution of
local commands.

%package plugin-python-wrapper
Summary:        Adapter for remmina Python plugins
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-python-wrapper
This package provides an adapter used by remmina Python plugins

%package plugin-spice
Summary:        SPICE Protocol Plugin for Remmina
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-spice
This package provides the SPICE protocol plugin for Remmina.

%if %{with remmina_kwallet}
%package plugin-kwallet
Summary:        Remmina plugin to support the KDE Wallet
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-kwallet
KDE Wallet plugin, that can be used instead of the GNOME Keyring
%endif

%package plugin-rdp
Summary:        RDP Protocol Plugin for Remmina
Group:          Productivity/Networking/Other
Requires:       freerdp
Requires:       remmina = %{version}

%description plugin-rdp
This package provides the RDP protocol plugin for Remmina.

%package plugin-vnc
Summary:        VNC Protocol Plugin for Remmina
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-vnc
This package provides the RDP protocol plugin for Remmina.

%package plugin-gvnc
Summary:        VNC Protocol Plugin for Remmina via GTK+ widget
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-gvnc
This package provides the RDP protocol plugin for Remmina using the
VNC viewer widget for GTK+.

%package plugin-www
Summary:        WWW Protocol Plugin for Remmina
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}

%description plugin-www
This package provides the a plugin for Remmina which allows to login and
to browse a page.

%package plugin-secret
Summary:        Gnome Keyring Pasword Manager Plugin for Remmina
Group:          Productivity/Networking/Other
Requires:       remmina = %{version}
Provides:       remmina-plugins-gnome = %{version}
Obsoletes:      remmina-plugins-gnome < %{version}

%description plugin-secret
This package provides a Remmina plugin for the GNOME keyring password manager.

%lang_package

%prep
%setup -q -n Remmina-v%{version}
%autopatch -p1
sed -e 's|%{_bindir}/env bash|%{_bindir}/sh|' -i data/desktop/remmina-file-wrapper.in

%build
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE -pie"
%ifarch aarch64
export CFLAGS="$CFLAGS -fPIC"
%endif

%cmake \
	-DCMAKE_SKIP_RPATH=ON \
	-DWITH_NEWS=OFF \
	-DWITH_KIOSK_SESSION=ON \
	-DWITH_GVNC=ON \
%if %{with remmina_kwallet}
	-DWITH_KF5WALLET=ON \
%else
	-DWITH_KF5WALLET=OFF \
%endif
	-DWITH_APPINDICATOR=ON \
	%{nil}

%cmake_build

%install
%cmake_install

%suse_update_desktop_file org.remmina.Remmina Network RemoteAccess GTK

%fdupes %{buildroot}%{_datadir}/remmina
%fdupes %{buildroot}%{_datadir}/icons

%find_lang %{name}

%files
%license LICENSE LICENSE.OpenSSL
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-file-wrapper
%{_datadir}/applications/org.remmina.Remmina-file.desktop
%{_datadir}/applications/org.remmina.Remmina.desktop
%dir %{_datadir}/icons/hicolor/apps
%{_datadir}/icons/hicolor/apps/*
%{_datadir}/icons/hicolor/**/**/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.remmina.Remmina.appdata.xml
%{_datadir}/mime/packages/%{name}-mime.xml
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-file-wrapper.1%{?ext_man}

%files kiosk
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_datadir}/gnome-session/sessions/remmina-gnome.session
%{_bindir}/gnome-session-remmina
%{_bindir}/remmina-gnome
%{_mandir}/man1/gnome-session-remmina.1%{?ext_man}
%{_mandir}/man1/remmina-gnome.1%{?ext_man}
%{_datadir}/xsessions/remmina-gnome.desktop
%{_datadir}/applications/%{name}-gnome.desktop

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files plugin-exec
%{_libdir}/remmina/plugins/remmina-plugin-exec.so

%files plugin-python-wrapper
%{_libdir}/remmina/plugins/remmina-plugin-python_wrapper.so

%files plugin-spice
%{_libdir}/remmina/plugins/remmina-plugin-spice.so

%if %{with remmina_kwallet}
%files plugin-kwallet
%{_libdir}/remmina/plugins/remmina-plugin-kwallet.so
%endif

%files plugin-rdp
%{_libdir}/remmina/plugins/remmina-plugin-rdp.so

%files plugin-vnc
%{_libdir}/remmina/plugins/remmina-plugin-vnc.so

%files plugin-gvnc
%{_libdir}/remmina/plugins/remmina-plugin-gvnc.so

%files plugin-www
%{_libdir}/remmina/plugins/remmina-plugin-www.so

%files plugin-secret
%{_libdir}/remmina/plugins/remmina-plugin-secret.so

%changelog
