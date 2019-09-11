#
# spec file for package vegastrike-speech
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vegastrike-speech
Version:        0.5.1.r1
Release:        0
Summary:        Speech files for Vega Strike
License:        GPL-2.0+
Group:          Amusements/Games/3D/Simulation
Url:            http://vegastrike.sourceforge.net/
# This is the music budle
Source0:        http://downloads.sourceforge.net/project/vegastrike/vegastrike/0.5.1/%{name}-%{version}.tar
Source1:        COPYING
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       vegastrike-data >= %{version}
Conflicts:      vegastrike-data < %{version}
ExcludeArch:    %{ix86}

%description
Optional speech files, so you can hear characters speak, 
for Vega Strike, a GPL 3D OpenGL Action RPG space sim 
that allows a player to trade and bounty hunt.

This package is not required to play Vega Strike. 


%prep
%setup -q

%build
# nothing to build; data only

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vegastrike
find communications/sounds -type f -exec install -p -m 644 -D {} $RPM_BUILD_ROOT%{_datadir}/vegastrike/{} \;
find sounds -type f -exec install -p -m 644 -D {} $RPM_BUILD_ROOT%{_datadir}/vegastrike/{} \;
cp %{SOURCE1} .

%files
%defattr(-,root,root,-)
%{_datadir}/vegastrike
%doc COPYING

%changelog
