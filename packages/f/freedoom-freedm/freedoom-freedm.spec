#
# spec file for package freedoom-freedm
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           freedoom-freedm
Version:        0.12.1
Release:        0
Summary:        Deathmatch levels for Doom
License:        BSD-3-Clause
Group:          Amusements/Games/3D/Shoot
Url:            https://freedoom.github.io/
Source:         https://github.com/freedoom/freedoom/releases/download/v%{version}/freedm-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  unzip
Requires:       freedoom

%description
A set of deathmatch levels for the DOOM game engine, based on the
freely redistributable Freedoom game files.

%prep
%setup -q -n freedm-%{version}

%build
# Game data files.  Nothing to build!

%install
install -D -m 0644 freedm.wad %{buildroot}%{_datadir}/doom/freedm.wad

%files
%defattr(-,root,root)
%doc CREDITS.txt freedoom-manual.pdf README.html
%license COPYING.txt
%{_datadir}/doom/

%changelog
