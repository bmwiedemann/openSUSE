#
# spec file for package powermanga
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           powermanga
Version:        0.93.1
Release:        0
Summary:        Arcade 2D shoot-them-up game
License:        GPL-3.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://linux.tlk.fr/games/Powermanga/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.sh
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)

%description
In this "shoot 'em up" with 3d graphics, you'll have to face
and destroy more than 60 different types of opponents.
Nice musics, many weapons, and a ton of surprises.

%prep
%setup -q

# Default to English
sed -i 's|fr|en|' texts/config.ini

%build
autoreconf -fi
%configure LIBS=-lm
make %{?_smp_mflags} CFLAGS="%{optflags} -std=c99"

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install executables and mans
install -Dm 0755 src/%{name} %{buildroot}%{_libexecdir}/%{name}/%{name}
install -Dm 0644 %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6
install -Dm 0644 man/%{name}.fr.6 %{buildroot}%{_mandir}/fr/man6/%{name}.6

# install Games data
for d in data graphics order sounds texts ; do
    cp -r $d %{buildroot}%{_libexecdir}/%{name}/
done

# Remove not needed files
find %{buildroot}%{_libexecdir}/%{name} -name 'Makefile*' -exec rm -f {} ';'

# install icons
for i in 16 32 48 ; do
    install -Dm 0644 images_for_menu_entry/%{name}.${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
install -Dm 0644 images_for_menu_entry/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install desktop file
install -Dm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# install score
mkdir -p %{buildroot}%{_localstatedir}/games/%{name}
touch %{buildroot}%{_localstatedir}/games/%{name}/{powermanga.hi-easy,powermanga.hi,powermanga.hi-hard}

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES COPYING README
%{_bindir}/%{name}
%{_mandir}/fr
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/%{name}.png
%{_libexecdir}/%{name}
%dir %{_localstatedir}/games/
%attr(0755,root,games) %{_localstatedir}/games/%{name}
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/%{name}.hi
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/%{name}.hi-easy
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}/%{name}.hi-hard

%changelog
