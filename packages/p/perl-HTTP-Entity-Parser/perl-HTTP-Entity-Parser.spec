#
# spec file for package perl-HTTP-Entity-Parser
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-HTTP-Entity-Parser
Version:        0.22
Release:        0
%define cpan_name HTTP-Entity-Parser
Summary:        PSGI compliant HTTP Entity Parser
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Message) >= 6
BuildRequires:  perl(HTTP::MultiPartParser)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003007
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.23
Requires:       perl(HTTP::MultiPartParser)
Requires:       perl(Hash::MultiValue)
Requires:       perl(JSON::MaybeXS) >= 1.003007
Requires:       perl(Module::Load)
Requires:       perl(Stream::Buffered)
Requires:       perl(WWW::Form::UrlEncoded) >= 0.23
%{perl_requires}

%description
HTTP::Entity::Parser is a PSGI-compliant HTTP Entity parser. This module
also is compatible with HTTP::Body. Unlike HTTP::Body, HTTP::Entity::Parser
reads HTTP entities from PSGI's environment '$env->{'psgi.input'}' and
parses it. This module supports application/x-www-form-urlencoded,
multipart/form-data and application/json.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes minil.toml README.md
%license LICENSE

%changelog
