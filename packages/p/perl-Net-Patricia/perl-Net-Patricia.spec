#
# spec file for package perl-Net-Patricia
#
# Copyright (c) 2023 SUSE LLC
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


#disable test suite as it doesn't work at all without being online
#and our build hosts are completly without network interfaces
%bcond_with test

Name:           perl-Net-Patricia
Version:        1.22
Release:        0
%define cpan_name Net-Patricia
Summary:        Patricia Trie perl module for fast IP address lookups
License:        BSD-2-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/Net-Patricia/
Source:         http://www.cpan.org/authors/id/G/GR/GRUBER/%{cpan_name}-%{version}.tar.gz
Patch1:         no-libnsl.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::CIDR::Lite) >= 0.20
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version)
Requires:       perl(Net::CIDR::Lite) >= 0.20
Requires:       perl(Socket6)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(version)
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
%setup -q -n %{cpan_name}-%{version}
%patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%if %{with test}
%check
%{__make} test
%endif

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes COPYING MYMETA.json MYMETA.yml README

%changelog
