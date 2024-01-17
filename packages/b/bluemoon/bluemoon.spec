#
# spec file for package bluemoon
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


Name:           bluemoon
Version:        2.12
Release:        0
Summary:        Blue Moon card solitaire
License:        BSD-3-Clause
Group:          Amusements/Games/Board/Card
Url:            http://www.catb.org/~esr/bluemoon/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - bluemoon-2.12-Makefile.patch -- add $(DESTDIR), png and desktop, fix conflict with bluez
Patch0:         %{name}-2.12-Makefile.patch
# PATCH-FIX-UPSTREAM - bluemoon-2.12-bluemoon.desktop.patch -- change executable
Patch1:         %{name}-2.12-bluemoon.desktop.patch
# PATCH-FIX-UPSTREAM - bluemoon-2.12-bluemoon.c.patch -- fix 'File is compiled without RPM_OPT_FLAGS'
Patch2:         %{name}-2.12-bluemoon.c.patch
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bluemoon - Blue Moon card solitaire

This 52-card solitaire starts with the entire deck shuffled and
dealt out in four rows. The aces are then moved to the left end of
the layout, making 4 initial free spaces. You may move to a space
only the card that matches the left neighbor in suit, and is one
greater in rank. Kings are high, so no cards may be placed to their
right (they create dead spaces).

When no moves can be made, cards still out of sequence are reshuffled
and dealt face up after the ends of the partial sequences, leaving
a card space after each sequence, so that each row looks like a
partial sequence followed by a space, followed by enough cards to
make a row of 14. A moment's reflection will show that this game
cannot take more than 13 deals. A good score is 1-3 deals, 4-7 is
average, 8 or more is poor.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/%{name}-catb
%{_mandir}/man6/%{name}-catb.6%{ext_man}
%{_datadir}/appdata/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
