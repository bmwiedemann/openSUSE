#
# spec file for package perl-Net-Patricia
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Net-Patricia
Name:           perl-Net-Patricia
Version:        1.240.0
Release:        0
# 1.24 -> normalize -> 1.240.0
%define cpan_version 1.24
#Upstream: SUSE-Public-Domain
License:        BSD-2-Clause AND GPL-2.0-or-later
Summary:        Patricia Trie for fast IP address lookups
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GRUBER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::CIDR::Lite) >= 0.200
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.0
BuildRequires:  perl(version)
Requires:       perl(Net::CIDR::Lite) >= 0.200
Requires:       perl(Socket6)
Requires:       perl(version)
Provides:       perl(Net::Patricia) = %{version}
Provides:       perl(Net::Patricia::AF_INET)
Provides:       perl(Net::Patricia::AF_INET6)
%undefine       __perllib_provides
%{perl_requires}

%description
This module uses a Patricia Trie data structure to quickly perform IP
address prefix matching for applications such as IP subnet, network or
routing table lookups. The data structure is based on a radix tree using a
radix of two, so sometimes you see patricia implementations called "radix"
as well. The term "Trie" is derived from the word "retrieval" but is
pronounced like "try". Patricia stands for "Practical Algorithm to Retrieve
Information Coded as Alphanumeric", and was first suggested for routing
table lookups by Van Jacobsen. Patricia Trie performance characteristics
are well-known as it has been employed for routing table lookups within the
BSD kernel since the 4.3 Reno release.

The BSD radix code is thoroughly described in "TCP/IP Illustrated, Volume
2" by Wright and Stevens and in the paper ``A Tree-Based Packet Routing
Table for Berkeley Unix'' by Keith Sklower.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license COPYING

%changelog
