#
# spec file for package perl-Net-SSLGlue
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-SSLGlue
Version:        1.058
Release:        0
%define cpan_name Net-SSLGlue
Summary:        Add/Extend Ssl Support for Common Perl Modules
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-SSLGlue/
Source0:        http://www.cpan.org/authors/id/S/SU/SULLR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::SSL) >= 1.19
Requires:       perl(IO::Socket::SSL) >= 1.19
%{perl_requires}

%description
Some commonly used perl modules don't have SSL support at all, even if the
protocol supports it. Others have SSL support, but most of them don't do
proper checking of the server's certificate.

The 'Net::SSLGlue::*' modules try to add SSL support or proper certificate
checking to these modules. Currently support for the following modules is
available:

* Net::SMTP - add SSL from beginning or using STARTTLS

* Net::POP3 - add SSL from beginning or using STLS

* Net::FTP  - add SSL and IPv6 support to Net::FTP

* Net::LDAP - add proper certificate checking

* LWP - add proper certificate checking for older LWP versions

There is also a Net::SSLGlue::Socket package which combines ssl and non-ssl
and ipv6 capabilities to make it easier to enhance modules based on
IO::Socket::INET.

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
%doc Changes COPYRIGHT examples README

%changelog
