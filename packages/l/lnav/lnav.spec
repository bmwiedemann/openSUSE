#
# spec file for package lnav
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2010-2013 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           lnav
Version:        0.13.1
Release:        0
Summary:        Logfile Navigator
License:        BSD-2-Clause
Group:          System/Monitoring
URL:            https://lnav.org
#Git-Clone:     https://github.com/tstack/lnav.git
Source:         https://github.com/tstack/lnav/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  c++_compiler
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(doctest)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sqlite3) >= 3.9.0
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
The Logfile Navigator, lnav for short, is a curses-based tool for viewing and
analyzing log files. The value added by lnav over text viewers or editors is
that it takes advantage of any semantic information that can be gleaned from
the log file, such as timestamps and log levels. Using this extra semantic
information, lnav can do things like interleaving messages from different
files, generate histograms of messages over time, and provide hotkeys for
navigating through the file. These features are meant to allow the user to
quickly and efficiently focus on problems.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%configure \
     --disable-silent-rules \
     --disable-static \
     --with-system-doctest \
     --with-ncurses \
     --with-readline
#     --with-yajl       local copy contains changes that will probably be merged for next release (after 2.1.0).

%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS NEWS.md README
%{_bindir}/lnav
%{_mandir}/man1/lnav.1%{?ext_man}

%changelog
