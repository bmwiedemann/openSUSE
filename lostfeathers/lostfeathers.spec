#
# spec file for package lostfeathers
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


Name:           lostfeathers
Version:        1.0b
Release:        0
Summary:        Help a bird to recover his magical feathers
License:        BSD-3-Clause
Group:          Amusements/Games/Action/Arcade
Url:            https://code.google.com/p/lostfeathers/
Source0:        http://lostfeathers.googlecode.com/files/%{name}-%{version}.zip
Source1:        %{name}.sh
Source2:        %{name}.png
Source3:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  unzip
Requires:       python
Requires:       python-pygame
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Lost Feathers

You control a boy and his bird named Py. Your goal is to recover Py's
magical feathers, which were stolen by Evil Businessman.

Help a bird to recover his magical feathers.

%prep
%setup -q

# Some docs have the DOS line ends
dos2unix README.txt

# Correct Permissions
chmod 0644 pyglet/gl/wgl.py
chmod 0555 cocos/euclid.py cocos/tiles.py

%build

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{cocos,data,gamelib,pyglet}
for d in cocos data gamelib pyglet ; do
    cp -a $d %{buildroot}%{_datadir}/%{name}
done

# install files
install -Dm 0555 run_game.py %{buildroot}%{_datadir}/%{name}

# install icon
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
