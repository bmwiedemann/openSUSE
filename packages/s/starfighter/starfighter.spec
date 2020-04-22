#
# spec file for package starfighter
#
# Copyright (c) 2020 SUSE LLC
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


%define baseversion 2.0
Name:           starfighter
Version:        2.0.0.3
Release:        0
Summary:        Liberate the universe from the evil company WEAPCO
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://pr-starfighter.github.io/
Source0:        https://github.com/pr-starfighter/%{name}/releases/download/v%{version}/starfighter-%{baseversion}-src.tar.gz
Source1:        %{name}-icons.tar
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sdl)

%description
Project: Starfighter is an old school 2D shoot 'em up. In the game you take on
the role of a rebel pilot called Chris, who is attempting to overthrow a
military corporation called Weapco. Weapco has seized control of the known
universe and currently rules it with an iron fist. Chris can no longer stand
back and watch as millions of people suffer and die. He steals an experimental
craft known as "Firefly" and begins his mission to fight his way to Sol,
freeing key systems along the way. The game opens with Chris attempting to
escape a Weapco patrol that has intercepted him.

%prep
%setup -q -a 1 -n %{name}-%{baseversion}-src

%build
%configure
%make_build

%install
%make_install

# install icons
for i in 16 32 48 64 72 96 128 ; do
    install -Dm 0644 icons/%{name}_${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# remove duplicate docs
rm -fr %{buildroot}%{_datadir}/doc/%{name}

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%license COPYING LICENSES
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
