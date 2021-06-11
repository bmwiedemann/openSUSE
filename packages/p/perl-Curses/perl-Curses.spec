#
# spec file for package perl-Curses
#
# Copyright (c) 2021 SUSE LLC
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


Name:           perl-Curses
Version:        1.37
Release:        0
%define cpan_name Curses
Summary:        Terminal screen handling and optimization
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

# Fix perl script interpreters
sed -i '1s|../../perl|%{__perl}|' test.syms
sed -i '1s| /usr//bin/perl|%{__perl}|' demo.form
sed -i '1s| /usr/bin/perl|%{__perl}|' demo* gdc

%build
export CURSES_CFLAGS="-I/usr/include/ncurses5/ncursesw"
export CURSES_LDFLAGS="-L%{_libdir}/ncurses5 -lncursesw"
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" PANELS MENUS FORMS
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc demo* gdc gen.tar HISTORY list.syms MAINTENANCE README testcurses test.syms
%license Artistic Copying

%changelog
