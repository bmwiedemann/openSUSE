#
# spec file for package asteroids3D
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           asteroids3D
Version:        0.5.1+
Release:        0
Summary:        First-person shooter blowing up asteroids
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://sf.net/projects/a3d

#Git-Clone:	git://a3d.git.sf.net/gitroot/a3d/a3d
Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  freeglut-devel
BuildRequires:  pkgconfig >= 0.19
BuildRequires:  xz
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)

%description
A simple first person shooter of blowing up asteroids in 3D space.
The codebase also serves as an introduction to trigonometry and
OpenGL.

%prep
%setup -q

%build
%configure --with-gamesdir=%_bindir --with-gamedatadir=%_datadir/games/%name
make %{?_smp_mflags};

%install
make install DESTDIR="%buildroot";

%files
%defattr(-,root,root)
%_bindir/asteroids3D
%_datadir/games/%name

%changelog
