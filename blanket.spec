#
# spec file for package blanket
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


Name:           blanket
Version:        0.7.0
Release:        0
Summary:        Listen to different sounds
License:        GPL-3.0-or-later
Group:          Amusements/Toys/Other
URL:            https://github.com/rafaelmardojai/blanket
Source:         https://github.com/rafaelmardojai/blanket/archive/%{version}.tar.gz
BuildRequires:  appstream-glib-devel
BuildRequires:  blueprint-compiler
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libhandy-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildArch:      noarch

%description
Improve focus and increase your productivity by listening to different sounds.
Or allows you to fall asleep in a noisy environment.

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
%license COPYING
%doc README.md
%{_bindir}/blanket
%{_datadir}/blanket/
%{_datadir}/applications/com.rafaelmardojai.Blanket.desktop
%{_datadir}/glib-2.0/schemas/com.rafaelmardojai.Blanket.gschema.xml
%{_datadir}/metainfo/com.rafaelmardojai.Blanket.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/com.rafaelmardojai.Blanket.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.rafaelmardojai.Blanket-symbolic.svg

%files lang -f %{name}.lang
%{_datadir}/locale/??/LC_MESSAGES/blanket.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/blanket.mo

%changelog
