#
# spec file for package perl-Net-Daemon
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Net-Daemon
Name:           perl-Net-Daemon
Version:        0.520.0
Release:        0
# 0.52 -> normalize -> 0.520.0
%define cpan_version 0.52
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for portable daemons
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sys::Syslog) >= 0.29
Requires:       perl(Sys::Syslog) >= 0.29
Provides:       perl(Net::Daemon) = %{version}
Provides:       perl(Net::Daemon::Log) = %{version}
Provides:       perl(Net::Daemon::Test) = %{version}
Provides:       perl(Net::Daemon::Test::Fork)
Provides:       perl(Net::Daemon::Test::Win32)
%undefine       __perllib_provides
%{perl_requires}

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl 5.006
and ithreads, but can work with fork() as well.

The Net::Daemon class offers methods for the most common tasks a daemon
needs: Starting up, logging, accepting clients, authorization, restricting
its own environment for security and doing the true work. You only have to
override those methods that aren't appropriate for you, but typically
inheriting will safe you a lot of work anyways.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc AI_POLICY.md ChangeLog README.md

%changelog
