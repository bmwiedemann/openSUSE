#
# spec file for package qtox
#
# Copyright (c) 2020 SUSE LLC
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


%define realname qTox

Name:           qtox
Version:        1.17.2
Release:        0
Summary:        Tox client
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://qtox.github.io/
Source0:        https://github.com/qTox/qTox/releases/download/v%{version}/v%{version}.tar.gz
Source1:        https://github.com/qTox/qTox/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:        qtox.keyring
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files

# needed?
####BuildRequires:  gcc-c++
####BuildRequires:  opencv-devel >= 2.4.9
###BuildRequires:  opencv-qt5-devel
###BuildRequires:  pkgconfig(Qt5Sql5-sqlite)
BuildRequires:  libqt5-qtbase-common-devel >= 5.2.0
BuildRequires:  pkgconfig(sqlite3)
# needed?

%if 0%{?suse_version} > 1500
BuildRequires:  ffmpeg-devel >= 4.0.0
%else
BuildRequires:  ffmpeg-devel
%endif
#BuildRequires:  pkgconfig(libavformat)
#BuildRequires:  pkgconfig(libavdevice)
#BuildRequires:  pkgconfig(libavutil)
#BuildRequires:  pkgconfig(libavcodec)
#BuildRequires:  pkgconfig(libswscale)

BuildRequires:  glib2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel >= 5.2.0
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libqrencode) >= 3.0.3
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openal) >= 1.16.0
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(toxcore)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(xscrnsaver) >= 1.2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Powerful Tox client that tries to follow the Tox UI mockup while running on all
major systems.

%prep
%setup -q -c -n qTox-%{version}
# rpmlint: datetime
sed -i -e 's|__TIME__ + " " + __DATE__|"%(date +"%%H:%%M") %(date +"%%Y-%%m-%%d")"|g' src/main.cpp
sed -i -e 's|__TIME__ << __DATE__|"%(date +"%%H:%%M") %(date +"%%Y-%%m-%%d")"|g' src/main.cpp

%build
CFLAGS="%{optflags} -Wno-error=parentheses"
mkdir build
pushd build
cmake -DCMAKE_C_FLAGS="$CFLAGS" -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags} PREFIX=%{_prefix}
popd

%install
make install -C build PREFIX=%{_prefix} DESTDIR=%{buildroot}
# remove non-standard dimensions
rm -rf %{buildroot}%{_datadir}/icons/hicolor/14x14
# decompress svgz to svg
cd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
gzip -d < %{name}.svgz > %{name}.svg
rm %{name}.svgz
# fix desktop-file-name
mv %{buildroot}%{_datadir}/applications/io.github.qtox.qTox.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/metainfo
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
