#
# spec file for package perl-MooX-Options
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooX-Options
Version:        4.103
Release:        0
%define cpan_name MooX-Options
Summary:        Explicit Options eXtension for Object Class
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long) >= 2.43
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.099
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(MooX::Locale::Passthrough)
BuildRequires:  perl(Path::Class) >= 0.32
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Text::LineFold)
BuildRequires:  perl(strictures) >= 2
Requires:       perl(Getopt::Long) >= 2.43
Requires:       perl(Getopt::Long::Descriptive) >= 0.099
Requires:       perl(MRO::Compat)
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 1.003
Requires:       perl(MooX::Locale::Passthrough)
Requires:       perl(Path::Class) >= 0.32
Requires:       perl(Text::LineFold)
Requires:       perl(strictures) >= 2
Recommends:     perl(Data::Record)
Recommends:     perl(JSON::MaybeXS)
Recommends:     perl(Regexp::Common)
%{perl_requires}

%description
Create a command line tool with your Moo, Moose objects.

Everything is explicit. You have an 'option' keyword to replace the usual
'has' to explicitly use your attribute into the command line.

The 'option' keyword takes additional parameters and uses
Getopt::Long::Descriptive to generate a command line tool.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes coverage.txt README.md
%license LICENSE

%changelog
