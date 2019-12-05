#
# spec file for package sdlpop
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sdlpop
Version:        1.20
Release:        0
Summary:        An open-source port of Prince of Persia
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            http://www.popot.org/get_the_games.php?game=SDLPoP
Source:         https://github.com/NagyD/SDLPoP/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/NagyD/SDLPoP/pull/184.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)

%description
SDLPoP is an open-source port of Prince of Persia 1,
that runs natively under Linux. It is based on the DOS
version of the game, and uses SDL.

Run the prince executable in a path were the original
game data files are located.

%prep
%setup -q -n SDLPoP-%{version}
%patch0 -p1
sed -i 's/\r$//' doc/*.txt

%build
cd src
%cmake
%make_jobs

%install
install -d %{buildroot}/%{_bindir}
install -Dm0755 prince %{buildroot}/%{_libexecdir}/%{name}/%{name}
install -Dm0644 data/icon.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -d %{buildroot}/%{_libexecdir}/%{name}
mv data/ %{buildroot}/%{_libexecdir}/%{name}
%suse_update_desktop_file -c %{name} %{name} "Platformer" %{name} %{name} Game ActionGame

%fdupes %{buildroot}/%{_libexecdir}/%{name}

# Install Wrapper
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
exec "%{_libexecdir}/%{name}/\${0##*/}" \$@
EOF

%files
%doc doc/Readme.txt doc/ChangeLog.txt doc/bugs.txt
%license doc/gpl-3.0.txt
%attr(0755,root,root) %{_bindir}/sdlpop
%{_libexecdir}/%{name}
%{_datadir}/icons/hicolor/32x32/apps/sdlpop.png
%{_datadir}/applications/sdlpop.desktop

%changelog
