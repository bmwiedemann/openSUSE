#
# spec file for package quakespasm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Luke Jones <luke.nukem.jones@gmail.com>
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


Name:           quakespasm
Version:        0.93.1
Release:        0
Summary:        A Quake Engine
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
Url:            http://quakespasm.sourceforge.net/
Source:         http://ufpr.dl.sourceforge.net/project/quakespasm/Source/%{name}-%{version}.tgz
Source100:      quakespasm.appdata.xml
Source99:       %{name}.changes
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(vorbis)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QuakeSpasm is a Quake 1 engine based on the SDL2 port of FitzQuake.  It includes
64-bit CPU support, a new sound driver, several networking fixes and a few
graphical niceities, while also staying true to the original game.
Game data must be placed in ~/.quakespasm/id1 .

%prep
%setup
# Fix usage of __DATE__ and __TIME__ macros to prevent build in excess
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" Quake/host.c
# Prepare for later installation
mkdir html/
ln -s README.html ./html/README.html
mv Quakespasm.txt README
mv Quakespasm-Music.txt MUSIC
mv LICENSE.txt LICENSE

%build
export CFLAGS='%{optflags} -DQUAKE_BASEDIR=\"%{_datadir}/quake\"'
make %{?_smp_mflags} -C Quake\
    DO_USERDIRS=1 \
    USE_CODEC_MP3=0 \
    USE_SDL2=1

%install
install -D -p -m 755 Quake/quakespasm %{buildroot}%{_bindir}/quakespasm
install -D -p -m 644 Misc/QuakeSpasm_512.png %{buildroot}%{_datadir}/pixmaps/quakespasm.png
install -D -p -m 644 %{SOURCE100}  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -d -m 755 %{buildroot}%{_datadir}/quake/

%suse_update_desktop_file -c %{name} 'Quake' 'QuakeSpasm' %{name} %{name} Game ActionGame

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc README MUSIC LICENSE html/
%{_bindir}/%{name}
%dir %{_datadir}/quake/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Leap 42.1 or SLE
%dir %{_datadir}/appdata
%endif
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
