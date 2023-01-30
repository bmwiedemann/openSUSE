#
# spec file for package mirrormagic
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mirrormagic
Version:        3.1.0
Release:        0
Summary:        Puzzle game where you steer a beam of light using mirrors
License:        GPL-2.0-only
Group:          Amusements/Games/Logic
URL:            https://www.artsoft.org/mirrormagic/
Source0:        https://www.artsoft.org/RELEASES/unix/%{name}/%{name}-%{version}-linux.tar.gz
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(sdl2)

%description
This is a nice little game with color graphics and sound for your
Unix system with color X11. You need an 8-bit color display or better.
It will not work on black&white systems, and maybe not on gray scale
systems.

It was first released as "Mindbender" in the year 1989 on the Amiga
(with ports on other computer systems) and is in fact a clone of the
C64 game "Deflektor".

%prep
%setup -q -b 1

rm -rfv lib mirrormagic
find . -name "*.orig" -delete

%build
%make_build \
    PROGBASE=%{name} \
    OPTIONS="%{optflags} -fPIE" \
    EXTRA_LDFLAGS="%{optflags} -pie" \
    BASE_PATH=%{_datadir}/%{name}

%install
# install executable
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{graphics,levels,music,sounds}
for d in graphics levels music sounds ; do
    cp -a $d %{buildroot}%{_datadir}/%{name}
done

# install icons
for i in 32 48 64 72 96 ; do
    install -Dm 0644 ../icons/%{name}_${i}x${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install Desktop file
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%license COPYING
%doc ChangeLog CREDITS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%changelog
