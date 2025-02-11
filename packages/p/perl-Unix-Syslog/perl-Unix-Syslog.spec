#
# spec file for package perl-Unix-Syslog
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Unix-Syslog
Name:           perl-Unix-Syslog
Version:        1.100.0
Release:        0
# 1.1 -> normalize -> 1.100.0
%define cpan_version 1.1
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0
Summary:        Perl interface to the UNIX syslog(3) calls
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MH/MHARNISCH/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Unix::Syslog) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides an interface to the system logger *syslogd*(8) via
Perl's XSUBs. The implementation attempts to resemble the native
libc-functions of your system, so that anyone being familiar with
_syslog.h_ should be able to use this module right away.

In contrary to Sys::Syslog(3), this modules does not open a network
connection to send the messages. This can help you to avoid opening
security holes in your computer (see "FAQ").

The subs imported by the tag 'macros' are simply wrappers around the most
important '#defines' in your system's C header file _syslog.h_. The macros
return integer values that are used to specify options, facilities and
priorities in a more or less portable way. They also provide general
information about your local syslog mechanism. Check syslog(3) and your
local _syslog.h_ for information about the macros, options and facilities
available on your system.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license Artistic

%changelog
