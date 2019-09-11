#
# spec file for package perl-Curses
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


Name:           perl-Curses
Version:        1.36
Release:        0
Summary:        Terminal screen handling and optimization
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://cpan.org/modules/by-module/Curses/
Source0:        Curses-%{version}.tar.gz
Source1:        https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/Curses-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       Curses
Provides:       perl_cur
Obsoletes:      perl_cur
%{perl_requires}

%description
Curses is the interface between Perl and your system's curses(3) library.
For descriptions on the usage of a given function, variable, or constant,
consult your system's documentation, as such information invariably varies
(:-) between different curses(3) libraries and operating systems. This
document describes the interface itself, and assumes that you already know
how your system's curses(3) library works.

%prep
%setup -q -n Curses-%{version}

%build
CURSES_LDFLAGS="-lncursesw" CURSES_CFLAGS="-I/usr/include/ncursesw/" perl Makefile.PL PANELS MENUS OPTIMIZE="%{optflags} -Wall"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist
chmod a-x test.syms demo.form

%files
%license Copying
%doc README Artistic demo demo2 demo.form demo.menu demo.panel HISTORY list.syms MAINTENANCE README test.syms
%{_mandir}/man3/*
%{perl_vendorarch}/Curses.pm
%{perl_vendorarch}/auto/Curses

%changelog
