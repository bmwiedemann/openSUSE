#
# spec file for package gperiodic
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


Name:           gperiodic
Version:        3.0.3
Release:        0
Summary:        A program for looking up data of elements from the periodic table 
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            http://gperiodic.sf.net/

Source:         http://download.sf.net/gperiodic/%name-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-2.0)

%description
GPeriodic is a program for looking up data of elements from the
periodic table. This program also features a non-graphical interface.

%lang_package

%prep
%autosetup -p1

%build
%make_build CFLAGS="%optflags"

%install
%make_install
%find_lang %name
%fdupes %buildroot/%_prefix

%files
%_bindir/gperiodic
%_mandir/man1/gperiodic*
%_datadir/applications/gperiodic*
%_datadir/icons/*
%_datadir/pixmaps/gperiodic*
%license gpl.txt

%files lang -f %name.lang

%changelog
