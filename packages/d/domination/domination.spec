#
# spec file for package domination
#
# Copyright (c) 2023 SUSE LLC
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


Name:           domination
Version:        1.2.7
Release:        0
Summary:        Board game that is a bit like the well known game Risk
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Turn Based
URL:            http://domination.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Domination/%{version}/Domination_%{version}.zip
Source1:        %{name}-FlashGUI.sh
Source2:        %{name}-Increment1GUI.sh
Source3:        %{name}-SimpleGUI.sh
Source4:        %{name}-SwingGUI.sh
Source5:        %{name}.desktop
Source6:        %{name}.png
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       %{name}-data
Requires:       jre >= 1.6.0
BuildArch:      noarch

%description
Domination is a board game that is a bit like the well known game Risk.

Domination is a game that is a bit like the well known board game of Risk
or RisiKo. It has many game options and includes many maps.

Written in java it includes a map editor, a simple map format, multiplayer
network play, single player, hotseat, 5 user interfaces and many more features,
it works in all OSs that run java.

%prep
%setup -q -n Domination

# Convert to unix line end
find -name "*.txt" -print0 -or -name "*.ini" -print0 -or -name "*.cmd" -print0 \
    -or -name "*.htm" -print0 -or -name "*.cards" -print0 -or -name "*.map" -print0 \
    -or -name "*.properties" -print0 | xargs -0 dos2unix

%build

%install
# install wrappers
install -Dm 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-FlashGUI
install -Dm 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-Increment1GUI
install -Dm 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-SimpleGUI
install -Dm 0755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}-SwingGUI

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{help,lib,maps,maps/preview,resources}
for d in help lib resources ; do
   install -Dm 0644 $d/* %{buildroot}%{_datadir}/%{name}/$d
done

cp -a maps %{buildroot}%{_datadir}/%{name}/

# install files
for f in *.jar *.txt *.ini ; do
    install -Dm 0644 "$f" %{buildroot}%{_datadir}/%{name}
done
# install icon
install -Dm 0644 %{SOURCE6} %{buildroot}%{_datadir}/pixmaps/%{name}.png
# install Desktop file
install -Dm 0644 %{SOURCE5} %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%{_bindir}/%{name}-*GUI
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
