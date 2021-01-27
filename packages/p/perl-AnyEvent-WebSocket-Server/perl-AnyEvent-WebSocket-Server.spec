#
# spec file for package perl-AnyEvent-WebSocket-Server
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


%define cpan_name AnyEvent-WebSocket-Server
Name:           perl-AnyEvent-WebSocket-Server
Version:        0.10
Release:        0
Summary:        WebSocket server for AnyEvent
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::WebSocket::Client) >= 0.37
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Module::Build::Prereqs::FromCPANfile) >= 0.02
BuildRequires:  perl(Protocol::WebSocket::Frame)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Client)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Server)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(AnyEvent::Handle)
Requires:       perl(AnyEvent::WebSocket::Client) >= 0.37
Requires:       perl(Protocol::WebSocket::Handshake::Server)
Requires:       perl(Try::Tiny)
Recommends:     perl(Net::SSLeay)
%{perl_requires}

%description
This class is an implementation of the WebSocket server in an AnyEvent
context.

  * Currently this module supports WebSocket protocol version 13 only. See at
https://tools.ietf.org/html/rfc6455 for detail.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes TODO

%changelog
