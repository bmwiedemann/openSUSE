#
# spec file for package phalanx
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define srcname Phalanx
%define srcver  XXV

Name:           phalanx
Url:            http://sourceforge.net/projects/phalanx
Provides:       chess_backend
Version:        25
Release:        0
Source:         http://downloads.sourceforge.net/project/phalanx/Version%20%{srcver}/%{name}-%{srcver}-source.tgz
Patch0:         Phalanx-XXII.diff
# PATCH-FIX-UPSTREAM phalanx-castling-broken.patch bnc#819525 mike.catanzaro@gmail.com -- fix castling always treated as illegal move
Patch1:         phalanx-castling-broken.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A Chess Program
License:        GPL-2.0+
Group:          Amusements/Games/Board/Chess

%description
A smart chess playing program which uses opening book.



Authors:
--------
    Dusan Dobes <dobes@math.muni.cz>

%prep
%setup -q -n %{srcname}-%{srcver}
%patch0 -p1
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
install -d $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/usr/share/phalanx/
install -m 0755 {x,}phalanx $RPM_BUILD_ROOT/usr/bin/
install -m 0644 eco.phalanx pbook.phalanx sbook.phalanx $RPM_BUILD_ROOT/usr/share/phalanx

%files
%defattr(-,root,root)
%doc COPYING HISTORY README
/usr/share/phalanx
/usr/bin/*

%changelog
