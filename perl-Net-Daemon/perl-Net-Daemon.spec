#
# spec file for package perl-Net-Daemon
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Net-Daemon
Version:        0.48
Release:        0
%define cpan_name Net-Daemon
Summary:        Perl extension for portable daemons
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Daemon/
Source:         http://www.cpan.org/authors/id/M/MN/MNOONING/Net-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl 5.005
and threads, but can work with fork() and Perl 5.004.

The Net::Daemon class offers methods for the most common tasks a daemon
needs: Starting up, logging, accepting clients, authorization, restricting
its own environment for security and doing the true work. You only have to
override those methods that aren't appropriate for you, but typically
inheriting will safe you a lot of work anyways.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
# requires syslog in chroot
# %{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc ChangeLog README regexp-threads

%changelog
