#
# spec file for package swappy
#
# Copyright (c) 2022 SUSE LLC
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


Name:           swappy
Version:        1.5.1
Release:        0
Summary:        Wayland compositor screenshot editor
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://github.com/jtheoof/swappy
Source:         https://github.com/jtheoof/swappy/archive/v%{version}.tar.gz
Source1:        https://github.com/jtheoof/swappy/releases/download/v%{version}/swappy-%{version}.tar.gz.sig
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(pango)
Requires:       fontawesome-fonts
Suggests:       wl-clipboard
Suggests:       wl-clipboard-rs

%description
A Wayland native snapshot and editor tool

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*
%{_datadir}/applications/swappy.desktop
%{_datadir}/icons/hicolor/scalable/apps/swappy.svg

%files lang -f %{name}.lang
%{_datadir}/locale/en/LC_MESSAGES/swappy.mo

%changelog
