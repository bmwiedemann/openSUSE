#
# spec file for package sc-im
#
# Copyright (c) 2025 SUSE LLC
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


Name:           sc-im
Version:        0.8.5
Release:        0
Summary:        An ncurses spreadsheet program for terminal
License:        BSD-4-Clause
Group:          Productivity/Office/Spreadsheets
URL:            https://github.com/andmarti1424
Source0:        https://github.com/andmarti1424/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  gnuplot
BuildRequires:  make
BuildRequires:  pkgconfig(libxls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(ncurses)
# Currently causing build failures as of libxlsxwriter 1.2.2
# See gh#andmarti1424/sc-im#948 for bug report
# BuildRequires:  pkgconfig(xlsxwriter)

%description
Spreadsheet Calculator Improvised, aka sc-im, is an ncurses based,
vim-like spreadsheet calculator.

sc-im is based on sc, whose original authors are James Gosling and
Mark Weiser, and mods were later added by Chuck Martin.

%prep
%setup -q

%build
%make_build -C src prefix=/usr

%install
%make_install -C src prefix=/usr

%files
%license LICENSE
%doc BUGS CHANGES HELP KNOWN_ISSUES Readme.md
%{_bindir}/%{name}
%{_bindir}/scopen
%dir %{_datadir}/%{name}
%{_datadir}/themes/*
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1.*

%changelog
