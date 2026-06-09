#
# spec file for package perl-DBI
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name DBI
Name:           perl-DBI
Version:        1.648.0
Release:        0
# 1.648 -> normalize -> 1.648.0
%define cpan_version 1.648
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Database independent interface for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{cpan_version}.tgz
Source1:        perl-DBI.rpmlintrc
Source2:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.48
BuildRequires:  perl(Test::Simple) >= 0.90
Provides:       perl(Bundle::DBI) = 12.8.696
Provides:       perl(DBD::DBM) = 0.80.0
Provides:       perl(DBD::DBM::Statement)
Provides:       perl(DBD::DBM::Table)
Provides:       perl(DBD::DBM::db)
Provides:       perl(DBD::DBM::dr)
Provides:       perl(DBD::DBM::st)
Provides:       perl(DBD::ExampleP) = 12.14.311
Provides:       perl(DBD::ExampleP::db)
Provides:       perl(DBD::ExampleP::dr)
Provides:       perl(DBD::ExampleP::st)
Provides:       perl(DBD::File) = 0.450.0
Provides:       perl(DBD::File::DataSource::File)
Provides:       perl(DBD::File::DataSource::Stream)
Provides:       perl(DBD::File::Statement)
Provides:       perl(DBD::File::Table)
Provides:       perl(DBD::File::TableSource::FileSystem)
Provides:       perl(DBD::File::db)
Provides:       perl(DBD::File::dr)
Provides:       perl(DBD::File::st)
Provides:       perl(DBD::Gofer) = 0.15.327
Provides:       perl(DBD::Gofer::Policy::Base) = 0.10.88
Provides:       perl(DBD::Gofer::Policy::classic) = 0.10.88
Provides:       perl(DBD::Gofer::Policy::pedantic) = 0.10.88
Provides:       perl(DBD::Gofer::Policy::rush) = 0.10.88
Provides:       perl(DBD::Gofer::Transport::Base) = 0.14.121
Provides:       perl(DBD::Gofer::Transport::corostream)
Provides:       perl(DBD::Gofer::Transport::null) = 0.10.88
Provides:       perl(DBD::Gofer::Transport::pipeone) = 0.10.88
Provides:       perl(DBD::Gofer::Transport::stream) = 0.14.599
Provides:       perl(DBD::Gofer::db)
Provides:       perl(DBD::Gofer::dr)
Provides:       perl(DBD::Gofer::st)
Provides:       perl(DBD::Mem) = 0.1.0
Provides:       perl(DBD::Mem::DataSource)
Provides:       perl(DBD::Mem::Statement)
Provides:       perl(DBD::Mem::Table)
Provides:       perl(DBD::Mem::db)
Provides:       perl(DBD::Mem::dr)
Provides:       perl(DBD::Mem::st)
Provides:       perl(DBD::NullP) = 12.14.715
Provides:       perl(DBD::NullP::db)
Provides:       perl(DBD::NullP::dr)
Provides:       perl(DBD::NullP::st)
Provides:       perl(DBD::Proxy) = 0.200.400
Provides:       perl(DBD::Proxy::RPC::PlClient)
Provides:       perl(DBD::Proxy::db)
Provides:       perl(DBD::Proxy::dr)
Provides:       perl(DBD::Proxy::st)
Provides:       perl(DBD::Sponge) = 12.10.3
Provides:       perl(DBD::Sponge::db)
Provides:       perl(DBD::Sponge::dr)
Provides:       perl(DBD::Sponge::st)
Provides:       perl(DBDI)
Provides:       perl(DBI) = %{version}
Provides:       perl(DBI::Const::GetInfo::ANSI) = 2.8.697
Provides:       perl(DBI::Const::GetInfo::ODBC) = 2.11.374
Provides:       perl(DBI::Const::GetInfoReturn) = 2.8.697
Provides:       perl(DBI::Const::GetInfoType) = 2.8.697
Provides:       perl(DBI::DBD) = 12.15.129
Provides:       perl(DBI::DBD::Metadata) = 2.14.214
Provides:       perl(DBI::DBD::SqlEngine) = 0.60.0
Provides:       perl(DBI::DBD::SqlEngine::DataSource)
Provides:       perl(DBI::DBD::SqlEngine::Statement)
Provides:       perl(DBI::DBD::SqlEngine::Table)
Provides:       perl(DBI::DBD::SqlEngine::TableSource)
Provides:       perl(DBI::DBD::SqlEngine::TieMeta)
Provides:       perl(DBI::DBD::SqlEngine::TieTables)
Provides:       perl(DBI::DBD::SqlEngine::db)
Provides:       perl(DBI::DBD::SqlEngine::dr)
Provides:       perl(DBI::DBD::SqlEngine::st)
Provides:       perl(DBI::Gofer::Execute) = 0.14.283
Provides:       perl(DBI::Gofer::Request) = 0.12.537
Provides:       perl(DBI::Gofer::Response) = 0.11.566
Provides:       perl(DBI::Gofer::Serializer::Base) = 0.9.950
Provides:       perl(DBI::Gofer::Serializer::DataDumper) = 0.9.950
Provides:       perl(DBI::Gofer::Serializer::Storable) = 0.15.586
Provides:       perl(DBI::Gofer::Transport::Base) = 0.12.537
Provides:       perl(DBI::Gofer::Transport::pipeone) = 0.12.537
Provides:       perl(DBI::Gofer::Transport::stream) = 0.12.537
Provides:       perl(DBI::Profile) = 2.15.65
Provides:       perl(DBI::ProfileData) = 2.10.8
Provides:       perl(DBI::ProfileDumper) = 2.15.325
Provides:       perl(DBI::ProfileDumper::Apache) = 2.14.121
Provides:       perl(DBI::ProfileSubs) = 0.9.396
Provides:       perl(DBI::ProxyServer) = 0.300.500
Provides:       perl(DBI::ProxyServer::db)
Provides:       perl(DBI::ProxyServer::dr)
Provides:       perl(DBI::ProxyServer::st)
Provides:       perl(DBI::SQL::Nano) = 1.15.544
Provides:       perl(DBI::SQL::Nano::Statement_)
Provides:       perl(DBI::SQL::Nano::Table_)
Provides:       perl(DBI::Util::CacheMemory) = 0.10.315
Provides:       perl(DBI::common)
%undefine       __perllib_provides
%{perl_requires}

%description
The DBI is a database access module for the Perl programming language. It
defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database being
used.

It is important to remember that the DBI is just an interface. The DBI is a
layer of "glue" between an application and one or more database _driver_
modules. It is the driver modules which do most of the real work. The DBI
provides a standard interface and framework for the drivers to operate
within.

This document often uses terms like _references_, _objects_, _methods_. If
you're not familiar with those terms then it would be a good idea to read
at least the following perl manuals first: perlreftut, perldsc, perllol,
and perlboot.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog Driver.xst README.md
%license LICENSE

%changelog
