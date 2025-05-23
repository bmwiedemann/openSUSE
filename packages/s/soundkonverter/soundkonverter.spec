#
# spec file for package soundkonverter
#
# Copyright (c) 2025 SUSE LLC
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


Name:           soundkonverter
Version:        3.0.1+git20240225
Release:        0
Summary:        Audio file converter, CD ripper and Replay Gain tool
License:        GPL-2.0-only
URL:            https://github.com/nphantasm/%{name}
# n=soundkonverter && v=3.0.1 && g=20240225 && d=$n-$v+git$g && cd /tmp && git clone https://github.com/nphantasm/$n.git && pushd $n && rm -rf .??* && popd && mv $n $d && f=$d.tar.xz && tar c --remove-files "$d" | xz -9e > "$f"
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cdparanoia-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)
Requires:       cdparanoia
Requires:       flac
Requires:       speex
Requires:       vorbis-tools
Requires:       wavpack

%description
soundKonverter is a frontend to various audio converters.

%prep
%autosetup -p1

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
pushd src
%cmake_kf5 -d build -- "-DKF5_BUILD=ON"
%cmake_build
popd

%install
pushd src
%kf5_makeinstall -C build
popd

%suse_update_desktop_file -r %{name} AudioVideo AudioVideoEditing KDE

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license src/COPYING
%doc src/CHANGELOG src/README
%dir %{_datadir}/kxmlgui5/soundkonverter
%dir %{_datadir}/solid
%dir %{_datadir}/solid/actions
%dir %{_datadir}/soundkonverter
%{_bindir}/soundkonverter
%{_libdir}/libsoundkonvertercore.so*
%{_libdir}/qt5/plugins/soundkonverter_*
%{_datadir}/metainfo/soundkonverter.appdata.xml
%{_datadir}/applications/soundkonverter.desktop
%{_datadir}/icons/hicolor/*/apps/soundkonverter*.png
%{_datadir}/kservices5/soundkonverter_*
%{_datadir}/kservicetypes5/soundkonverter_*.desktop
%{_datadir}/kxmlgui5/soundkonverter/soundkonverterui.rc
%{_datadir}/solid/actions/soundkonverter-rip-audiocd.desktop
%{_datadir}/soundkonverter/*

%changelog
