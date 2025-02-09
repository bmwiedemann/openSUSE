#
# spec file for package perl-Getopt-Tabular
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


%define cpan_name Getopt-Tabular
Name:           perl-Getopt-Tabular
Version:        0.300.0
Release:        0
# 0.3 -> normalize -> 0.300.0
%define cpan_version 0.3
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Table-driven argument parsing for Perl 5
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWARD/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Getopt::Tabular) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
*Getopt::Tabular* is a Perl 5 module for table-driven argument parsing,
vaguely inspired by John Ousterhout's Tk_ParseArgv. All you really need to
do to use the package is set up a table describing all your command-line
options, and call &GetOptions with three arguments: a reference to your
option table, a reference to '@ARGV' (or something like it), and an
optional third array reference (say, to '@newARGV'). &GetOptions will
process all arguments in '@ARGV', and copy any leftover arguments (i.e.
those that are not options or arguments to some option) to the '@newARGV'
array. (If the '@newARGV' argument is not supplied, 'GetOptions' will
replace '@ARGV' with the stripped-down argument list.) If there are any
invalid options, 'GetOptions' will print an error message and return 0.

Before I tell you all about why Getopt::Tabular is a wonderful thing, let
me explain some of the terminology that will keep popping up here.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes demo README

%changelog
