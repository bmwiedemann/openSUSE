#
# spec file for package pongix
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pongix
Version:        0.4
Release:        0
Summary:        Free Pong-like game
License:        GPL-2.0
Group:          Amusements/Games/Arcade/Logic
Url:            http://www.losersjuegos.com.ar/juegos/pongix
# Not exist good SourceUrl link
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(sdl)

%description
Pongix is a free game based on the classical Pong game with
support for net game.

%prep
%setup -q

# Fix int to main
sed -i 's|int paleta_|void paleta_|' src/paleta.c

# Correct bad code, add -lm
sed -i 's|-lSDL $LIBS|-lSDL $LIBS -lm|' configure

%build

%configure
make %{?_smp_mflags}

%install
%make_install

# install icon
install -Dm 0644 %{S:2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%attr(0755,root,games) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/%{name}

%changelog
