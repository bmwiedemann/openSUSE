#
# spec file for package deepin-music-player
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013-2020 Hillwood Yang <hillwood@opensuse.org>
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


Name:           deepin-music-player
Version:        5.0.1
Release:        0
Summary:        Deepin Music Player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/linuxdeepin/deepin-music
Source0:        https://github.com/linuxdeepin/deepin-music/archive/%{version}/deepin-music-%{version}.tar.gz
Patch0:         deepin-music-Qt-5_15.patch
# Fix boo#1131464
Source1:        %{name}-rpmlintrc
BuildRequires:  QtAV-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Network-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xext)
Provides:       deepin-music = %{version}-%{release}
Obsoletes:      deepin-music < %{version}-%{release}
Recommends:     deepin-music-libnetease-meta-search = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Music Player is a music player backed by gstreamer, with
customizable UI, and featuring music search by Pinyin and Quanpin. It
supports colorful lyrics, online audio support and a "mini mode".

%package -n libdmusic1
Summary:        Libraries for Deepin Music Player
Group:          System/Libraries

%description -n libdmusic1
This package contains the main implementation of the Deepin Music
Player.

%package -n deepin-music-libnetease-meta-search
Summary:        Libnetease integration for the Deepin Music Player
Group:          Productivity/Multimedia/Sound/Players

%description -n deepin-music-libnetease-meta-search
This package contains the libnetease plugin for searches with the
Deepin Music Player searches.

%package -n libdbusextended-qt5-1
Summary:        D-Bus system for the Deepin Music Player
Group:          System/Libraries

%description -n libdbusextended-qt5-1
Deepin Music Player with brilliant and tweakful UI Deepin-UI based,
gstreamer front-end, with features likes search music by pinyin,
quanpin, colorful lyrics supports, and more powerful functions
you will found.

The libdbusextended-qt5 is the Dbus system libraries for
Deepin Music Player.

%package -n libmpris-qt5-1
Summary:        MPRI system for the Deepin Music Player
Group:          System/Libraries

%description -n libmpris-qt5-1
The MPRI system library for Deepin Music Player.

%package -n libdbusextended-qt5-devel
Summary:        Development files for the Deepin Music Player D-Bus system
Group:          Development/Libraries/C and C++
Requires:       libdbusextended-qt5-1 = %{version}-%{release}

%description -n libdbusextended-qt5-devel
The libdbusextended-devel package contains the header files and developer
docs for libdbusextended.

%package -n libmpris-qt5-devel
Summary:        Development files for the Deepin Music Player MPRI library
Group:          Development/Libraries/C and C++
Requires:       libmpris-qt5-1 = %{version}-%{release}

%description -n libmpris-qt5-devel
The libmpris-devel package contains the header files and developer
docs for libmpris.

%lang_package

%prep
%setup -q -n deepin-music-%{version}
%if 0%{?suse_version} > 1500
%patch0 -p1
%endif

sed -i '/%1/s|lib|%{_lib}|' src/music-player/core/pluginmanager.cpp
sed -i '/target.path/s|lib|%{_lib}|' src/libdmusic/libdmusic.pro \
src/plugin/netease-meta-search/netease-meta-search.pro
# fix the non-standard unity stuff, anyway we will not use it.
# appending -x
sed -i 's/^\[\([^D].*$\)/\[X-\1/' src/music-player/data/deepin-music.desktop
# replace [[:space:]] with '-'
sed -i 's/ Shortcut /-Shortcut-/' src/music-player/data/deepin-music.desktop
# Enable netease plugin
sed -i 's/#SUBDIRS/SUBDIRS/' src/plugin/plugin.pro
sed -i 's|share/$${TARGET}|share/deepin-music|' src/music-player/install.pri

%build
%qmake5 DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir} \
        LIBSUFFIX=%{lib}
make %{?_smp_mflags}

%install
%qmake5_install

%ifnarch i386 i486 i586 i686 athlon %{arm}
    mv %{buildroot}%{_libexecdir}/*.so* %{buildroot}%{_libdir}
    mv %{buildroot}%{_libexecdir}/pkgconfig %{buildroot}%{_libdir}/pkgconfig
    rm -rf %{buildroot}%{_libexecdir}
%endif

# Remove invalid developement files.
rm -rf %{buildroot}%{_libdir}/libdmusic.so
rm -rf %{buildroot}%{_datadir}/translations

%suse_update_desktop_file -r deepin-music Player AudioVideo
%fdupes %{buildroot}%{_prefix}

%post -n libdmusic1 -p /sbin/ldconfig

%postun -n libdmusic1 -p /sbin/ldconfig

%post -n libdbusextended-qt5-1 -p /sbin/ldconfig

%postun -n libdbusextended-qt5-1 -p /sbin/ldconfig

%post -n libmpris-qt5-1 -p /sbin/ldconfig

%postun -n libmpris-qt5-1 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE  COPYING
%{_bindir}/deepin-music
%{_datadir}/applications/deepin-music.desktop
%{_datadir}/dman
%{_datadir}/icons/hicolor/scalable/apps/deepin-music.svg

%files -n libdmusic1
%defattr(-,root,root,-)
%{_libdir}/libdmusic.so.*

%files -n deepin-music-libnetease-meta-search
%defattr(-,root,root,-)
%dir %{_libdir}/deepin-music
%dir %{_libdir}/deepin-music/plugins
%{_libdir}/deepin-music/plugins/libnetease-meta-search.so.*
%{_libdir}/deepin-music/plugins/libnetease-meta-search.so

%files -n libdbusextended-qt5-1
%defattr(-,root,root,-)
%{_libdir}/libdbusextended-qt5.so.*

%files -n libmpris-qt5-1
%defattr(-,root,root,-)
%{_libdir}/libmpris-qt5.so.*

%files -n libdbusextended-qt5-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/dbusextended-qt5.pc
%{_libdir}/libdbusextended-qt5.so
%{_includedir}/DBusExtended

%files -n libmpris-qt5-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/mpris-qt5.pc
%{_libdir}/libmpris-qt5.so
%dir %{_libdir}/qt5/
%dir %{_libdir}/qt5/mkspecs/
%dir %{_libdir}/qt5/mkspecs/features/
%{_libdir}/qt5/mkspecs/features/mpris-qt5.prf
%{_includedir}/MprisQt/

%files lang
%defattr(-,root,root,-)
%{_datadir}/deepin-music

%changelog
