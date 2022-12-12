#
# spec file for package perl-Curses
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Curses
Name:           perl-Curses
Version:        1.43
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Terminal screen handling and optimization
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GI/GIRAFFED/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  ncurses5-devel
# MANUAL END

%description
'Curses' is the interface between Perl and your system's curses(3) library.
For descriptions on the usage of a given function, variable, or constant,
consult your system's documentation, as such information invariably varies
(:-) between different curses(3) libraries and operating systems. This
document describes the interface itself, and assumes that you already know
how your system's curses(3) library works.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i '1s| /usr//bin/perl|%{__perl}|' demo.form
sed -i '1s| /usr/bin/perl|%{__perl}|' demo* gdc testsyms
chmod +x makeConfig
# MANUAL END

%build
export CURSES_CFLAGS="-I/usr/include/ncurses5/ncursesw"
export CURSES_LDFLAGS="-L%{_libdir}/ncurses5 -lncursesw"
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" PANELS MENUS FORMS
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog demo demo2 demo.form demo.menu demo.panel HISTORY MAINTENANCE README
%license Artistic Copying

%changelog
