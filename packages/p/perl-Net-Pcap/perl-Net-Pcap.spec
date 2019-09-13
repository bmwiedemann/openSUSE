#
# spec file for package perl-Net-Pcap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-Pcap
Version:        0.18
Release:        0
Summary:        Interface to pcap LBL packet capture library
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/Net-Pcap
Source:         https://cpan.metacpan.org/authors/id/S/SA/SAPER/Net-Pcap-%{version}.tar.gz
Patch1:         perl-Net-Pcap-avoid-pcap_rmtauth-redefinition.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(XSLoader)
Requires:       perl(Carp)
Requires:       perl(Socket)
Requires:       perl(Sys::Hostname)
Requires:       perl(Test::More) >= 0.45
Requires:       perl(XSLoader)
%{perl_requires}
%if 0%{?suse_version} == 0 || 0%{?suse_version} >= 1030
BuildRequires:  libpcap-devel
%else
BuildRequires:  libpcap
%endif

%description
Net::Pcap is a Perl binding to the LBL pcap(3) library. The README for libpcap
describes itself as: "a system-independent interface for user-level packet
capture.  libpcap provides a portable framework for low-level network
monitoring.  Applications include network statistics collection, security
monitoring, network debugging, etc."

%package -n pcapdump
Summary:        Dump packets from the network
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}

%description -n pcapdump
Command line tool to dump packets from the network.

pcapdump mimics the very basic features of tcpdump(1) and provides a good
example of how to use Net::Pcap.

%package -n pcapinfo
Summary:        Prints detailed information about the network devices
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}

%description -n pcapinfo
pcapinfo prints detailed information about the network devices and Pcap library
available on the current host.

%prep
%setup -q -n "Net-Pcap-%{version}"

if pkg-config --atleast-version=1.9.0 libpcap; then
%patch1 -p1
fi

sed -i '/^auto_install/d' Makefile.PL

%build
perl Makefile.PL PREFIX="%{_prefix}"
make %{?_smp_mflags} \
    CCFLAGS="-Wall -Wextra -I/usr/include/pcap" \
    CC="gcc"

%install
%perl_make_install
install -D -m0755 eg/pcapdump "%{buildroot}%{_bindir}/pcapdump"
%perl_process_packlist

# make test is just borked when not running as root

%files
%doc Changes README
%dir %{perl_vendorarch}/Net
%{perl_vendorarch}/Net/Pcap.pm
%dir %{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Net/Pcap
%doc %{perl_man3dir}/Net::Pcap.%{perl_man3ext}%{ext_man}

%files -n pcapdump
%{_bindir}/pcapdump

%files -n pcapinfo
%{_bindir}/pcapinfo
%{_mandir}/man1/pcapinfo.1%{?ext_man}

%changelog
