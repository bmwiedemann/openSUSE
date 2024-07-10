#
# spec file for package lximage-qt
#
# Copyright (c) 2024 SUSE LLC
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
Version:        2.0.1
Release:        0
Summary:        LXQt Image Viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/lxqt/lximage-qt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lxqt2-build-tools-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6DBus) >= 6.3.0
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache) >= 1.1.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
Recommends:     %{name}-lang = %{version}-%{release}
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils

%description
Image Viewer for LXQt and Thumbnail Generator for PCManFM-Qt

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%qt6_build

%install
%qt6_install
%suse_update_desktop_file -r %{name} Graphics Viewer RasterGraphics 2DGraphics Photography
%fdupes -s %{buildroot}%{_datadir}/%{name}

%find_lang %{name} --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/metainfo/%{name}.metainfo.xml
%license COPYING

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
