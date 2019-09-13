#
# spec file for package audacious
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define aud_plugin_ver_min 3.10
%define aud_plugin_ver_max 3.10.99
%define core_soname 5
%define qt_soname 2
%define gui_soname 5
%define tag_soname 3
Name:           audacious
Version:        3.10.1
Release:        0
Summary:        Audio player with graphical UI and library functionality
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Sound/Players
URL:            https://audacious-media-player.org/
Source:         https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.5
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(dbus-1) >= 1.0.2
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.88
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.32
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libguess) >= 1.2
Requires:       %{name}-plugins%{?_isa} <= %{aud_plugin_ver_max}
Requires:       %{name}-plugins%{?_isa} >= %{aud_plugin_ver_min}
Recommends:     %{name}-lang
Recommends:     %{name}-plugins-extra >= %{aud_plugin_ver_min}

%description
Audacious is an audio player. It is based on GTK+ and supports a wide
range of audio codecs. It still features an alternative skinned user
interface (based on Winamp 2.x skins). Historically, it started as a
fork of a fork of XMMS.

%lang_package

%package -n libaudcore%{core_soname}
Summary:        Main functionality library of Audacious
Group:          System/Libraries
Provides:       libaudcore%{?_isa} = %{version}

%description -n libaudcore%{core_soname}
Library from the Audacious audio player.

%package -n libaudqt%{qt_soname}
Summary:        QT GUI implementation of Audacious
Group:          System/Libraries
Requires:       libaudcore%{core_soname} >= %{version}

%description -n libaudqt%{qt_soname}
Library from the Audacious audio player.

%package -n libaudgui%{gui_soname}
Summary:        GTK GUI implementation of Audacious
Group:          System/Libraries
Requires:       libaudcore%{core_soname} >= %{version}

%description -n libaudgui%{gui_soname}
Library from the Audacious audio player.

%package -n libaudtag%{tag_soname}
Summary:        ID3 and APE metadata support for Audacious
Group:          System/Libraries
Requires:       libaudcore%{core_soname} >= %{version}

%description -n libaudtag%{tag_soname}
Library from the Audacious audio player.

%package devel
Summary:        Development files for Audacious
Group:          Development/Libraries/C and C++
Requires:       libaudcore%{core_soname} = %{version}
Requires:       libaudgui%{gui_soname} = %{version}
Requires:       libaudqt%{qt_soname} = %{version}
Requires:       libaudtag%{tag_soname} = %{version}

%description devel
Development files for Audacious audio player.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-qt     \
  --enable-gtk    \
  --disable-rpath
make %{?_smp_mflags} V=1

%install
%make_install

install -Dpm 0644 contrib/%{name}.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%post -n libaudcore%{core_soname} -p /sbin/ldconfig

%postun -n libaudcore%{core_soname} -p /sbin/ldconfig

%post -n libaudqt%{qt_soname} -p /sbin/ldconfig

%postun -n libaudqt%{qt_soname} -p /sbin/ldconfig

%post -n libaudgui%{gui_soname} -p /sbin/ldconfig

%postun -n libaudgui%{gui_soname} -p /sbin/ldconfig

%post -n libaudtag%{tag_soname} -p /sbin/ldconfig

%postun -n libaudtag%{tag_soname} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/audtool
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_mandir}/man?/audtool.?%{?ext_man}

%files lang -f %{name}.lang

%files -n libaudcore%{core_soname}
%{_libdir}/libaudcore.so.%{core_soname}*

%files -n libaudqt%{qt_soname}
%{_libdir}/libaudqt.so.%{qt_soname}*

%files -n libaudgui%{gui_soname}
%{_libdir}/libaudgui.so.%{gui_soname}*

%files -n libaudtag%{tag_soname}
%{_libdir}/libaudtag.so.%{tag_soname}*

%files devel
%{_includedir}/%{name}/
%{_includedir}/libaudcore/
%{_libdir}/libaudcore.so
%{_includedir}/libaudqt/
%{_libdir}/libaudqt.so
%{_includedir}/libaudgui/
%{_libdir}/libaudgui.so
%{_libdir}/libaudtag.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
