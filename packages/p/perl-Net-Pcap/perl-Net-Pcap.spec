#
# spec file for package perl-Net-Pcap
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Net-Pcap
Name:           perl-Net-Pcap
Version:        0.20
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Interface to the pcap(3) LBL packet capture library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libpcap-devel
Requires:       perl(Data::Hexdumper)
Requires:       perl(NetPacket)
# MANUAL END

%description
'Net::Pcap' is a Perl binding to the LBL pcap(3) library and its Win32
counterpart, the WinPcap library. Pcap (packet capture) is a portable API
to capture network packet: it allows applications to capture packets at
link-layer, bypassing the normal protocol stack. It also provides features
like kernel-level packet filtering and access to internal statistics.

Common applications include network statistics collection, security
monitoring, network debugging, etc.

%package -n pcapdump
Summary:        Dump packets from the network
Requires:       %{name} = %{version}

%description -n pcapdump
Command line tool to dump packets from the network.

pcapdump mimics the very basic features of tcpdump(1) and provides a good
example of how to use Net::Pcap.

%package -n pcapinfo
Summary:        Prints detailed information about the network devices
Requires:       %{name} = %{version}

%description -n pcapinfo
pcapinfo prints detailed information about the network devices and Pcap library
available on the current host.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
install -D -m0755 eg/pcapdump "%{buildroot}%{_bindir}/pcapdump"
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%exclude %{_bindir}/pcapinfo
%exclude %{_bindir}/pcapdump
%exclude %{_mandir}/man1/pcapinfo.1%{?ext_man}

%files -n pcapdump
%{_bindir}/pcapdump

%files -n pcapinfo
%{_bindir}/pcapinfo
%{_mandir}/man1/pcapinfo.1%{?ext_man}
%doc Changes README stubs.inc

%changelog
