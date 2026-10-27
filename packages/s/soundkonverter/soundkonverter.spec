#
# spec file for package soundkonverter
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        3.0.1+git20260628
Release:        0
Summary:        Audio file converter, CD ripper and Replay Gain tool
License:        GPL-2.0-only
URL:            https://github.com/ssharunas/%{name}#branch=port-qt6
# n=soundkonverter && cd /tmp && git clone --depth=1 -bport-qt6 https://github.com/ssharunas/$n.git $n && pushd $n && v=3.0.1+git$(TZ=UTC date -d @`git log -1 --format=%at` +%Y%m%d) && d=$n-$v && f=$d.tar.xz && rm -rf .??* && popd && mv $n $d && tar c --remove-files "$d" | xz -9e > "$f"
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cdparanoia-devel
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KCddb6)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(taglib)
Requires:       cdparanoia
Requires:       flac
Requires:       speex
Requires:       vorbis-tools
Requires:       wavpack

%description
%{name} is a frontend to various audio converters.

%prep
%autosetup -p1

%build
%cmake_kf6
%kf6_build

%install
%kf6_install

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license src/COPYING
%doc src/CHANGELOG src/README
%{_bindir}/%{name}
%{_libdir}/lib%{name}core.so*
%{_libdir}/qt6/plugins/%{name}plugins
%{_datadir}/metainfo/org.kde.%{name}.metainfo.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/%{name}

%changelog
