#
# spec file for package lpairs
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


Name:           lpairs
Version:        1.0.4
Release:        0
Summary:        Classical memory game
License:        GPL-2.0
Group:          Amusements/Games/Arcade/LogicGame
Url:            http://lgames.sourceforge.net/index.php?project=LPairs
Source0:        http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(sdl)

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed
will be counted but there is no highscore chart or limit to this.

%prep
%setup -q

# Replace game path
sed -i 's|games/lpairs|lpairs|' configure

%build

export CFLAGS="%{optflags} -fgnu89-inline"
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} install
%find_lang %name

# install icon
install -Dm 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install desktop
install -Dm 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
