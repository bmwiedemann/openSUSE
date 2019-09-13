#
# spec file for package openarena-data
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


Name:           openarena-data
Version:        0.8.8
Release:        0
Summary:        Data files for Open Arena
License:        GPL-2.0+
Group:          Amusements/Games/Action/Shoot
Url:            http://openarena.ws/
Source:         http://download.tuxfamily.org/openarena/rel/088/openarena-0.8.8.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  unzip
Requires:       openarena = %{version}
BuildArch:      noarch
NoSource:       0
Provides:       openarena-doc = %version-%release
Obsoletes:      openarena-doc < %version-%release

%description
OpenArena is a content package for the Quake III Arena engine,
effectively creating a free/libre stand-alone game.

This package contains only platform-independent data files like
maps, player models, weapon models, etc.

%prep
%setup -q -n openarena-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/games/openarena/baseoa
install baseoa/* %{buildroot}%{_datadir}/games/openarena/baseoa
mkdir -p %{buildroot}/%{_datadir}/games/openarena/missionpack
install missionpack/* %{buildroot}%{_datadir}/games/openarena/missionpack
mkdir -p %{buildroot}/%{_docdir}/games/openarena
install LINUX* C* README readme* WENEED %{buildroot}/%{_docdir}/games/openarena

%files
%defattr(-,root,root)
%dir %{_datadir}/games/openarena
%dir %{_datadir}/games/openarena/baseoa
%attr(644,root,root) %{_datadir}/games/openarena/baseoa/*
%dir %{_datadir}/games/openarena/missionpack
%attr(644,root,root) %{_datadir}/games/openarena/missionpack/*
%dir %{_docdir}/games
%dir %{_docdir}/games/openarena
%attr(644,root,root) %{_docdir}/games/openarena/*

%changelog
