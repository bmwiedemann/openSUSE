#
# spec file for package hexedit
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


Name:           hexedit
Version:        1.5
Release:        0
Summary:        Hexadecimal editor for binary files
License:        GPL-2.0-or-later
Group:          Development/Tools/Editor
URL:            https://github.com/pixel/hexedit
Source0:        https://github.com/pixel/hexedit/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         hexedit-Prevent-division-by-zero-on-empty-files.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)

%description
Terminal binary file editor - edit and search hexadecimal and text.
For the times when hexdump shows something you did not want to see.

%prep
%setup -q
%autopatch -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install \
    mandir=%{_mandir}

%files
%license COPYING
%doc Changes
%{_mandir}/man*/*
%{_bindir}/*

%changelog
