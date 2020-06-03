#
# spec file for package perl-SQL-Abstract
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


Name:           perl-SQL-Abstract
Version:        1.87
Release:        0
%define cpan_name SQL-Abstract
Summary:        Generate SQL from Perl data structures
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(MRO::Compat) >= 0.12
BuildRequires:  perl(Moo) >= 2.000001
BuildRequires:  perl(Sub::Quote) >= 2.000001
BuildRequires:  perl(Test::Builder::Module) >= 0.84
BuildRequires:  perl(Test::Deep) >= 0.101
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::Balanced) >= 2.00
Requires:       perl(Hash::Merge) >= 0.12
Requires:       perl(MRO::Compat) >= 0.12
Requires:       perl(Moo) >= 2.000001
Requires:       perl(Sub::Quote) >= 2.000001
Requires:       perl(Test::Builder::Module) >= 0.84
Requires:       perl(Test::Deep) >= 0.101
Requires:       perl(Text::Balanced) >= 2.00
%{perl_requires}

%description
This module was inspired by the excellent DBIx::Abstract. However, in using
that module I found that what I really wanted to do was generate SQL, but
still retain complete control over my statement handles and use the DBI
interface. So, I set out to create an abstract SQL generation module.

While based on the concepts used by DBIx::Abstract, there are several
important differences, especially when it comes to WHERE clauses. I have
modified the concepts used to make the SQL easier to generate from Perl
data structures and, IMO, more intuitive. The underlying idea is for this
module to do what you mean, based on the data structures you provide it.
The big advantage is that you don't have to modify your code every time
your data changes, as this module figures it out.

To begin with, an SQL INSERT is as easy as just specifying a hash of
'key=value' pairs:

    my %data = (
        name => 'Jimbo Bobson',
        phone => '123-456-7890',
        address => '42 Sister Lane',
        city => 'St. Louis',
        state => 'Louisiana',
    );

The SQL can then be generated with this:

    my($stmt, @bind) = $sql->insert('people', \%data);

Which would give you something like this:

    $stmt = "INSERT INTO people
                    (address, city, name, phone, state)
                    VALUES (?, ?, ?, ?, ?)";
    @bind = ('42 Sister Lane', 'St. Louis', 'Jimbo Bobson',
             '123-456-7890', 'Louisiana');

These are then used directly in your DBI code:

    my $sth = $dbh->prepare($stmt);
    $sth->execute(@bind);

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README
%license LICENSE

%changelog
