#
# spec file for package perl-Net-DNS
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Net-DNS
Version:        1.28
Release:        0
%define cpan_name Net-DNS
Summary:        Perl Interface to the Domain Name System
License:        MIT
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.1
BuildRequires:  perl(Digest::HMAC) >= 1.03
BuildRequires:  perl(Digest::SHA) >= 5.23
BuildRequires:  perl(Encode) >= 2.26
BuildRequires:  perl(Getopt::Long) >= 2.43
BuildRequires:  perl(IO::Socket::IP) >= 0.38
BuildRequires:  perl(PerlIO) >= 1.05
BuildRequires:  perl(Scalar::Util) >= 1.25
BuildRequires:  perl(Time::Local) >= 1.19
Requires:       perl(Carp) >= 1.1
Requires:       perl(Digest::HMAC) >= 1.03
Requires:       perl(Digest::SHA) >= 5.23
Requires:       perl(Encode) >= 2.26
Requires:       perl(IO::Socket::IP) >= 0.38
Requires:       perl(PerlIO) >= 1.05
Requires:       perl(Scalar::Util) >= 1.25
Requires:       perl(Time::Local) >= 1.19
Recommends:     perl(Digest::BubbleBabble) >= 0.01
Recommends:     perl(Net::LibIDN2) >= 1
%{perl_requires}

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System
(DNS) resolver. It allows the programmer to perform DNS queries that are
beyond the capabilities of "gethostbyname" and "gethostbyaddr".

The programmer should be familiar with the structure of a DNS packet. See
RFC 1035 or DNS and BIND (Albitz & Liu) for details.

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
%doc Changes README

%changelog
