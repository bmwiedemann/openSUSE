#
# spec file for package perl-HTTP-Entity-Parser
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


%define cpan_name HTTP-Entity-Parser
Name:           perl-HTTP-Entity-Parser
Version:        0.250.0
Release:        0
# 0.25 -> normalize -> 0.250.0
%define cpan_version 0.25
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        PSGI compliant HTTP Entity Parser
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Message) >= 6
BuildRequires:  perl(HTTP::MultiPartParser)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(JSON::MaybeXS) >= 1.3.7
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.230
Requires:       perl(HTTP::MultiPartParser)
Requires:       perl(Hash::MultiValue)
Requires:       perl(JSON::MaybeXS) >= 1.3.7
Requires:       perl(Module::Load)
Requires:       perl(Stream::Buffered)
Requires:       perl(WWW::Form::UrlEncoded) >= 0.230
Provides:       perl(HTTP::Entity::Parser) = %{version}
Provides:       perl(HTTP::Entity::Parser::JSON)
Provides:       perl(HTTP::Entity::Parser::MultiPart)
Provides:       perl(HTTP::Entity::Parser::OctetStream)
Provides:       perl(HTTP::Entity::Parser::UrlEncoded)
%undefine       __perllib_provides
%{perl_requires}

%description
HTTP::Entity::Parser is a PSGI-compliant HTTP Entity parser. This module
also is compatible with HTTP::Body. Unlike HTTP::Body, HTTP::Entity::Parser
reads HTTP entities from PSGI's environment '$env->{'psgi.input'}' and
parses it. This module supports application/x-www-form-urlencoded,
multipart/form-data and application/json.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
