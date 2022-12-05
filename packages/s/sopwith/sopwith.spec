#
# spec file for package sopwith
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


Name:           sopwith
Version:        2.1.1
Release:        0
Summary:        SDL port of the %{name} game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/fragglet/sdl-sopwith
Source0:        https://github.com/fragglet/sdl-sopwith/releases/download/sdl-sopwith-%{version}/sdl-sopwith-%{version}.tar.gz
Source1:        %{name}.png
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_gfx-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme

%description
This is a port of the classic computer game "Sopwith" to run on modern
computers and operating systems.

%prep
%setup -q -n sdl-%{name}-%{version}

%build
%configure --docdir=%{_docdir}
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/sdl-%{name}

cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Sopwith
Type=Application
Comment=The classic %{name} game
Exec=%{name}
Terminal=false
Icon=%{name}
EOF

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications           \
  --add-category ArcadeGame                            \
  --add-category Game                                  \
  %{name}.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/72x72/apps/
cp %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/72x72/apps/

%files
%license COPYING.md
%doc FAQ.md NEWS.md README.md TODO doc/origdoc.txt
%{_bindir}/%{name}
%{_mandir}/man5/sopwith.cfg.5*
%{_mandir}/man6/%{name}*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
