#
# spec file for package perl-Net-DNS-Resolver-Programmable
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-DNS-Resolver-Programmable
Version:        0.009
Release:        0
%define cpan_name Net-DNS-Resolver-Programmable
Summary:        Programmable Dns Resolver Class for Offline
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-DNS-Resolver-Programmable/
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::DNS) >= 0.69
Requires:       perl(Net::DNS) >= 0.69
%{perl_requires}

%description
*Net::DNS::Resolver::Programmable* is a *Net::DNS::Resolver* descendant
class that allows a virtual DNS to be emulated instead of querying the real
DNS. A set of static DNS records may be supplied, or arbitrary code may be
specified as a means for retrieving DNS records, or even generating them on
the fly.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc CHANGES README TODO
%license LICENSE

%changelog
