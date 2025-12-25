#
# spec file for package dino
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define libdino libdino0
%define libqlite libqlite0
%define libcryptovala libcrypto-vala0
%define libxmppvala libxmpp-vala0
%bcond_with    separated_plugins
%bcond_with    separated_libs
Name:           dino
Version:        0.5.1
Release:        0
Summary:        Modern Jabber/XMPP Client using GTK+/Vala
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/dino/dino
Source:         https://github.com/dino/dino/releases/download/v%{version}/dino-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM -- Add more emoji translations gh/dino/dino#1207
Patch0:         dino-0.4.3-emoji.patch
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libomemo-c-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c-devel
BuildRequires:  pkgconfig(gee-0.8) >= 0.10
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(nice) >= 0.1.15
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vapigen) >= 0.30
BuildRequires:  pkgconfig(webrtc-audio-processing)
Requires:       hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  libgpgmepp-devel
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gpgme-glib)
%else
BuildRequires:  gpgme-devel
%endif
%if "%{_lib}" == "lib64"
Requires:       gstreamer1(element-gtksink)()(64bit)
%else
Requires:       gstreamer1(element-gtksink)
%endif
%if %{with separated_plugins}
Recommends:     %{name}-plugin-http-upload = %{version}
Recommends:     %{name}-plugin-omemo = %{version}
Recommends:     %{name}-plugin-openpgp = %{version}
%else
Provides:       %{name}-plugin-openpgp = %{version}
Obsoletes:      %{name}-plugin-openpgp < %{version}
Provides:       %{name}-plugin-omemo = %{version}
Obsoletes:      %{name}-plugin-omemo < %{version}
Provides:       %{name}-plugin-http-upload = %{version}
Obsoletes:      %{name}-plugin-http-upload < %{version}
%endif
%if ! %{with separated_libs}
Provides:       %{libdino} = %{version}-%{release}
Obsoletes:      %{libdino} < %{version}-%{release}
Provides:       %{libqlite} = %{version}-%{release}
Obsoletes:      %{libqlite} < %{version}-%{release}
Provides:       %{libcryptovala} = %{version}-%{release}
Obsoletes:      %{libcryptovala} < %{version}-%{release}
Provides:       %{libxmppvala} = %{version}-%{release}
Obsoletes:      %{libxmppvala} < %{version}-%{release}
%endif

%description
Dino is an instant messaging client for the Jabber/XMPP network,
providing a unique and modern user experience based on the latest
technology from the GNOME project. Dino is still in early
development and has limited features, but already has basic support
for XMPP's latest encryption features. Future versions will provide
a plug-in API, so that developers can easily add new optional
features.

%package -n     %{libdino}
Summary:        Library libdino of %{name}
Group:          Productivity/Networking/Instant Messenger

%description -n %{libdino}
The package contains libraries used and provided by %{name}.

%package -n     %{libqlite}
Summary:        Library libqlite of %{name}
Group:          Productivity/Networking/Instant Messenger

%description -n %{libqlite}
The package contains libraries used and provided by %{name}.

%package -n     %{libcryptovala}
Summary:        Library libcrypto-vala of %{name}
Group:          Productivity/Networking/Instant Messenger

%description -n %{libcryptovala}
The package contains libraries used and provided by %{name}.

%package -n     %{libxmppvala}
Summary:        Library libxmpp-vala of %{name}
Group:          Productivity/Networking/Instant Messenger

%description -n %{libxmppvala}
The package contains libraries used and provided by %{name}.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/Other
%if %{with separated_libs}
Requires:       %{libcryptovala} = %{version}
Requires:       %{libdino} = %{version}
Requires:       %{libqlite} = %{version}
Requires:       %{libxmppvala} = %{version}
%else
Requires:       %{name} = %{version}
%endif

%description    devel
Contains libraries and header files for developing plugins for %{name}.

%if %{with separated_plugins}
%package        plugin-openpgp
Summary:        OpenPGP plugin for %{name}
Group:          Productivity/Networking/Instant Messenger

%description    plugin-openpgp
Contains the OpenPGP plugin for %{name}.

%package        plugin-omemo
Summary:        OMEMO plugin for %{name}
Group:          Productivity/Networking/Instant Messenger

%description    plugin-omemo
Contains the OMEMO plugin for %{name}.

%package        plugin-http-upload
Summary:        HTTP Upload plugin for %{name}
Group:          Productivity/Networking/Instant Messenger

%description    plugin-http-upload
Contains the HTTP Upload plugin for %{name}.
%endif

%prep
%autosetup -p1

%build
# gh/dino/dino/#1696
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson
%meson_build

%install
%meson_install
# desktop-file-validate %{buildroot}%{_datadir}/applications/dino.desktop

%find_lang dino
%find_lang dino-omemo
%find_lang dino-openpgp
#find_lang dino-http-files

%if 0%{?suse_version}
%post
%if ! %{with separated_libs}
/sbin/ldconfig
%endif
%icon_theme_cache_post

%postun
%if ! %{with separated_libs}
/sbin/ldconfig
%endif
%icon_theme_cache_postun
%else

%post
%if ! %{with separated_libs}
/sbin/ldconfig
%endif
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
%if ! %{with separated_libs}
/sbin/ldconfig
%endif
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%if %{with separated_libs}
%post   -n %{libdino} -p /sbin/ldconfig
%postun -n %{libdino} -p /sbin/ldconfig
%post   -n %{libqlite} -p /sbin/ldconfig
%postun -n %{libqlite} -p /sbin/ldconfig
%post   -n %{libcryptovala} -p /sbin/ldconfig
%postun -n %{libcryptovala} -p /sbin/ldconfig
%post   -n %{libxmppvala} -p /sbin/ldconfig
%postun -n %{libxmppvala} -p /sbin/ldconfig
%endif

%if %{with separated_plugins}
%files -f dino.lang
%else

%files -f dino.lang -f dino-omemo.lang -f dino-openpgp.lang
%endif
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/dino
%dir %{_libdir}/dino
%dir %{_libdir}/dino/plugins

%if ! %{with separated_plugins}
%{_libdir}/dino/plugins/*.so
%endif
%{_datadir}/applications/im.dino.Dino.desktop
%{_datadir}/dbus-1/services/im.dino.Dino.service
%{_datadir}/icons/hicolor/*/apps/*dino*
%{_datadir}/metainfo/im.dino.Dino.appdata.xml

%if ! %{with separated_libs}
%{_libdir}/libdino.so.*
%{_libdir}/libqlite.so.*
%{_libdir}/libcrypto-vala.so.*
%{_libdir}/libxmpp-vala.so.*
%endif

%if %{with separated_libs}
%files -n %{libdino}
%license LICENSE
%doc README.md
%{_libdir}/libdino.so.*

%files -n %{libqlite}
%license LICENSE
%doc README.md
%{_libdir}/libqlite.so.*

%files -n %{libxmppvala}
%license LICENSE
%doc README.md
%{_libdir}/libxmpp-vala.so.*
%endif

%files devel
%{_includedir}/*.h
%{_libdir}/libdino.so
%{_libdir}/libqlite.so
%{_libdir}/libcrypto-vala.so
%{_libdir}/libxmpp-vala.so
%{_datadir}/vala/vapi/*.{vapi,deps}

%if %{with separated_plugins}
%files plugin-openpgp -f dino-openpgp.lang
%license LICENSE
%doc README.md
%{_libdir}/dino/plugins/openpgp.so

%files plugin-omemo -f dino-omemo.lang
%license LICENSE
%doc README.md
%{_libdir}/dino/plugins/omemo.so

%files plugin-http-upload
#-f dino-http-files.lang
%license LICENSE
%doc README.md
%{_libdir}/dino/plugins/http-files.so
%endif

%changelog
