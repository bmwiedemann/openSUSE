#
# spec file for package perl-CHI
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


%define cpan_name CHI
Name:           perl-CHI
Version:        0.610.0
Release:        0
# 0.61 -> normalize -> 0.610.0
%define cpan_version 0.61
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Unified cache handling interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Carp::Assert) >= 0.200
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::JHash)
BuildRequires:  perl(Hash::MoreUtils)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::MoreUtils) >= 0.130
BuildRequires:  perl(Log::Any) >= 0.80
BuildRequires:  perl(Module::Mask)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.230
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(MooX::Types::MooseLike::Numeric)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::Duration) >= 1.06
BuildRequires:  perl(Time::Duration::Parse) >= 0.30
BuildRequires:  perl(Try::Tiny) >= 0.50
Requires:       perl(Carp::Assert) >= 0.200
Requires:       perl(Class::Load)
Requires:       perl(Data::UUID)
Requires:       perl(Digest::JHash)
Requires:       perl(Hash::MoreUtils)
Requires:       perl(JSON::MaybeXS) >= 1.003003
Requires:       perl(List::MoreUtils) >= 0.130
Requires:       perl(Log::Any) >= 0.80
Requires:       perl(Moo) >= 1.003
Requires:       perl(MooX::Types::MooseLike) >= 0.230
Requires:       perl(MooX::Types::MooseLike::Base)
Requires:       perl(MooX::Types::MooseLike::Numeric)
Requires:       perl(String::RewritePrefix)
Requires:       perl(Task::Weaken)
Requires:       perl(Time::Duration) >= 1.06
Requires:       perl(Time::Duration::Parse) >= 0.30
Requires:       perl(Try::Tiny) >= 0.50
Provides:       perl(CHI) = %{version}
Provides:       perl(CHI::CacheObject) = %{version}
Provides:       perl(CHI::Constants) = %{version}
Provides:       perl(CHI::Driver) = %{version}
Provides:       perl(CHI::Driver::Base::CacheContainer) = %{version}
Provides:       perl(CHI::Driver::CacheCache) = %{version}
Provides:       perl(CHI::Driver::FastMmap) = %{version}
Provides:       perl(CHI::Driver::File) = %{version}
Provides:       perl(CHI::Driver::Memory) = %{version}
Provides:       perl(CHI::Driver::Metacache) = %{version}
Provides:       perl(CHI::Driver::Null) = %{version}
Provides:       perl(CHI::Driver::RawMemory) = %{version}
Provides:       perl(CHI::Driver::Role::HasSubcaches) = %{version}
Provides:       perl(CHI::Driver::Role::IsSizeAware) = %{version}
Provides:       perl(CHI::Driver::Role::IsSubcache) = %{version}
Provides:       perl(CHI::Driver::Role::Universal) = %{version}
Provides:       perl(CHI::Stats) = %{version}
Provides:       perl(CHI::Types) = %{version}
Provides:       perl(CHI::Util) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
CHI provides a unified caching API, designed to assist a developer in
persisting data for a specified period of time.

The CHI interface is implemented by driver classes that support fetching,
storing and clearing of data. Driver classes exist or will exist for the
gamut of storage backends available to Perl, such as memory, plain files,
memory mapped files, memcached, and DBI.

CHI is intended as an evolution of DeWitt Clinton's Cache::Cache package,
adhering to the basic Cache API but adding new features and addressing
limitations in the Cache::Cache implementation.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes
%license LICENSE

%changelog
