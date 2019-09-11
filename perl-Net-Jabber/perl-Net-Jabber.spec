#
# spec file for package perl-Net-Jabber
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Net-Jabber
Version:        2.0
Release:        0
Summary:        Jabber Perl Library
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://cpan.org/modules/by-module/Net/
Source:         http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/Net-Jabber-%version.tar.gz
Patch:          Net-Jabber-%{version}-tests.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl-Net-XMPP
BuildRequires:  perl-macros
Requires:       perl-Authen-SASL
Requires:       perl-Digest-SHA1
Requires:       perl-Net-XMPP
Requires:       perl-Unicode-String
Requires:       perl-XML-Stream
%{perl_requires}

%description
Net::Jabber is a convenient tool to use for any perl script that would
like to utilize the Jabber Instant Messaging protocol. While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible and
easy to use. Net::Jabber is a wrapper around the rest of the official
Net::Jabber::xxxxxx packages.



Authors:
--------
    Ryan Eatmon <reatmon@ti.com>

%prep
%setup -q -n Net-Jabber-%{version}
%patch

%build
perl Makefile.PL
make %{?_smp_mflags}
make test || echo "obelisk.net has discontinued test account"

%install
%perl_make_install
%perl_process_packlist
chmod a-x examples/component_accept.pl examples/component_test.pl

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE.LGPL examples
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net
%{perl_vendorarch}/auto/Net

%changelog
