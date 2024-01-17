#
# spec file for package frozen-bubble
#
# Copyright (c) 2022 SUSE LLC
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


Name:           frozen-bubble
# 2.212 == 2.2.1beta1
Version:        2.212
Release:        0
Summary:        Puzzle with Bubbles
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            http://www.frozen-bubble.org/
Source0:        http://www.frozen-bubble.org/data/frozen-bubble-2.2.1-beta1.tar.bz2
Source1:        fb-server
Source2:        fb-server.service
# PATCH-FIX-OPENSUSE frozen-bubble-2.212-configpath.patch
Patch1:         frozen-bubble-2.212-configpath.patch
# PATCH-FIX-OPENSUSE msgfmt.diff
Patch2:         msgfmt.diff
# PATCH-FIX-UPSTREAM frozen-bubble-2.212-unused-result.patch
Patch3:         frozen-bubble-2.212-unused-result.patch
# PATCH-FEATURE-UPSTREAM https://github.com/kthakore/frozen-bubble/pull/63
Patch4:         desktop.patch
# PATCH-FEATURE-UPSTREAM https://github.com/kthakore/frozen-bubble/pull/64
Patch5:         appdata.patch
# PATCH-FIX-OPENSUSE get a strange check silent - what's the sense of checking snprintf when the buffer size is correct
Patch6:         silencebadsnprintfcheck.patch
BuildRequires:  Mesa-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  perl-SDL >= 2.400
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  perl(Alien::SDL)
BuildRequires:  perl(Compress::Bzip2)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Locale::Maketext::Extract)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Locale::Msgfmt)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Tie::Simple)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(systemd)
# Fix for: Failed loading SDL2 library on openSUSE Leap
%if 0%{?suse_version} <= 1500
BuildRequires:  pkgconfig(sdl2)
%endif
Requires:       %{name}-server = %{version}
Requires:       perl = %{perl_version}
Requires:       perl-SDL >= 2.400
Requires:       perl(Alien::SDL)
Requires:       perl(Compress::Bzip2)
Requires:       perl(Locale::Maketext::Lexicon)
Requires:       perl(Locale::Maketext::Simple)
Requires:       perl(Tie::Simple)
Requires(pre):  %fillup_prereq
Requires(pre):  net-tools
Recommends:     %{name}-lang

%description
Shoot up bubbles. Similar to the console game Puzzle-Bobble.

Colorful 3D rendered penguin animations, 100 levels of 1p game, hours and
hours of 2p game, nights and nights of 2p/3p/4p/5p game over LAN or Internet,
a level-editor, 3 professional quality digital soundtracks, 15 stereo sound
effects, 8 unique graphical transition effects, 8 unique logo eye-candies.

%package server
Summary:        Puzzle with Bubbles - Server
Group:          Amusements/Games/Action/Arcade
Requires(post): coreutils
%{?systemd_requires}

%description server
Server for frozen-bubble.

Colorful 3D rendered penguin animations, 100 levels of 1p game, hours and
hours of 2p game, nights and nights of 2p/3p/4p/5p game over LAN or Internet,
a level-editor, 3 professional quality digital soundtracks, 15 stereo sound
effects, 8 unique graphical transition effects, 8 unique logo eye-candies.

%lang_package

%prep
%setup -q -n frozen-bubble-2.2.1-beta1
cp server/init/README server/README.init
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
perl Build.PL destdir=%{buildroot} installdirs=vendor --prefix=%{_prefix}
./Build manifest
./Build

%check
./Build test

%install
install -d -m 1755 %{buildroot}%{_datadir}/%{name}
./Build install

mv %{buildroot}%{perl_vendorarch}/auto/share/dist/Games-FrozenBubble/* %{buildroot}%{_datadir}/%{name}/

for res in 64x64 48x48 32x32 16x16; do
    install -Dm644 share/icons/frozen-bubble-icon-$res.png %{buildroot}%{_datadir}/icons/hicolor/$res/apps/%{name}.png
done

mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 share/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_datadir}/appdata/
install -m 644 share/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

mkdir -p %{buildroot}%{_unitdir} %{buildroot}/%{_sbindir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/frozen-bubble-server.service
ln -s /sbin/service %{buildroot}%{_sbindir}/rcfb-server
ln -s /sbin/service %{buildroot}%{_sbindir}/rcfrozen-bubble-server

install -d -m 755 %{buildroot}/%{_sysconfdir}
touch %{buildroot}/%{_sysconfdir}/fb-server.conf

%fdupes %{buildroot}${_datadir}
%perl_process_packlist

%post server
%fillup_only
%service_add_post frozen-bubble-server.service
if [ ! -f "%{_sysconfdir}/fb-server.conf" ]; then
  if [ -f "%{_sysconfdir}/language" ]; then
	. %{_sysconfdir}/language
	lang=$(echo ${RC_LANG%*_*})
  fi
  if [ -n "$lang" -o "$lang" = "" ]; then
	lang="en"
  fi
  if [ -x /bin/hostname ]; then
	servername=$(hostname -s)
  else
	servername="testserver"
  fi
  cat > %{_sysconfdir}/fb-server.conf << EOF
# Specify the desired language of the server below (it is just an
# indication used by players when choosing a server, so that
# they can chat using their native language). You can specify none
# with the parameterless option 'z'.
# Name of the server as seen by FB players
n $servername
# Preferred language of players
a $lang
EOF
fi

%postun server
%service_del_postun frozen-bubble-server.service

%pre server
%service_add_pre frozen-bubble-server.service

%preun server
%service_del_preun frozen-bubble-server.service

%files
%license COPYING
%doc AUTHORS README
%dir %{perl_vendorarch}/Games
%dir %{perl_vendorarch}/Games/FrozenBubble
%dir %{perl_vendorarch}/auto/Games
%dir %{perl_vendorarch}/auto/Games/FrozenBubble
%{perl_vendorarch}/Games/FrozenBubble/*
%{perl_vendorarch}/Games/FrozenBubble.pm
%{perl_vendorarch}/auto/Games/FrozenBubble/CStuff*
%{_bindir}/%{name}
%{_bindir}/frozen-bubble-editor
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/locale/*.po
%attr (644,root,root) %{_mandir}/man*/frozen-bubble*
%attr (644,root,root) %{_mandir}/man*/Games*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files server
%license COPYING
%doc server/AUTHORS server/README* server/init/fb-server.conf
%ghost %config(noreplace) %{_sysconfdir}/fb-server.conf
%defattr(755, root, root)
%{_bindir}/fb-server
%attr (644,root,root) %{_unitdir}/frozen-bubble-server.service
%{_sbindir}/rcfb-server
%{_sbindir}/rcfrozen-bubble-server

%files lang
%defattr(-,root,root,-)
# Don't find a solution to install locales on standard directory
%{_datadir}/%{name}/locale/*.po

%changelog
