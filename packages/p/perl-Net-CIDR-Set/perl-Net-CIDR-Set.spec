#
# spec file for package perl-Net-CIDR-Set
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-CIDR-Set
Version:        0.13
Release:        0
%define cpan_name Net-CIDR-Set
Summary:        Manipulate sets of IP addresses
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-CIDR-Set/
Source:         http://www.cpan.org/authors/id/A/AN/ANDYA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.42
%{perl_requires}

%description
'Net::CIDR::Set' represents sets of IP addresses and allows standard set
operations (union, intersection, membership test etc) to be performed on
them.

In spite of the name it can work with sets consisting of arbitrary ranges
of IP addresses - not just CIDR blocks.

Both IPv4 and IPv6 addresses are handled - but they may not be mixed in the
same set. You may explicitly set the personality of a set:

  my $ip4set = Net::CIDR::Set->new({ type => 'ipv4 }, '10.0.0.0/8');

Normally this isn't necessary - the set will guess its personality from the
first data that is added to it.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
