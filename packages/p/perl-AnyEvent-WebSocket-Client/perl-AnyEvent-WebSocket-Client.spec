#
# spec file for package perl-AnyEvent-WebSocket-Client
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.54
Release:        0
Summary:        WebSocket client for AnyEvent
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent) >= 7.13
BuildRequires:  perl(AnyEvent::Connector) >= 0.03
BuildRequires:  perl(Moo) >= 2.0
BuildRequires:  perl(PerlX::Maybe) >= 0.003
BuildRequires:  perl(Protocol::WebSocket) >= 0.20
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require) >= 0.000060
BuildRequires:  perl(Test2::Require::Module) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(URI) >= 1.53
BuildRequires:  perl(URI::ws)
Requires:       perl(AnyEvent) >= 7.13
Requires:       perl(AnyEvent::Connector) >= 0.03
Requires:       perl(Moo) >= 2.0
Requires:       perl(PerlX::Maybe) >= 0.003
Requires:       perl(Protocol::WebSocket) >= 0.20
Requires:       perl(URI) >= 1.53
Requires:       perl(URI::ws)
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
%autosetup  -n %{cpan_name}-%{version}
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
%doc author.yml Changes example README
%license LICENSE

%changelog
