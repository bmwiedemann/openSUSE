#
# spec file for package perl-Dancer2
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


Name:           perl-Dancer2
Version:        0.300004
Release:        0
%define cpan_name Dancer2
Summary:        Lightweight yet powerful web application framework
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CROMEDOME/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Cmd::Setup)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.21
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(MIME::Base64) >= 3.13
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Plack) >= 1.0040
BuildRequires:  perl(Plack::Middleware::FixMissingBodyInRedirect)
BuildRequires:  perl(Plack::Middleware::RemoveRedundantBody)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Role::Tiny) >= 2.000000
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Tiny)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Type::Tiny) >= 1.000006
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(YAML) >= 0.86
BuildRequires:  perl(parent)
Requires:       perl(App::Cmd::Setup)
Requires:       perl(Clone)
Requires:       perl(Config::Any)
Requires:       perl(Digest::SHA)
Requires:       perl(Exporter::Tiny)
Requires:       perl(File::Share)
Requires:       perl(HTTP::Date)
Requires:       perl(HTTP::Headers::Fast) >= 0.21
Requires:       perl(HTTP::Tiny)
Requires:       perl(Hash::Merge::Simple)
Requires:       perl(Hash::MultiValue)
Requires:       perl(Import::Into)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(List::Util) >= 1.29
Requires:       perl(MIME::Base64) >= 3.13
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2.000000
Requires:       perl(Moo::Role)
Requires:       perl(Plack) >= 1.0040
Requires:       perl(Plack::Middleware::FixMissingBodyInRedirect)
Requires:       perl(Plack::Middleware::RemoveRedundantBody)
Requires:       perl(Ref::Util)
Requires:       perl(Role::Tiny) >= 2.000000
Requires:       perl(Safe::Isa)
Requires:       perl(Sub::Quote)
Requires:       perl(Template)
Requires:       perl(Template::Tiny)
Requires:       perl(Test::More) >= 0.92
Requires:       perl(Type::Tiny) >= 1.000006
Requires:       perl(Types::Standard)
Requires:       perl(URI::Escape)
Requires:       perl(YAML) >= 0.86
Requires:       perl(parent)
Recommends:     perl(CGI::Deurl::XS)
Recommends:     perl(Class::XSAccessor)
Recommends:     perl(Cpanel::JSON::XS)
Recommends:     perl(Crypt::URandom)
Recommends:     perl(HTTP::XSCookies) >= 0.000007
Recommends:     perl(HTTP::XSHeaders)
Recommends:     perl(Math::Random::ISAAC::XS)
Recommends:     perl(MooX::TypeTiny)
Recommends:     perl(Pod::Simple::Search)
Recommends:     perl(Pod::Simple::SimpleTree)
Recommends:     perl(Scope::Upper)
Recommends:     perl(Type::Tiny::XS)
Recommends:     perl(URL::Encode::XS)
Recommends:     perl(YAML::XS)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Test::Deep)
# MANUAL END

%description
Dancer2 is the new generation of Dancer, the lightweight web-framework for
Perl. Dancer2 is a complete rewrite based on Moo.

Dancer2 can optionally use XS modules for speed, but at its core remains
fatpackable (packable by App::FatPacker) so you could easily deploy Dancer2
applications on hosts that do not support custom CPAN modules.

Dancer2 is easy and fun:

    use Dancer2;
    get '/' => sub { "Hello World" };
    dance;

This is the main module for the Dancer2 distribution. It contains logic for
creating a new Dancer2 application.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc AUTHORS Changes examples GitGuide.md
%license LICENSE

%changelog
