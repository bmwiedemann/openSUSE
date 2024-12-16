#
# spec file for package perl-Mojolicious
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


%define cpan_name Mojolicious
Name:           perl-Mojolicious
Version:        9.390.0
Release:        0
# 9.39 -> normalize -> 9.390.0
%define cpan_version 9.39
License:        Artistic-2.0
Summary:        Real-time web framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::IP) >= 0.37
BuildRequires:  perl(Sub::Util) >= 1.41
Requires:       perl(IO::Socket::IP) >= 0.37
Requires:       perl(Sub::Util) >= 1.41
Provides:       perl(Mojo)
Provides:       perl(Mojo::Asset)
Provides:       perl(Mojo::Asset::File)
Provides:       perl(Mojo::Asset::Memory)
Provides:       perl(Mojo::Base)
Provides:       perl(Mojo::BaseUtil)
Provides:       perl(Mojo::ByteStream)
Provides:       perl(Mojo::Cache)
Provides:       perl(Mojo::Collection)
Provides:       perl(Mojo::Content)
Provides:       perl(Mojo::Content::MultiPart)
Provides:       perl(Mojo::Content::Single)
Provides:       perl(Mojo::Cookie)
Provides:       perl(Mojo::Cookie::Request)
Provides:       perl(Mojo::Cookie::Response)
Provides:       perl(Mojo::DOM)
Provides:       perl(Mojo::DOM::CSS)
Provides:       perl(Mojo::DOM::HTML)
Provides:       perl(Mojo::Date)
Provides:       perl(Mojo::DynamicMethods)
Provides:       perl(Mojo::EventEmitter)
Provides:       perl(Mojo::Exception)
Provides:       perl(Mojo::File)
Provides:       perl(Mojo::Headers)
Provides:       perl(Mojo::HelloWorld)
Provides:       perl(Mojo::Home)
Provides:       perl(Mojo::IOLoop)
Provides:       perl(Mojo::IOLoop::Client)
Provides:       perl(Mojo::IOLoop::Server)
Provides:       perl(Mojo::IOLoop::Stream)
Provides:       perl(Mojo::IOLoop::Subprocess)
Provides:       perl(Mojo::IOLoop::TLS)
Provides:       perl(Mojo::JSON)
Provides:       perl(Mojo::JSON::Pointer)
Provides:       perl(Mojo::Loader)
Provides:       perl(Mojo::Log)
Provides:       perl(Mojo::Log::_Capture)
Provides:       perl(Mojo::Message)
Provides:       perl(Mojo::Message::Request)
Provides:       perl(Mojo::Message::Response)
Provides:       perl(Mojo::Parameters)
Provides:       perl(Mojo::Path)
Provides:       perl(Mojo::Promise)
Provides:       perl(Mojo::Reactor)
Provides:       perl(Mojo::Reactor::EV)
Provides:       perl(Mojo::Reactor::Poll)
Provides:       perl(Mojo::Server)
Provides:       perl(Mojo::Server::CGI)
Provides:       perl(Mojo::Server::Daemon)
Provides:       perl(Mojo::Server::Hypnotoad)
Provides:       perl(Mojo::Server::Morbo)
Provides:       perl(Mojo::Server::Morbo::Backend)
Provides:       perl(Mojo::Server::Morbo::Backend::Poll)
Provides:       perl(Mojo::Server::PSGI)
Provides:       perl(Mojo::Server::PSGI::_IO)
Provides:       perl(Mojo::Server::Prefork)
Provides:       perl(Mojo::Template)
Provides:       perl(Mojo::Transaction)
Provides:       perl(Mojo::Transaction::HTTP)
Provides:       perl(Mojo::Transaction::WebSocket)
Provides:       perl(Mojo::URL)
Provides:       perl(Mojo::Upload)
Provides:       perl(Mojo::UserAgent)
Provides:       perl(Mojo::UserAgent::CookieJar)
Provides:       perl(Mojo::UserAgent::Proxy)
Provides:       perl(Mojo::UserAgent::Server)
Provides:       perl(Mojo::UserAgent::Transactor)
Provides:       perl(Mojo::Util)
Provides:       perl(Mojo::Util::_Guard)
Provides:       perl(Mojo::WebSocket)
Provides:       perl(Mojolicious) = %{version}
Provides:       perl(Mojolicious::Command)
Provides:       perl(Mojolicious::Command::Author::cpanify)
Provides:       perl(Mojolicious::Command::Author::generate)
Provides:       perl(Mojolicious::Command::Author::generate::app)
Provides:       perl(Mojolicious::Command::Author::generate::dockerfile)
Provides:       perl(Mojolicious::Command::Author::generate::lite_app)
Provides:       perl(Mojolicious::Command::Author::generate::makefile)
Provides:       perl(Mojolicious::Command::Author::generate::plugin)
Provides:       perl(Mojolicious::Command::Author::inflate)
Provides:       perl(Mojolicious::Command::cgi)
Provides:       perl(Mojolicious::Command::daemon)
Provides:       perl(Mojolicious::Command::eval)
Provides:       perl(Mojolicious::Command::get)
Provides:       perl(Mojolicious::Command::prefork)
Provides:       perl(Mojolicious::Command::psgi)
Provides:       perl(Mojolicious::Command::routes)
Provides:       perl(Mojolicious::Command::version)
Provides:       perl(Mojolicious::Commands)
Provides:       perl(Mojolicious::Controller)
Provides:       perl(Mojolicious::Lite)
Provides:       perl(Mojolicious::Plugin)
Provides:       perl(Mojolicious::Plugin::Config)
Provides:       perl(Mojolicious::Plugin::DefaultHelpers)
Provides:       perl(Mojolicious::Plugin::EPLRenderer)
Provides:       perl(Mojolicious::Plugin::EPRenderer)
Provides:       perl(Mojolicious::Plugin::HeaderCondition)
Provides:       perl(Mojolicious::Plugin::JSONConfig)
Provides:       perl(Mojolicious::Plugin::Mount)
Provides:       perl(Mojolicious::Plugin::NotYAMLConfig)
Provides:       perl(Mojolicious::Plugin::TagHelpers)
Provides:       perl(Mojolicious::Plugins)
Provides:       perl(Mojolicious::Renderer)
Provides:       perl(Mojolicious::Routes)
Provides:       perl(Mojolicious::Routes::Match)
Provides:       perl(Mojolicious::Routes::Pattern)
Provides:       perl(Mojolicious::Routes::Route)
Provides:       perl(Mojolicious::Sessions)
Provides:       perl(Mojolicious::Static)
Provides:       perl(Mojolicious::Types)
Provides:       perl(Mojolicious::Validator)
Provides:       perl(Mojolicious::Validator::Validation)
Provides:       perl(Test::Mojo)
Provides:       perl(ojo)
%undefine       __perllib_provides
%{perl_requires}

%description
An amazing real-time web framework built on top of the powerful Mojo web
development toolkit. With support for RESTful routes, plugins, commands,
Perl-ish templates, content negotiation, session management, form
validation, testing framework, static file server, 'CGI'/'PSGI' detection,
first class Unicode support and much more for you to discover.

Take a look at our excellent documentation in Mojolicious::Guides!

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README.md
%license LICENSE

%changelog
