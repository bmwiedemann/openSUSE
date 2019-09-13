#
# spec file for package perl-Net-XMPP
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Net-XMPP
Version:        1.05
Release:        0
%define cpan_name Net-XMPP
Summary:        XMPP Perl Library
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-XMPP/
Source0:        http://www.cpan.org/authors/id/D/DA/DAPATRICK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Authen::SASL) >= 2.12
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(LWP::Online) >= 1.07
BuildRequires:  perl(Module::Build) >= 0.360300
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(XML::Stream) >= 1.24
BuildRequires:  perl(YAML::Tiny) >= 1.41
Requires:       perl(Authen::SASL) >= 2.12
Requires:       perl(Digest::SHA)
Requires:       perl(XML::Stream) >= 1.24
%{perl_requires}

%description
Net::XMPP is a convenient tool to use for any perl script that would like
to utilize the XMPP Instant Messaging protocol. While not a client in and
of itself, it provides all of the necessary back-end functions to make a
CGI client or command-line perl client feasible and easy to use. Net::XMPP
is a wrapper around the rest of the official Net::XMPP::xxxxxx packages.

There is are example scripts in the example directory that provide you with
examples of very simple XMPP programs.

NOTE: The parser that the XML::Stream::Parser manpage provides, as are most
Perl parsers, is synchronous. If you are in the middle of parsing a packet
and call a user defined callback, the Parser is blocked until your callback
finishes. This means you cannot be operating on a packet, send out another
packet and wait for a response to that packet. It will never get to you.
Threading might solve this, but as of this writing threading in Perl is not
quite up to par yet. This issue will be revisted in the future.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
rm t/gtalk.t # skip tests that need network
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES examples LICENSE README

%changelog
