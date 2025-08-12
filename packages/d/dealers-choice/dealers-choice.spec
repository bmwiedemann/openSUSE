#
# spec file for package dealers-choice
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


Name:           dealers-choice
Version:        0.0.8
Release:        0
Summary:        Online Multiplayer Stud and Draw Poker
License:        MIT
Group:          Amusements/Games/Board/Card
URL:            https://dealer-s-choice.github.io/
Source:         https://github.com/Dealer-s-Choice/dealers-choice/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  meson >= 0.61.0
BuildRequires:  python3
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(sdl2)
Requires:       hicolor-icon-theme

%description
Dealer's Choice is a cross-platform, networked multiplayer poker game that
supports various draw and stud variants, including optional wild cards. The
deal rotates between players, and each new game allows a different player to
choose the variant.

%lang_package

%prep
%autosetup -n %{name}-%{version}

%build
%meson \
	-Ddocdir=%{_docdir}/%{name} \
	--buildtype=release \
	-Dstrip=true \
	-Db_sanitize=none
%meson_build

%install
%meson_install
%check
%meson_test

%find_lang %{name}

rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%license LICENSE
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/dealers-choice.desktop
%{_datadir}/%{name}/
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/128x128/apps/dealers-choice.png
%{_datadir}/icons/hicolor/64x64/apps/dealers-choice.png
%{_datadir}/icons/hicolor/32x32/apps/dealers-choice.png
%{_datadir}/icons/hicolor/16x16/apps/dealers-choice.png
%{_datadir}/icons/hicolor/scalable/apps/dealers-choice.svg

%files lang -f %{name}.lang

%changelog
