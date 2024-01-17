#
# spec file for package perl-Net-Twitter
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


Name:           perl-Net-Twitter
Version:        4.01043
Release:        0
%define cpan_name Net-Twitter
Summary:        Perl Interface to the Twitter Api
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Twitter/
Source0:        https://cpan.metacpan.org/authors/id/M/MM/MMIMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Socket::SSL) >= 2.005
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent) >= 5.819
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
#BuildRequires:  perl(Net::HTTP) >= >= 0, != 6.04, != 6.05
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(Net::OAuth::Message)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
Requires:       perl(Carp::Clan)
Requires:       perl(Class::Load)
Requires:       perl(Data::Visitor::Callback)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(Devel::StackTrace)
Requires:       perl(Digest::SHA)
Requires:       perl(HTML::Entities)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(IO::Socket::SSL) >= 2.005
Requires:       perl(JSON::MaybeXS)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Moose)
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Meta::Method)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::Role::Parameterized)
Requires:       perl(namespace::autoclean)
#Requires:       perl(Net::HTTP) >= >= 0, != 6.04, != 6.05
Requires:       perl(Net::OAuth)
Requires:       perl(Try::Tiny)
Requires:       perl(URI)
Requires:       perl(URI::Escape)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Net::HTTP) > 6.05
Requires:       perl(Net::HTTP) > 6.05
# MANUAL END

%description
This module has been superseded by Twitter::API. Please update as soon as
you possibly can to use new features and the new API versions. This module
will no longer be supported.

This module provides a perl interface to the Twitter APIs. See
http://dev.twitter.com/docs for a full description of the Twitter APIs.

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
%doc Changes examples README
%license LICENSE

%changelog
