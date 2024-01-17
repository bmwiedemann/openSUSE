#
# spec file for package perl-DBIx-Class-Fixtures
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


Name:           perl-DBIx-Class-Fixtures
Version:        1.001039
Release:        0
%define cpan_name DBIx-Class-Fixtures
Summary:        Dump data and repopulate a database using rules
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBIx-Class-Fixtures/
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAUFMAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Grouped) >= 0.1001
BuildRequires:  perl(Config::Any) >= 0.23
BuildRequires:  perl(DBIx::Class) >= 0.08102
BuildRequires:  perl(DBIx::Class::InflateColumn::FS) >= 0.01007
BuildRequires:  perl(DBIx::Class::Schema::Loader) >= 0.07035
BuildRequires:  perl(Data::Dump::Streamer) >= 2.05
BuildRequires:  perl(Data::Visitor) >= 0.3
BuildRequires:  perl(DateTime) >= 1.03
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::Pg)
BuildRequires:  perl(DateTime::Format::SQLite) >= 0.1
BuildRequires:  perl(Devel::Confess)
BuildRequires:  perl(File::Copy::Recursive) >= 0.38
BuildRequires:  perl(File::Temp) >= 0.2304
BuildRequires:  perl(Hash::Merge) >= 0.1
BuildRequires:  perl(IO::All) >= 0.85
BuildRequires:  perl(JSON::Syck) >= 1.27
BuildRequires:  perl(Path::Class) >= 0.32
BuildRequires:  perl(Scalar::Util) >= 1.27
BuildRequires:  perl(Test::Compile::Internal)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::TempDir::Tiny)
Requires:       perl(Class::Accessor::Grouped) >= 0.1001
Requires:       perl(Config::Any) >= 0.23
Requires:       perl(DBIx::Class) >= 0.08102
Requires:       perl(DBIx::Class::Schema::Loader) >= 0.07035
Requires:       perl(Data::Dump::Streamer) >= 2.05
Requires:       perl(Data::Visitor) >= 0.3
Requires:       perl(DateTime) >= 1.03
Requires:       perl(DateTime::Format::MySQL)
Requires:       perl(DateTime::Format::Pg)
Requires:       perl(DateTime::Format::SQLite) >= 0.1
Requires:       perl(File::Copy::Recursive) >= 0.38
Requires:       perl(File::Temp) >= 0.2304
Requires:       perl(Hash::Merge) >= 0.1
Requires:       perl(IO::All) >= 0.85
Requires:       perl(JSON::Syck) >= 1.27
Requires:       perl(Path::Class) >= 0.32
Requires:       perl(Scalar::Util) >= 1.27
%{perl_requires}

%description
Dump fixtures from source database to filesystem then import to another
database (with same schema) at any time. Use as a constant dataset for
running tests against or for populating development databases when
impractical to use production clones. Describe fixture set using relations
and conditions based on your DBIx::Class schema.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%license LICENSE

%changelog
