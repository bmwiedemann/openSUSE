#
# spec file for package perl-ldap
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


%define cpan_name perl-ldap
Name:           perl-ldap
Version:        0.66
Release:        0
Summary:        Client Interface for LDAP Servers
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/perl-ldap
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARSCHAP/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl-Authen-SASL
BuildRequires:  perl-Convert-ASN1
BuildRequires:  perl-IO-Socket-SSL
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-macros
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Writer)
Requires:       perl-Convert-ASN1
Requires:       perl-URI
Requires:       perl-XML-Parser
Provides:       perl-Net-LDAP = %{version}
Provides:       perl_ldp
Obsoletes:      perl-Net-LDAP < %{version}
Obsoletes:      perl_ldp
BuildArch:      noarch
%{perl_requires}

%description
A Client interface for LDAP servers.

%prep
%setup -q -n perl-ldap-%{version}
find . -type f -print0 | xargs -0 chmod 644
# MANUAL
find contrib -type f | xargs -n 1 sed -i "s@/usr/local/bin/perl@%{_bindir}/perl@"

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CREDITS README TODO

%changelog
