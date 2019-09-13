#
# spec file for package wumpus
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


%define oname   superhack

Name:           wumpus
Version:        1.6
Release:        0
Summary:        Faithful transcription of the 1974 Atari Wumpus game
License:        BSD-3-Clause
Group:          Amusements/Games/Action/Race
Url:            http://www.catb.org/~esr/wumpus/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source2:        %{name}.desktop
Source3:        %{oname}.desktop
Source4:        %{name}.png
# PATCH-FIX-UPSTREAM - wumpus-Makefile.patch -- Fix paths and installation
Patch0:         %{name}-Makefile.patch
# PATCH-FIX-UPSTREAM - wumpus-superhack.c.patch -- Fix bad C++ code
Patch1:         %{name}-superhack.c.patch
# PATCH-FIX-UPSTREAM - wumpus-wumpus.c.patch -- Fix bad C++ code
Patch2:         %{name}-wumpus.c.patch
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
WUMPUS is a bit of retrocomputing nostalgia. It is an *exact* clone,
even down to the godawful user interface, of an ancient classic game.
This version fixes two minor bugs in my original 1992 USENET posting
of the source. Superhack is a structurally similar game with a
different premise.

%prep
%setup -q
%patch0
%patch1
%patch2

cp -af %{S:2} .
cp -af %{S:3} .
cp -af %{S:4} .

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

# Symlink Manpage
ln -sf %{_mandir}/man6/%{name}.6%{ext_man} %{buildroot}%{_mandir}/man6/%{oname}.6%{ext_man}

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/%{name}
%{_bindir}/%{oname}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_mandir}/man6/%{oname}.6%{ext_man}
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/icons/hicolor/

%changelog
