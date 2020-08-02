#
# spec file for package xteddy
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


Name:           xteddy
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Provides:       xteddy10
Requires:       imlib2-loaders
Summary:        A cuddly teddy bear for your X Window desktop
License:        GPL-2.0+
Group:          Amusements/Toys/Graphics
Version:        2.2
Release:        0
Source:         xteddy_2.2.orig.tar.bz2
Patch:          teddy-2.2-as-needed.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://webstaff.itn.liu.se/~stegu/xteddy/

%description
Normally, xteddy just sits around doing nothing. After all, that's what
teddy bears are for. Look at him, talk to him, place heavy windows on
top of him, zap him around until he becomes dizzy, do what you like; he
will always be your true (albeit virtual) friend.

You can move xteddy with the mouse by pointing at him and dragging him
around. When clicked upon, he will pop up on top of all other windows.
If you type "q" on him, he will die (or, as I like to think of it, be
tucked away in the file system until you need him next time).

That's it. But he's cute.



Authors:
--------
    Stefan Gustavson <stefang@isy.liu.se>

%prep
%setup -q
%patch
sed -i s,/usr/games,/usr/bin, xtoys

%build
autoreconf --force --install
%configure 
%{__make} %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
#cd $RPM_BUILD_ROOT/usr/X11R6/bin/ && ln xteddy xpenguin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc	html/*.html
%doc	html/images
	%{_bindir}/*
	%{_mandir}/man6/*
	%{_datadir}/%{name}
#

%changelog
