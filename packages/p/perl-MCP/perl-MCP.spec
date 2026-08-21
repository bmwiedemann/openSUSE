#
# spec file for package perl-MCP
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


%define cpan_name MCP
Name:           perl-MCP
Version:        0.150.0
Release:        0
# 0.15 -> normalize -> 0.150.0
%define cpan_version 0.15
License:        MIT
Summary:        Connect Perl with AI using MCP (Model Context Protocol)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CryptX) >= 0.87
BuildRequires:  perl(IPC::Run) >= 20231003.0
BuildRequires:  perl(JSON::Schema::Tiny) >= 0.34
BuildRequires:  perl(Mojolicious) >= 9.410
Requires:       perl(CryptX) >= 0.87
Requires:       perl(IPC::Run) >= 20231003.0
Requires:       perl(JSON::Schema::Tiny) >= 0.34
Requires:       perl(Mojolicious) >= 9.410
Provides:       perl(MCP) = %{version}
Provides:       perl(MCP::Client)
Provides:       perl(MCP::Constants)
Provides:       perl(MCP::Primitive)
Provides:       perl(MCP::Prompt)
Provides:       perl(MCP::Resource)
Provides:       perl(MCP::Server)
Provides:       perl(MCP::Server::Context)
Provides:       perl(MCP::Server::Legacy)
Provides:       perl(MCP::Server::Subscription)
Provides:       perl(MCP::Server::Transport)
Provides:       perl(MCP::Server::Transport::HTTP)
Provides:       perl(MCP::Server::Transport::Stdio)
Provides:       perl(MCP::Tool)
%undefine       __perllib_provides
%{perl_requires}

%description
Connect Perl with AI using the Model Context Protocol (MCP). An MCP server
hands a model three kinds of things: tools it can call, prompts it can
start from, and resources it can read. At its core MCP is all about text
processing, which makes it a great fit for Perl.

The protocol revision implemented is '2026-07-28', and it is stateless.
There is no handshake and no session, every request stands on its own, so
an MCP endpoint is just another route in your Mojolicious application and
scales the same way.

Read on for a tour, or go straight to MCP::Server for the reference
documentation.

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
%doc Changes examples README.md
%license LICENSE

%changelog
