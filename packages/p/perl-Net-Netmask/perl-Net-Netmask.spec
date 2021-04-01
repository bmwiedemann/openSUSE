#
# spec file for package perl-Net-Netmask
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Net-Netmask
Name:           perl-Net-Netmask
Version:        2.0001
Release:        0
Summary:        Parse, manipulate and lookup IP network blocks
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMASLAK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
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
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING errors.err README TODO
%license LICENSE

%changelog
