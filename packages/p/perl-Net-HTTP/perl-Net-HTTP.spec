#
# spec file for package perl-Net-HTTP
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


Name:           perl-Net-HTTP
Version:        6.19
Release:        0
%define cpan_name Net-HTTP
Summary:        Low-level HTTP connection (client)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(URI)
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(URI)
%{perl_requires}

%description
The 'Net::HTTP' class is a low-level HTTP client. An instance of the
'Net::HTTP' class represents a connection to an HTTP server. The HTTP
protocol is described in RFC 2616. The 'Net::HTTP' class supports
'HTTP/1.0' and 'HTTP/1.1'.

'Net::HTTP' is a sub-class of one of 'IO::Socket::IP' (IPv6+IPv4),
'IO::Socket::INET6' (IPv6+IPv4), or 'IO::Socket::INET' (IPv4 only). You can
mix the methods described below with reading and writing from the socket
directly. This is not necessary a good idea, unless you know what you are
doing.

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
%doc Changes CONTRIBUTORS README.md
%license LICENSE

%changelog
