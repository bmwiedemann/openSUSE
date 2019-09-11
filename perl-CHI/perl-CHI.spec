#
# spec file for package perl-CHI
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


Name:           perl-CHI
Version:        0.60
Release:        0
%define cpan_name CHI
Summary:        Unified cache handling interface
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CHI/
Source0:        http://www.cpan.org/authors/id/J/JS/JSWARTZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Assert) >= 0.20
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::JHash)
BuildRequires:  perl(Hash::MoreUtils)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::MoreUtils) >= 0.13
BuildRequires:  perl(Log::Any) >= 0.08
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.23
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(MooX::Types::MooseLike::Numeric)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::Duration) >= 1.060000
BuildRequires:  perl(Time::Duration::Parse) >= 0.03
BuildRequires:  perl(Try::Tiny) >= 0.05
Requires:       perl(Carp::Assert) >= 0.20
Requires:       perl(Class::Load)
Requires:       perl(Data::UUID)
Requires:       perl(Digest::JHash)
Requires:       perl(Hash::MoreUtils)
Requires:       perl(JSON::MaybeXS) >= 1.003003
Requires:       perl(List::MoreUtils) >= 0.13
Requires:       perl(Log::Any) >= 0.08
Requires:       perl(Moo) >= 1.003
Requires:       perl(MooX::Types::MooseLike) >= 0.23
Requires:       perl(MooX::Types::MooseLike::Base)
Requires:       perl(MooX::Types::MooseLike::Numeric)
Requires:       perl(String::RewritePrefix)
Requires:       perl(Task::Weaken)
Requires:       perl(Time::Duration) >= 1.060000
Requires:       perl(Time::Duration::Parse) >= 0.03
Requires:       perl(Try::Tiny) >= 0.05
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
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes LICENSE README

%changelog
