#
# spec file for package pentobi
#
# Copyright (c) 2021 SUSE LLC
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


Name:           pentobi
Version:        19.0
Release:        0
Summary:        Program to play the board game Blokus
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            http://pentobi.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  kio-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  rsvg-convert
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.15
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5WebView)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(appstream)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun):hicolor-icon-theme
Requires(postun):update-desktop-files

%description
Pentobi is a computer opponent for the board game Blokus with
support for Classic, Duo, Junior, Trigon, and Nexos game variants.
Different levels of playing strength are available. Pentobi can
save and load games along with comments and move variations.

%package kde-thumbnailer
Summary:        KDE thumbnailer for Pentobi game files
Group:          Amusements/Games/Strategy/Other
Enhances:       dolphin

%description kde-thumbnailer
This package contains a KDE plugin to display thumbnails of
Pentobi game files.

%prep
%setup -q

%build
%cmake -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
       -DPENTOBI_BUILD_KDE_THUMBNAILER=ON \
       -DPENTOBI_BUILD_TESTS=ON
%make_jobs VERBOSE=1

%install
%cmake_install

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license LICENSE.md
%doc AUTHORS.md NEWS.md README.md
%{_bindir}/pentobi
%{_datadir}/applications/io.sourceforge.pentobi.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/help/*/%{name}
%{_mandir}/man6/pentobi.6%{?ext_man}
%{_mandir}/*/man6/pentobi.6%{?ext_man}
%{_datadir}/metainfo/io.sourceforge.pentobi.appdata.xml

%files kde-thumbnailer
%{_bindir}/pentobi-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/pentobi.thumbnailer
%{_libdir}/qt5/plugins/pentobi-thumbnail.so
%{_datadir}/kservices5/pentobi-thumbnail.desktop
%{_mandir}/man6/pentobi-thumbnailer.6%{?ext_man}
%{_mandir}/*/man6/pentobi-thumbnailer.6%{?ext_man}

%changelog
