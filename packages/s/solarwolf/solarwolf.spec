#
# spec file for package solarwolf
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


Name:           solarwolf
Version:        1.5
Release:        0
Summary:        Action/arcade game originally based on SolarFox
License:        LGPL-2.1+
Group:          Amusements/Games/Action/Arcade
Url:            http://www.pygame.org/shredwheat/solarwolf/index.shtml
Source0:        http://www.pygame.org/shredwheat/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        solar-wolf-logo-64.png
Source4:        %{name}-rpmlintrc
%if 0%{?suse_version}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  python
Requires:       libmikmod
Requires:       pygame
BuildArch:      noarch

%description
The point of this game is to scramble through 48 levels of patterns,
collecting all the boxes. The part that makes it tricky is avoiding the
relentless hailstorm of fire coming at you from all directions.

Authors:
--------
    Pete Shinners <pete@shinners.org>

%prep
%setup
find -type d | xargs chmod 755

# Remove not needed files
rm -rf data/.xvpics

%build

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{code,data}
for d in code data ; do
    cp -r "$d"/* %{buildroot}%{_datadir}/%{name}/"$d"
done

# install files
install -Dm 0755 %{name}.py %{buildroot}%{_datadir}/%{name}

# install icon
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop

python -m compileall -d %{_datadir}/%{name} %{buildroot}%{_datadir}/%{name}
python -O -m compileall -d %{_datadir}/%{name} %{buildroot}%{_datadir}/%{name}

%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
