#
# spec file for package sopwith
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


Name:           sopwith
Version:        1.8.4
Release:        0
Summary:        SDL port of the %{name} game
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://sdl-sopwith.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/sdl-sopwith/sdl_%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Patch0:         %{name}-fix-string-include.patch
Patch5:         %{name}-gpl.diff

BuildRequires:  SDL-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme

%description
This is a port of the classic computer game "Sopwith" to run on modern
computers and operating systems.


%prep
%setup -q
rm -f src/font.h
%patch0 -p1
%patch5 -p1
sed -i 's/\r//' doc/readme.txt

%build
%configure --docdir=%{_docdir}
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/doc/%{name}

cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Sopwith
Type=Application
Comment=The classic %{name} game
Exec=%{name}
Terminal=false
Icon=%{name}
EOF

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications           \
  --add-category ArcadeGame                            \
  --add-category Game                                  \
  %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/72x72/apps/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/72x72/apps/

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING FAQ NEWS README TODO doc/keys.txt doc/origdoc.txt doc/readme.txt
%{_bindir}/%{name}
%{_mandir}/man6/%{name}*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
