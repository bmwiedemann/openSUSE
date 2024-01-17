#
# spec file for package perl-Net-Daemon
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


Name:           perl-Net-Daemon
Version:        0.49
Release:        0
#Upstream:  Am Eisteich 9 72555 Metzingen Germany Phone: +49 7123 14887 Email: joe@ispsoft.de All rights reserved. You may distribute this package under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
%define cpan_name Net-Daemon
Summary:        Perl extension for portable daemons
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sys::Syslog) >= 0.29
Requires:       perl(Sys::Syslog) >= 0.29
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
%doc ChangeLog README

%changelog
