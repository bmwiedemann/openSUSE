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
Version:        0.80.0
Release:        0
# 0.08 -> normalize -> 0.80.0
%define cpan_version 0.08
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
BuildRequires:  perl(JSON::Validator) >= 5.150
BuildRequires:  perl(Mojolicious) >= 9.410
Requires:       perl(CryptX) >= 0.87
Requires:       perl(IPC::Run) >= 20231003.0
Requires:       perl(JSON::Validator) >= 5.150
Requires:       perl(Mojolicious) >= 9.410
Provides:       perl(MCP) = %{version}
Provides:       perl(MCP::Client)
Provides:       perl(MCP::Constants)
Provides:       perl(MCP::Prompt)
Provides:       perl(MCP::Resource)
Provides:       perl(MCP::Server)
Provides:       perl(MCP::Server::Transport)
Provides:       perl(MCP::Server::Transport::HTTP)
Provides:       perl(MCP::Server::Transport::Stdio)
Provides:       perl(MCP::Tool)
%undefine       __perllib_provides
%{perl_requires}

%description
Connect Perl with AI using the Model Context Protocol (MCP). Currently this
module is focused on tool calling and prompts, but it will be extended to
support other MCP features in the future. At its core, MCP is all about
text processing, making it a great fit for Perl.

Streamable HTTP Transport
    Use the MCP::Server/"to_action" method to add an MCP endpoint to any
    Mojolicious application. The tool name and description are used for
    discovery, and the at https://json-schema.org is used to validate the
    input.

      use Mojolicious::Lite -signatures;

      use MCP::Server;

      my $server = MCP::Server->new;
      $server->tool(
        name         => 'echo',
        description  => 'Echo the input text',
        input_schema => {type => 'object', properties => {msg => {type => 'string'}}, required => ['msg']},
        code         => sub ($tool, $args) {
          return "Echo: $args->{msg}";
        }
      );

      any '/mcp' => $server->to_action;

      app->start;

    Authentication can be added by the web application, just like for any
    other route. To allow for MCP applications to scale with prefork web
    servers, server to client streaming is currentlly avoided when
    possible.

Stdio Transport
    Build local command line applications and use the stdio transport for
    testing with the MCP::Server/"to_stdio" method.

      use Mojo::Base -strict, -signatures;

      use MCP::Server;

      my $server = MCP::Server->new;
      $server->tool(
        name         => 'echo',
        description  => 'Echo the input text',
        input_schema => {type => 'object', properties => {msg => {type => 'string'}}, required => ['msg']},
        code         => sub ($tool, $args) {
          return "Echo: $args->{msg}";
        }
      );

      $server->to_stdio;

    Just run the script and type requests on the command line.

      $ perl examples/echo_stdio.pl
      {"jsonrpc":"2.0","id":"1","method":"tools/list"}
      {"jsonrpc":"2.0","id":"2","method":"tools/call","params":{"name":"echo","arguments":{"msg":"hello perl"}}}

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
