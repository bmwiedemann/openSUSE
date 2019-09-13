#
# spec file for package kvirc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kvirc
Version:        5.0.0
Release:        0
Summary:        Graphical Front-End for IRC
License:        GPL-2.0-or-later AND (GPL-3.0-only OR SUSE-LGPL-2.1-with-digia-exception-1.1)
Group:          Productivity/Networking/IRC
URL:            http://www.kvirc.net/
Source:         ftp://ftp.kvirc.net/pub/kvirc/%{version}/source/KVIrc-%{version}.tar.bz2
BuildRequires:  audiofile-devel
BuildRequires:  cmake >= 3.1.0
BuildRequires:  doxygen
BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libX11-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtheora-devel
BuildRequires:  perl
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  subversion
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5MultimediaWidgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
%requires_eq    perl
Obsoletes:      %{name}-devel < %{version}
%if 0%{?suse_version} < 1500
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif

%description
IRC (Internet Relay Chat) client with an MDI interface; scripting,
pop-up, alias, and event editor; DCC (SEND CHAT VOICE and RESUME);
SOCKSV4 & V5 support; and more.

%prep
%setup -q -n KVIrc-%{version}

%build
%if 0%{?suse_version} < 1500
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
export CC=gcc-7
export CXX=g++-7
%endif

EXTRA_FLAGS="-UCMAKE_MODULE_LINKER_FLAGS \
%if "%{?_lib}" == "lib64"
-DLIB_SUFFIX=64 \
%endif
"

%cmake_kf5 -d build -- $EXTRA_FLAGS
%make_jobs

%install
%kf5_makeinstall -C build
%suse_update_desktop_file kvirc Network IRCClient
L="$PWD/%{name}.lang"
echo -n >"$L"
pushd "%{buildroot}%{_kf5_sharedir}/%{name}"
find . -type f -name '*.mo' | while read f; do
l="${f#./}"
l="${l%%/*}"
echo "%lang($l) %{_kf5_sharedir}/%{name}/${f#./}" >> "$L"
done
popd
%fdupes %{buildroot}

rm %{buildroot}%{_libdir}/libkvilib.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc ChangeLog
%license COPYING
%{_kf5_applicationsdir}/kvirc.desktop
%{_kf5_bindir}/kvirc
%{_kf5_bindir}/kvirc-config
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_libdir}/kvirc/
%{_kf5_libdir}/libkvilib.so.*
%{_kf5_mandir}/*/man?/kvirc.*
%{_kf5_mandir}/man?/kvirc.*
%{_kf5_sharedir}/kvirc/
%{_kf5_sharedir}/pixmaps/kvirc.png

%changelog
