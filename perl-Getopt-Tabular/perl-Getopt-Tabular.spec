#
# spec file for package perl-Getopt-Tabular
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Getopt-Tabular
Name:           perl-Getopt-Tabular
Version:        0.3
Release:        0
Summary:        table-driven argument parsing for Perl 5
License:        GPL-2.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Getopt-Tabular/
Source:         http://www.cpan.org/authors/id/G/GW/GWARD/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#BuildRequires: perl(Getopt::Tabular)
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

* argument

  any single word appearing on the command-line, i.e. one element of the
  '@ARGV' array.

* option

  an argument that starts with a certain sequence of characters; the
  default is "-". (If you like GNU-style options, you can change this to
  "--".) In most Getopt::Tabular-based applications, options can come
  anywhere on the command line, and their order is unimportant (unless one
  option overrides a previous option). Also, Getopt::Tabular will allow any
  non-ambiguous abbreviation of options.

* option argument

  (or _value_) an argument that immediately follows certain types of
  options. For instance, if '-foo' is a scalar-valued integer option, and
  '-foo 3' appears on the command line, then '3' will be the argument to
  '-foo'.

* option type

  controls how 'GetOptions' deals with an option and the arguments that
  follow it. (Actually, for most option types, the type interacts with the
  'num_values' field, which determines whether the option is scalar- or
  vector-valued. This will be fully explained in due course.)

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes demo README

%changelog
