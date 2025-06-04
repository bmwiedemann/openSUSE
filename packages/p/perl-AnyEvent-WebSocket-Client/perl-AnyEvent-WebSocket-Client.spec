#
# spec file for package perl-AnyEvent-WebSocket-Client
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


%define cpan_name AnyEvent-WebSocket-Client
Name:           perl-AnyEvent-WebSocket-Client
Version:        0.550.0
Release:        0
# 0.55 -> normalize -> 0.550.0
%define cpan_version 0.55
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        WebSocket client for AnyEvent
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent) >= 7.130
BuildRequires:  perl(AnyEvent::Connector) >= 0.30
BuildRequires:  perl(Moo) >= 2.0
BuildRequires:  perl(PerlX::Maybe) >= 0.3
BuildRequires:  perl(Protocol::WebSocket) >= 0.200
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require) >= 0.000121
BuildRequires:  perl(Test2::Require::Module) >= 0.000121
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(URI) >= 1.530
BuildRequires:  perl(URI::ws)
Requires:       perl(AnyEvent) >= 7.130
Requires:       perl(AnyEvent::Connector) >= 0.30
Requires:       perl(Moo) >= 2.0
Requires:       perl(PerlX::Maybe) >= 0.3
Requires:       perl(Protocol::WebSocket) >= 0.200
Requires:       perl(URI) >= 1.530
Requires:       perl(URI::ws)
Provides:       perl(AnyEvent::WebSocket::Client) = %{version}
Provides:       perl(AnyEvent::WebSocket::Connection) = %{version}
Provides:       perl(AnyEvent::WebSocket::Message) = %{version}
Provides:       perl(Test2::Plugin::AnyEvent::Timeout)
Provides:       perl(Test2::Plugin::EV)
Provides:       perl(Test2::Require::NotWindows)
Provides:       perl(Test2::Require::SSL)
Provides:       perl(Test2::Tools::WebSocket::Connection)
Provides:       perl(Test2::Tools::WebSocket::Mojo)
Provides:       perl(Test2::Tools::WebSocket::Server)
%undefine       __perllib_provides
Recommends:     perl(EV)
Recommends:     perl(IO::Socket::SSL)
Recommends:     perl(Math::Random::Secure)
Recommends:     perl(Net::SSLeay)
Recommends:     perl(PerlX::Maybe::XS)
%{perl_requires}

%description
This class provides an interface to interact with a web server that
provides services via the WebSocket protocol in an AnyEvent context. It
uses Protocol::WebSocket rather than reinventing the wheel. You could use
AnyEvent and Protocol::WebSocket directly if you wanted finer grain
control, but if that is not necessary then this class may save you some
time.

The recommended API was added to the AnyEvent::WebSocket::Connection class
with version 0.12, so it is recommended that you include that version when
using this module. The older version of the API has since been deprecated
and removed.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes example README
%license LICENSE

%changelog
