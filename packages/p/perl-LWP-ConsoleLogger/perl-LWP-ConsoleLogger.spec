#
# spec file for package perl-LWP-ConsoleLogger
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name LWP-ConsoleLogger
Name:           perl-LWP-ConsoleLogger
Version:        1.000000
Release:        0
License:        Artistic-2.0
Summary:        LWP tracing and debugging
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         0001-replace-env.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Printer) >= 0.36
BuildRequires:  perl(DateTime)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::Restrict)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(HTTP::CookieMonster)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003005
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Log::Dispatch) >= 2.56
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(Parse::MIME)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Plack::Handler::HTTP::Server::Simple)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Test::Agent)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(String::Trim)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Term::Size::Any)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::SimpleTable::AutoWidth) >= 0.09
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(WWW::Mechanize)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(version)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(Data::Printer) >= 0.36
Requires:       perl(DateTime)
Requires:       perl(HTML::Restrict)
Requires:       perl(HTTP::Body)
Requires:       perl(HTTP::CookieMonster)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response)
Requires:       perl(JSON::MaybeXS) >= 1.003005
Requires:       perl(List::AllUtils)
Requires:       perl(Log::Dispatch) >= 2.56
Requires:       perl(Module::Load::Conditional)
Requires:       perl(Module::Runtime)
Requires:       perl(Moo)
Requires:       perl(MooX::StrictConstructor)
Requires:       perl(Parse::MIME)
Requires:       perl(Ref::Util)
Requires:       perl(String::Trim)
Requires:       perl(Sub::Exporter)
Requires:       perl(Term::Size::Any)
Requires:       perl(Text::SimpleTable::AutoWidth) >= 0.09
Requires:       perl(Try::Tiny)
Requires:       perl(Types::Common::Numeric)
Requires:       perl(Types::Standard)
Requires:       perl(URI::QueryParam)
Requires:       perl(XML::Simple)
Recommends:     perl(HTML::FormatText::Lynx) >= 23
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  netcfg
Requires:       perl(Term::Size::Any)
# MANUAL END

%description
It can be hard (or at least tedious) to debug mechanize scripts. LWP::Debug
is deprecated. It suggests you write your own debugging handlers, set up a
proxy or install Wireshark. Those are all workable solutions, but this
module exists to save you some of that work. The guts of this module are
stolen from Plack::Middleware::DebugLogging, which in turn stole most of
its internals from Catalyst. If you're new to LWP::ConsoleLogger, I suggest
getting started with the LWP::ConsoleLogger::Easy wrapper. This will get
you up and running in minutes. If you need to tweak the settings that
LWP::ConsoleLogger::Easy chooses for you (or if you just want to be fancy),
please read on.

Since this is a debugging library, I've left as much mutable state as
possible, so that you can easily toggle output on and off and otherwise
adjust how you deal with the output.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTORS examples README.md
%license LICENSE

%changelog
