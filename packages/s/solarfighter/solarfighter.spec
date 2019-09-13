#
# spec file for package solarfighter
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


Name:           solarfighter
Version:        proto.1
Release:        0
Summary:        Action/arcade game originally based on Solarwolf
License:        LGPL-2.1+
Group:          Amusements/Games/Action/Arcade
Url:            http://posor.eu/solarfighter/solarfighter.htm
Source0:        http://posor.eu/solarfighter/solarfighter_proto1.tar.bz2
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}-rpmlintrc
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
SolarFighter. Are you ready for the hardest fights in this solar system?
You are not sure? Well, then try this great game and find out!
SolarFighter is our new arcade style space shooter. In contrast to other
games of this genre, it features highly intelligent opponents and realistic
physics. This work is based on Solarwolf 1.5 written by Pete Shinners.

%prep
%setup -q -n SolarFighter
find -type d | xargs chmod 755

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
install -Dm 0755 *.py %{buildroot}%{_datadir}/%{name}

# install icon
install -Dm 0644 data/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

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
%attr(0664,root,root)%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
