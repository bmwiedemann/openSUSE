#
# spec file for package perl-Net-INET6Glue
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Net-INET6Glue
Version:        0.603
Release:        0
%define cpan_name Net-INET6Glue
Summary:        Make common modules IPv6 ready by hotpatching
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-INET6Glue/
Source:         http://www.cpan.org/authors/id/S/SU/SULLR/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::IP) >= 0.25
Requires:       perl(IO::Socket::IP) >= 0.25
%{perl_requires}

%description
the Net::INET6Glue manpage is a collection of modules to make common
modules IPv6 ready by hotpatching them.

Unfortunatly the current state of IPv6 support in perl is that no IPv6
support is in the core and that a lot of important modules (like the
Net::FTP manpage, the Net::SMTP manpage, the LWP manpage,...) do not
support IPv6 even if the modules for IPv6 sockets like the Socket6 manpage,
the IO::Socket::IP manpage or the IO::Socket::INET6 manpage are available.

This module tries to mitigate this by hotpatching. Currently the following
submodules are available:

* the Net::INET6Glue::INET_is_INET6 manpage

  Makes the IO::Socket::INET manpage behave like the IO::Socket::IP manpage
  (with fallback to like the IO::Socket::INET6 manpage), especially make it
  capable to create IPv6 sockets. This makes the LWP manpage, the Net::SMTP
  manpage and others IPv6 capable.

* the Net::INET6Glue::FTP manpage

  Hotpatches the Net::FTP manpage to support EPRT and EPSV commands which
  are needed to deal with FTP over IPv6. Also loads the
  Net::INET6Glue::INET_is_INET6 manpage.

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
%doc Changes COPYRIGHT README

%changelog
