#
# spec file for package perl-HTTP-Headers-ActionPack
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


%define cpan_name HTTP-Headers-ActionPack
Name:           perl-HTTP-Headers-ActionPack
Version:        0.100.0
Release:        0
# 0.10 -> normalize -> 0.100.0
%define cpan_version 0.10
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        HTTP Action, Adventure and Excitement
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Timer)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(parent)
Requires:       perl(HTTP::Date)
Requires:       perl(HTTP::Headers::Util)
Requires:       perl(Module::Runtime)
Requires:       perl(Sub::Exporter)
Requires:       perl(Time::Piece)
Requires:       perl(URI::Escape)
Requires:       perl(parent)
Provides:       perl(HTTP::Headers::ActionPack) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::AcceptCharset) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::AcceptLanguage) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::AuthenticationInfo) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Authorization) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Authorization::Basic) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Authorization::Digest) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::ContentNegotiation) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Core::Base) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Core::BaseAuthHeader) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Core::BaseHeaderList) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Core::BaseHeaderType) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Core::BaseHeaderWithParams) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::DateHeader) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::LinkHeader) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::LinkList) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::MediaType) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::MediaTypeList) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::PriorityList) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::Util) = %{version}
Provides:       perl(HTTP::Headers::ActionPack::WWWAuthenticate) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Plack)
# MANUAL END

%description
This is a module to handle the inflation and deflation of complex HTTP
header types. In many cases header values are simple strings, but in some
cases they are complex values with a lot of information encoded in them.
The goal of this module is to make the parsing and analysis of these
headers as easy as calling 'inflate' on a compatible object (see below for
a list).

This top-level class is basically a Factory for creating instances of the
other classes in this module. It contains a number of convenience methods
to help make common cases easy to write.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
