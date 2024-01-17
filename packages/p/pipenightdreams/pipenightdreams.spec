#
# spec file for package pipenightdreams
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pipenightdreams
Version:        0.10.0
Release:        0
Summary:        Puzzle game similar to PipeMania
License:        GPL-2.0+
Group:          Amusements/Games/Logic
Url:            https://www.libsdl.org/projects/pipenightdreams/
Source0:        https://www.libsdl.org/projects/%{name}/packages/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
# PATCH-FIX-OPENSUSE - pipenightdreams-src.patch -- Fix bad C code
Patch0:         %{name}-src.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(sdl)

%description
PipeNightDreams is a PipeDream style game. The objetive of the game
is to carry liquid from some point to the exit using different kinds
of pipes. On each level there is a minimum number of required pipes
that should be at least reached for it to be completed.

The score is increased by using as many pipes as possible an by
collecting various bonus tokens making the liquid pass through their
pipes. There are also life bonus and, hopefully soon, "freeze tokens".

%prep
%setup -q
%patch0 -p1

# SED-FIX-OPENSUSE -- Fix paths
sed -i 's|datadir/games|datadir|' configure
find -exec grep -q "/games" {} \; \
     -exec sed -i 's|/games||' {} \;

%build
%{?suse_update_config:%{suse_update_config -f}}
autoreconf -fi

%configure
make %{?_smp_mflags}

%install
%make_install

# install icon
install -Dm 0644 images/default/splash.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
