#
# spec file for package sdl-asylum
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oname  asylum

Name:           sdl-asylum
Version:        0.3.2
Release:        0
Summary:        Asylum like game
License:        GPL-3.0-or-later AND SUSE-Public-Domain
Group:          Amusements/Games/Logic
Url:            http://sdl-asylum.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Asylum/%{version}/%{oname}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch1:         return-in-nonvoid.diff
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Young Sigmund has a few problems. To help him resolve his mental instability
you must enter the surreal world of his inner mind and shut down the
malfunctioning brain cells.

SDL Asylum is a C port of the computer game Asylum, which was written by Andy
Southgate in 1994 for the Acorn Archimedes and is now public domain.

%prep
%setup -q -n asylum-%{version}
%patch -P 1 -p1

# SED-FIX-OPENSUSE -- Fix Paths and Highscore
sed -i -e 's|/usr/games/asylum|$(DESTDIR)/usr/bin/%{name}|;
           s|/usr/share/games/asylum|$(DESTDIR)/usr/share/%{name}|;
           s|/var/games/asylum|$(DESTDIR)/var/games/%{name}|;
           s|$(CHGRP) $(INSTALLGROUP)|#$(CHGRP) $(INSTALLGROUP)|;
           s|$(CHGRP) -R $(INSTALLGROUP)|#$(CHGRP) -R $(INSTALLGROUP)|' Makefile

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%make_install

# install icon
install -Dm 0644 %{S:1} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING Instruct README
%attr(0755,root,games) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%dir %{_localstatedir}/games/
%attr(0755,root,games) %{_localstatedir}/games/%{name}
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/EgoHighScores
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/ExtendedHighScores
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/IdHighScores
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/PsycheHighScores

%changelog
