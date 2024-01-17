#
# spec file for package perl-DBICx-Sugar
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


Name:           perl-DBICx-Sugar
Version:        0.0200
Release:        0
%define cpan_name DBICx-Sugar
Summary:        Just some syntax sugar for DBIx::Class
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(SQL::Translator) >= 0.11018
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(YAML)
Requires:       perl(DBIx::Class)
Requires:       perl(Module::Load)
Requires:       perl(SQL::Translator) >= 0.11018
Requires:       perl(YAML)
Recommends:     perl(DBIx::Class::Schema::Loader) >= 1
%{perl_requires}

%description
Just some syntax sugar for your DBIx::Class applications. This was
originally created to remove code duplication between Dancer::Plugin::DBIC
and Dancer2::Plugin::DBIC.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc CHANGES README
%license LICENSE

%changelog
