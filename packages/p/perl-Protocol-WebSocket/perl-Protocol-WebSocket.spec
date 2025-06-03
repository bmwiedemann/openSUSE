#
# spec file for package perl-Protocol-WebSocket
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


%define cpan_name Protocol-WebSocket
Name:           perl-Protocol-WebSocket
Version:        0.260.0
Release:        0
# 0.26 -> normalize -> 0.260.0
%define cpan_version 0.26
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        WebSocket protocol
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/V/VT/VTI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
Requires:       perl(Digest::SHA)
Provides:       perl(Protocol::WebSocket) = %{version}
Provides:       perl(Protocol::WebSocket::Client)
Provides:       perl(Protocol::WebSocket::Cookie)
Provides:       perl(Protocol::WebSocket::Cookie::Request)
Provides:       perl(Protocol::WebSocket::Cookie::Response)
Provides:       perl(Protocol::WebSocket::Frame)
Provides:       perl(Protocol::WebSocket::Handshake)
Provides:       perl(Protocol::WebSocket::Handshake::Client)
Provides:       perl(Protocol::WebSocket::Handshake::Server)
Provides:       perl(Protocol::WebSocket::Message)
Provides:       perl(Protocol::WebSocket::Request)
Provides:       perl(Protocol::WebSocket::Response)
Provides:       perl(Protocol::WebSocket::Stateful)
Provides:       perl(Protocol::WebSocket::URL)
%undefine       __perllib_provides
%{perl_requires}

%description
Client/server WebSocket message and frame parser/constructor. This module
does not provide a WebSocket server or client, but is made for using in
http servers or clients to provide WebSocket support.

Protocol::WebSocket supports the following WebSocket protocol versions:

    draft-ietf-hybi-17 (latest)
    draft-ietf-hybi-10
    draft-ietf-hybi-00 (with HAProxy support)
    draft-hixie-75

By default the latest version is used. The WebSocket version is detected
automatically on the server side. On the client side you have set a
'version' attribute to an appropriate value.

Protocol::WebSocket itself does not contain any code and cannot be used
directly. Instead the following modules should be used:

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README.md util
%license LICENSE

%changelog
