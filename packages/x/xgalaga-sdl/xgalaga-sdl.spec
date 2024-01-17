#
# spec file for package xgalaga-sdl
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


Name:           xgalaga-sdl
Version:        2.1.1.0
Release:        0
Summary:        Classic single screen vertical shoot em up SDL
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade/Shoot
Url:            http://sourceforge.net/projects/xgalaga-sdl/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-sdl.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  liberation-fonts
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(sdl)

%description
XGalaga-SDL is a port of the popular X11 game XGalaga,
a clone of Galaga, using the SDL library.
XGalaga was originally written by Joe Rumsey.

%prep
%setup -q -n %{name}-%{version}-sdl

# Remove not needed files
sed -i -e 's|CREDITS||' \
    -i -e 's|fonts/copyright||' Makefile.in

%build

%configure --datadir=%{_datadir}/%{name}
make %{?_smp_mflags}

%install
%make_install

# install icon
install -Dm 0644 %{S:2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# Use system fonts instead of bundling our own
rm -f %{buildroot}%{_datadir}/%{name}/fonts/LiberationMono-Bold.ttf
ln -s ../../fonts/truetype/LiberationMono-Bold.ttf %{buildroot}%{_datadir}/%{name}/fonts/LiberationMono-Bold.ttf

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING CREDITS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6x%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
