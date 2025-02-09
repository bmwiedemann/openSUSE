#
# spec file for package perl-Net-Jabber
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


%define cpan_name Net-Jabber
Name:           perl-Net-Jabber
Version:        2.0.0
Release:        0
# 2.0 -> normalize -> 2.0.0
%define cpan_version 2.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Jabber Perl Library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REATMON/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Net-Jabber-2.0-tests.diff
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::XMPP) >= 1
Requires:       perl(Net::XMPP) >= 1
Provides:       perl(Net::Jabber) = %{version}
Provides:       perl(Net::Jabber::Client) = %{version}
Provides:       perl(Net::Jabber::Component) = %{version}
Provides:       perl(Net::Jabber::Data) = %{version}
Provides:       perl(Net::Jabber::Debug) = %{version}
Provides:       perl(Net::Jabber::Dialback) = %{version}
Provides:       perl(Net::Jabber::Dialback::Result) = %{version}
Provides:       perl(Net::Jabber::Dialback::Verify) = %{version}
Provides:       perl(Net::Jabber::IQ) = %{version}
Provides:       perl(Net::Jabber::JID) = %{version}
Provides:       perl(Net::Jabber::Key) = %{version}
Provides:       perl(Net::Jabber::Log) = %{version}
Provides:       perl(Net::Jabber::Message) = %{version}
Provides:       perl(Net::Jabber::Namespaces)
Provides:       perl(Net::Jabber::Presence) = %{version}
Provides:       perl(Net::Jabber::Protocol) = %{version}
Provides:       perl(Net::Jabber::Server) = %{version}
Provides:       perl(Net::Jabber::Stanza)
Provides:       perl(Net::Jabber::XDB) = %{version}
Provides:       perl(Test::Builder) = 0.17
Provides:       perl(Test::More) = 0.47
Provides:       perl(Test::Simple) = 0.47
%undefine       __perllib_provides
%{perl_requires}

%description
  Net::Jabber is a convenient tool to use for any perl script that would
  like to utilize the Jabber Instant Messaging protocol.  While not a
  client in and of itself, it provides all of the necessary back-end
  functions to make a CGI client or command-line perl client feasible and
  easy to use.  Net::Jabber is a wrapper around the rest of the official
  Net::Jabber::xxxxxx packages.

  There is are example scripts in the example directory that provide you
  with examples of very simple Jabber programs.


  NOTE: The parser that XML::Stream::Parser provides, as are most Perl
  parsers, is synchronous.  If you are in the middle of parsing a packet
  and call a user defined callback, the Parser is blocked until your
  callback finishes.  This means you cannot be operating on a packet,
  send out another packet and wait for a response to that packet.  It
  will never get to you.  Threading might solve this, but as of the
  writing of this, threading in Perl is not quite up to par yet.  This
  issue will be revisted in the future.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -N

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
%patch -P0 -p0

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
%doc CHANGES examples README
%license LICENSE.LGPL

%changelog
