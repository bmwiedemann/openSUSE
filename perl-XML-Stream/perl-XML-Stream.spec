#
# spec file for package perl-XML-Stream
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-XML-Stream
Version:        1.24
Release:        0
%define cpan_name XML-Stream
Summary:        Creates an XML Stream connection and parses return data
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Stream/
Source:         http://www.cpan.org/authors/id/D/DA/DAPATRICK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(Module::Build) >= 0.3603
BuildRequires:  perl(Test::More) >= 0.92
Requires:       perl(Authen::SASL)
%{perl_requires}

%description
This module provides the user with methods to connect to a remote server,
send a stream of XML to the server, and receive/parse an XML stream from
the server. It is primarily based work for the Etherx XML router developed
by the Jabber Development Team. For more information about this project
visit http://xmpp.org/protocols/streams/.

XML::Stream gives the user the ability to define a central callback that
will be used to handle the tags received from the server. These tags are
passed in the format defined at instantiation time. the closing tag of an
object is seen, the tree is finished and passed to the call back function.
What the user does with it from there is up to them.

For a detailed description of how this module works, and about the data
structure that it returns, please view the source of Stream.pm and look at
the detailed description at the end of the file.

NOTE: The parser that XML::Stream::Parser provides, as are most Perl
parsers, is synchronous. If you are in the middle of parsing a packet and
call a user defined callback, the Parser is blocked until your callback
finishes. This means you cannot be operating on a packet, send out another
packet and wait for a response to that packet. It will never get to you.
Threading might solve this, but as we all know threading in Perl is not
quite up to par yet. This issue will be revisted in the future.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES INFO LICENSE README

%changelog
