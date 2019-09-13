#
# spec file for package ceferino
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


%define _lver 0.97.9
%define _svnrev svn37
Name:           ceferino
Version:        %{_lver}_%{_svnrev}
Release:        0
Summary:        Game similar to Super Pang
License:        GPL-2.0
Group:          Amusements/Games/Arcade
Url:            http://www.losersjuegos.com.ar/juegos/ceferino
# Downloaded from https://code.google.com/p/donceferino
# Packed as tar.bz2
Source0:        %{name}-%{_lver}+%{_svnrev}.tar.bz2
Source1:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  python-setuptools
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A game similar to 'Super Pang'. You are attacked by little green balls
which are bouncing around and which you have to destroy with your knife.

Your knife however is limited to being thrown upwards, thus you have
to get under the balls to destroy them. Even worse, if you destroy
a large ball, it doesn't just vanish, but breaks apart into two smaller balls.
Levels consist of little platforms connected by ladders, so you can go
up and down or find cover if needed.

%prep
%setup -q -n %{name}

%build
autoreconf -fi

%configure
make %{?_smp_mflags} -Wall

%install
%make_install

# install icon
install -Dm 0644 data/ima/icono.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
# link the icon back to the install directory. In preparation for app containerisation, as well
# as AppStream metadata generation, we need a real file in /usr/share/icons
# fdupes later on is likely to put the symlink there though
ln -sf %{_datadir}/icons/hicolor/32x32/apps/%{name}.png %{buildroot}%{_datadir}/%{name}/ima/icono.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}editor
%{_bindir}/%{name}setup
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
