#
# spec file for package fillets-ng-data
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


Name:           fillets-ng-data
Version:        1.0.1
Release:        0
Summary:        Game Data for Fish Fillets - Next Generation
License:        GPL-2.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://fillets.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/fillets/%{name}-%{version}.tar.gz
Source1:        fillets-ng-data-rpmlintrc
Requires:       fillets-ng >= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# as we just copy files around, there is no need for "sources"
NoSource:       0

%description
Fish Fillets is strictly a puzzle game. The goal in each of the 70
levels is always the same: to find a safe way out. The fish utter witty
remarks about their surroundings and the various inhabitants of their
underwater realm quarrel among themselves or comment on the efforts of
your fish. The whole game is accompanied by quiet, comforting music.

This package contains data for the game.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/fillets-ng
cp -r * %{buildroot}%{_datadir}/fillets-ng/

%files
%defattr(-,root,root)
%dir %{_datadir}/fillets-ng
%{_datadir}/fillets-ng/*

%changelog
