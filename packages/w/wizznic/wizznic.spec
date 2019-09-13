#
# spec file for package wizznic
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright Vincent Petry <PVince81@yahoo.fr>
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


Name:           wizznic
Version:        0.9.9
Release:        0
Summary:        Implementation of the arcade classic Puzznic
License:        GPL-3.0
Group:          Amusements/Games/Board/Puzzle
Url:            http://dustedgames.blogspot.co.uk/p/wizznic.html
Source0:        http://downloads.sourceforge.net/%{name}/Source%20Releases/%{name}-%{version}-src.tar.bz2
Source1:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
Wizznic is a brick-matching puzzle-game, an improved version of Puzznic.
The challenge is to clear each level of bricks by moving the bricks next
to each other, this sounds a lot easier than it is.
The bricks are heavy, so you can only push them, not lift them up.

%prep
%setup -q -n %{name}-%{version}-src

# Correct Permissions
sed -i 's|chmod -R 755|#chmod -R 755|' Makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fgnu89-inline" DATADIR="%{_datadir}/%{name}/"

# Correct what fdupes didn't find
rm -fv data/menu/charmap0.png
ln -sf ../../packs/000_wizznic/themes/chars/charmap0.png data/menu/charmap0.png
rm -fv data/menu/charmap1.png
ln -sf ../../packs/000_wizznic/themes/chars/charmap1.png data/menu/charmap1.png
rm -fv 010_wizznic-silver/themes/tiles/cyber-expl0.png
ln -sf ../../packs/000_wizznic/themes/chars/charmap0.png data/menu/charmap0.png
ln -sf ../../../000_wizznic/themes/oldskool/tiles/cyberpunk-expl0.png packs/010_wizznic-silver/themes/tiles/cyber-expl0.png
rm -fv data/snd/menuclick.ogg
ln -sf ../../packs/000_wizznic/themes/oldskool/snd/brickbreak.ogg data/snd/menuclick.ogg

%install
make install BINDIR=%{buildroot}%{_bindir}/ DATADIR=%{buildroot}%{_datadir}/%{name}/

# install icon
install -Dm 0644 data/wmicon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc doc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
