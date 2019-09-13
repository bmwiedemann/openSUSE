#
# spec file for package perl-NetPacket
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-NetPacket
Version:        1.7.2
Release:        0
%define cpan_name NetPacket
Summary:        Assemble/disassemble network packets at the protocol level
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Socket) >= 1.87
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
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTORS doap.xml README README.mkdn
%license LICENSE

%changelog
