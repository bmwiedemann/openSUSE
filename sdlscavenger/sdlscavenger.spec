#
# spec file for package sdlscavenger
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


Name:           sdlscavenger
Version:        145_2015_01_05
Release:        0
Summary:        Lode Runner like game
License:        GPL-1.0
Group:          Amusements/Games/Logic
Url:            http://sourceforge.net/projects/sdlscavenger/
Source0:        http://downloads.sourceforge.net/%{name}/sdlscav-145.4_2015_01_05.tgz
Source1:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
SdlScavenger a fun 2-D Game like Lode Runner.
With 196 very good puzzle screens to solve.

%prep
%setup -q -n sdlscav-145

# SED-FIX-OPENSUSE -- Fix Paths and Highscore
sed -i -e 's|$$HOME/.scavenger|$$HOME/.%{name}|;
           s|/usr/local/bin|$(DESTDIR)/usr/bin|;
           s|/usr/local/games/scavenger|$(DESTDIR)/usr/share/%{name}|;
           s|sdlscav $(DESTDIR)/usr/bin/|sdlscav $(DESTDIR)/usr/bin/%{name}|' Makefile
sed -i -e 's|local/games/scavenger|share/%{name}|;
           s|".scavenger"|".%{name}"|' names.h
sed -i 's|sdlscav|%{name}|' scavsaver

%build
make %{?_smp_mflags} CC="cc %{optflags}"

%install
%make_install

# install icon
install -Dm 0644 data/scav.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING CREDITS DOC NEW_FEATURES README STRATEGY changelog
%{_bindir}/%{name}
%{_bindir}/scavsaver
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
