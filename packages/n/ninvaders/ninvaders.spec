#
# spec file for package ninvaders
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ninvaders
Version:        0.1.1
Release:        0
Summary:        A space invaders-like game using ncurses
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            http://ninvaders.sourceforge.net/
Source:         http://downloads.sourceforge.net/ninvaders/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE buffer_owerflow.patch
# fix buffer owerflow that leads to an build error in Leap 15+
Patch0:         buffer_owerflow.patch
Patch1:         ninvaders-obey-cflags.patch
BuildRequires:  ncurses-devel

%description
A Space Invaders type game with text-only graphics.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags} -fcommon"
make %{?_smp_mflags}

%install
install -Dm 0755 nInvaders %{buildroot}%{_bindir}/%{name}

%files
%doc ChangeLog README
%license gpl.txt
%{_bindir}/%{name}

%changelog
