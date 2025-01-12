#
# spec file for package perl-Data-ObjectDriver
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Data-ObjectDriver
Name:           perl-Data-ObjectDriver
Version:        0.230.0
Release:        0
# 0.23 -> normalize -> 0.230.0
%define cpan_version 0.23
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple, transparent data interface, with caching
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIXAPART/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(DBI)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(version)
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Class::Data::Inheritable)
Requires:       perl(Class::Trigger)
Requires:       perl(DBI)
Provides:       perl(Data::ObjectDriver) = %{version}
Provides:       perl(Data::ObjectDriver::BaseObject)
Provides:       perl(Data::ObjectDriver::BaseView)
Provides:       perl(Data::ObjectDriver::Driver::BaseCache)
Provides:       perl(Data::ObjectDriver::Driver::Cache::Apache)
Provides:       perl(Data::ObjectDriver::Driver::Cache::Cache)
Provides:       perl(Data::ObjectDriver::Driver::Cache::Memcached)
Provides:       perl(Data::ObjectDriver::Driver::Cache::RAM)
Provides:       perl(Data::ObjectDriver::Driver::DBD)
Provides:       perl(Data::ObjectDriver::Driver::DBD::MariaDB)
Provides:       perl(Data::ObjectDriver::Driver::DBD::Oracle)
Provides:       perl(Data::ObjectDriver::Driver::DBD::Oracle::db)
Provides:       perl(Data::ObjectDriver::Driver::DBD::Pg)
Provides:       perl(Data::ObjectDriver::Driver::DBD::SQLite)
Provides:       perl(Data::ObjectDriver::Driver::DBD::mysql)
Provides:       perl(Data::ObjectDriver::Driver::DBI)
Provides:       perl(Data::ObjectDriver::Driver::GearmanDBI)
Provides:       perl(Data::ObjectDriver::Driver::MultiPartition)
Provides:       perl(Data::ObjectDriver::Driver::Multiplexer)
Provides:       perl(Data::ObjectDriver::Driver::Partition)
Provides:       perl(Data::ObjectDriver::Driver::SimplePartition)
Provides:       perl(Data::ObjectDriver::Errors)
Provides:       perl(Data::ObjectDriver::Iterator)
Provides:       perl(Data::ObjectDriver::Profiler)
Provides:       perl(Data::ObjectDriver::ResultSet)
Provides:       perl(Data::ObjectDriver::SQL)
Provides:       perl(Data::ObjectDriver::SQL::Oracle)
%undefine       __perllib_provides
Recommends:     perl(Text::SimpleTable)
%{perl_requires}

%description
_Data::ObjectDriver_ is an object relational mapper, meaning that it maps
object-oriented design concepts onto a relational database.

It's inspired by, and descended from, the _MT::ObjectDriver_ classes in Six
Apart's Movable Type and TypePad weblogging products. But it adds in
caching and partitioning layers, allowing you to spread data across
multiple physical databases, without your application code needing to know
where the data is stored.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md ToDo
%license LICENSE

%changelog
