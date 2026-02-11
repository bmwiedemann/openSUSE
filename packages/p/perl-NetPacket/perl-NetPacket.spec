#
# spec file for package perl-NetPacket
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


%define cpan_name NetPacket
Name:           perl-NetPacket
Version:        1.8.0
Release:        0
License:        Artistic-2.0
Summary:        Assemble/disassemble network packets at the protocol level
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Socket) >= 1.87
BuildRequires:  perl(Test2::Bundle::More)
BuildRequires:  perl(parent)
Requires:       perl(Socket) >= 1.87
Requires:       perl(parent)
Recommends:     perl(Net::Pcap)
Recommends:     perl(Net::PcapUtils)
%{perl_requires}

%description
'NetPacket' provides a base class for a cluster of modules related to
decoding and encoding of network protocols. Each 'NetPacket' descendent
module knows how to encode and decode packets for the network protocol it
implements. Consult the documentation for the module in question for
protocol-specific implementation.

Note that there is no inheritance in the 'NetPacket::' cluster of modules
other than each protocol module being a 'NetPacket'. This was seen to be
too restrictive as imposing inheritance relationships (for example between
the IP, UDP and TCP protocols) would make things like tunneling or other
unusual situations difficult.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS doap.xml README README.mkdn SECURITY.md
%license LICENSE

%changelog
