#
# spec file for package perl-Net-Netmask
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Net-Netmask
Version:        1.9104
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name Net-Netmask
Summary:        Parse, Manipulate and Lookup Ip Network Blocks
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Netmask/
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMASLAK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::BigInt) >= 1.999811
BuildRequires:  perl(Test2::V0) >= 0.000111
BuildRequires:  perl(Test::UseAllModules) >= 0.17
Requires:       perl(Math::BigInt) >= 1.999811
Recommends:     perl(AnyEvent) >= 7.14
%{perl_requires}

%description
Net::Netmask parses and understands IPv4 and IPv6 CIDR blocks (see
https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing for more
information on CIDR blocks). It's built with an object-oriented interface,
with functions being methods that operate on a Net::Netmask object.

These methods provide nearly all types of information about a network block
that you might want.

There are also functions to insert a network block into a table and then
later lookup network blocks by IP address using that table. There are
functions to turn a IP address range into a list of CIDR blocks. There are
functions to turn a list of CIDR blocks into a list of IP addresses.

There is a function for sorting by text IP address.

All functions understand both IPv4 and IPv6. Matches, finds, etc, will
always return false when an IPv4 address is matched against an IPv6
address.

IPv6 support was added in 1.9104.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING errors.err README TODO
%license LICENSE

%changelog
