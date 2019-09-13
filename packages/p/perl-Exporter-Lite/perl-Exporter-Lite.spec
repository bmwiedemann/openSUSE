#
# spec file for package perl-Exporter-Lite
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Exporter-Lite
Version:        0.08
Release:        0
%define cpan_name Exporter-Lite
Summary:        Lightweight Exporting of Functions and Variables
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Exporter-Lite/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Exporter::Lite is an alternative to Exporter, intended to provide a
lightweight subset of the most commonly-used functionality. It supports
'import()', '@EXPORT' and '@EXPORT_OK' and not a whole lot else.

Unlike Exporter, it is not necessary to inherit from Exporter::Lite; Ie you
don't need to write:

 @ISA = qw(Exporter::Lite);

Exporter::Lite simply exports its import() function into your namespace.
This might be called a "mix-in" or a "role".

Setting up a module to export its variables and functions is simple:

    package My::Module;
    use Exporter::Lite;

    our @EXPORT = qw($Foo bar);

Functions and variables listed in the '@EXPORT' package variable are
automatically exported if you use the module and don't explicitly list any
imports. Now, when you 'use My::Module', '$Foo' and 'bar()' will show up.

Optional exports are listed in the '@EXPORT_OK' package variable:

    package My::Module;
    use Exporter::Lite;

    our @EXPORT_OK = qw($Foo bar);

When My::Module is used, '$Foo' and 'bar()' will _not_ show up, unless you
explicitly ask for them:

    use My::Module qw($Foo bar);

Note that when you specify one or more functions or variables to import,
then you must also explicitly list any of the default symbols you want to
use. So if you have an exporting module:

    package Games;
    our @EXPORT    = qw/ pacman defender  /;
    our @EXPORT_OK = qw/ galaga centipede /;

Then if you want to use both 'pacman' and 'galaga', then you'd write:

    use Games qw/ pacman galaga /;

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
