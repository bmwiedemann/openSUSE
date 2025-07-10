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
Version:        0.0.5
Release:        0
Summary:        Online Multiplayer Stud and Draw Poker
License:        MIT
Group:          Amusements/Games/Board/Card
URL:            https://dealer-s-choice.github.io/
Source:         https://github.com/Dealer-s-Choice/dealers_choice/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson >= 0.61.0
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  libSDL2_net-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  libprotobuf-c-devel

Requires:       hicolor-icon-theme

%description
Dealer's Choice is an online Multiplayer Stud and Draw Poker, where the deal
rotates and each new game allows a different player to select the variant.

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

%find_lang %{name}

# Remove bundled license files if they exist in docs (duplicate with %license)
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%license LICENSE
%{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/applications/dealers-choice.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/dealers-choice.png
%{_datadir}/icons/hicolor/scalable/apps/dealers-choice.svg

%files lang -f %{name}.lang

%changelog
