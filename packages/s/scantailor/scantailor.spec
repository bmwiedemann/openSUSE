#
# spec file for package scantailor
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


Name:           scantailor
Version:        1.0.16
Release:        0
Summary:        Interactive post-processing tool for scanned pages
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://scantailor.sourceforge.net/
Source0:        https://github.com/4lex4/%{name}-advanced/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar.bz2
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-with-Qt-5.15-missing-QPainterPath-includes.patch
BuildRequires:  cmake >= 3.9.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_test-devel >= 1.65.0
%else
BuildRequires:  boost-devel >= 1.65.0
%endif

%description
Scan Tailor is an interactive post-processing tool for scanned pages.
It performs operations such as page splitting, deskewing,
adding/removing borders and others. It takes raw scans, and outputs
pages ready to be printed or assembled into a PDF or DJVU file.

%prep
%setup -q -a 1 -n %{name}-advanced-%{version}
cp -p resources/icons/{COPYING,COPYING.icons}
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

for s in 256 128 96 72 64 48 32 16 ; do
install -Dm 0644 scantailor-icons/scantailor-${s}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/scantailor.png
done
install -Dm 0644 resources/appicon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/scantailor.svg
# Create desktop-file
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Scan Tailor
GenericName=Post-Processing Tool for Scanned Pages
GenericName[ru]=Обработка отсканированных страниц
Type=Application
Exec=scantailor
Icon=scantailor
Categories=Graphics;Scanning;Qt;
Comment=Interactive Post-Processing Tool for Scanned Pages
Comment[ru]=Интерактивная обработка отсканированных страниц
StartupNotify=true
Terminal=false
EOF
%suse_update_desktop_file -i %{name}

%files
%license LICENSE resources/icons/COPYING.icons
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/icons/hicolor/*/*/ScanTailor.*
%{_datadir}/mime/packages/%{name}-project.xml
%dir %{_datadir}/%{name}-advanced
%dir %{_datadir}/%{name}-advanced/translations
%{_datadir}/%{name}-advanced/translations/%{name}_*.qm

%changelog
