#
# spec file for package aop
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


Name:           aop
Version:        0.6
Release:        0
Summary:        Ncurses based arcade game with only 64 lines of code
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://raffi.at/view/code/aop
Source0:        http://raffi.at/code/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
# PATCH-FIX-OPENSUSE - aop-Makefile.patch -- Fix build and installation
Patch0:         %{name}-Makefile.patch
# PATCH-FIX-OPENSUSE - aop-aop.c.patch-- Fix lifes and where are levels
Patch1:         %{name}-aop.c.patch
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
%if 0%{?suse_version} < 1320
BuildRequires:  ncurses-devel
%else
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ambassador of Pain is a curses based arcade game for Linux/UNIX
with only 64 lines of sourcecode.

The goal is to drive the hoovercraft (O) trough the level into
the 'at' sign (@) and reach as much points as possible by reducing
the number of moves and don't losing any time.
Lost lifes (0) can easily be picked up by simply drive over them.

%prep
%setup -q
%patch0
%patch1

%build
%if 0%{?suse_version} < 1320
CFLAGS="%optflags $(ncursesw6-config --cflags)"
LIBS="$(ncursesw6-config --libs)"
%else
CFLAGS="%optflags $(pkg-config ncurses --cflags)"
LIBS="$(pkg-config ncurses --libs)"
%endif

make %{?_smp_mflags} CFLAGS="$CFLAGS" LIBS="$LIBS"

%install
%make_install

# install icon
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
