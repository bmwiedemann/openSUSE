#
# spec file for package lximage-qt
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


Name:           lximage-qt
Version:        0.16.0
Release:        0
Summary:        LXQt Image Viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm-qt) >= %{version}
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(xfixes)
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils

%description
Image Viewer for LXQt and Thumbnail Generator for PCManFM-Qt

%lang_package

%prep
%setup -q

%build
%cmake \
    -DUSE_QT5=ON \
    -DPULL_TRANSLATIONS=OFF
%make_build

%install
%cmake_install

%suse_update_desktop_file -r %{name} Graphics Viewer RasterGraphics 2DGraphics Photography
%suse_update_desktop_file -r %{name}-screenshot Utility DesktopUtility

%fdupes %{buildroot}%{_datadir}/%{name}

%find_lang %{name} --with-qt

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*

%changelog
