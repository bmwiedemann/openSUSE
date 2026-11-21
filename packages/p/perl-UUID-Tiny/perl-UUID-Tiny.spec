#
# spec file for package perl-UUID-Tiny
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


%define cpan_name UUID-Tiny
Name:           perl-UUID-Tiny
Version:        1.40.0
Release:        0
# 1.04 -> normalize -> 1.40.0
%define cpan_version 1.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Pure Perl UUID Support With Functional Interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAUGUSTIN/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(UUID::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
UUID::Tiny is a lightweight, low dependency Pure Perl module for UUID
creation and testing. This module provides the creation of version 1 time
based UUIDs (using random multicast MAC addresses), version 3 MD5 based
UUIDs, version 4 random UUIDs, and version 5 SHA-1 based UUIDs.

ATTENTION! UUID::Tiny uses Perl's 'rand()' to create the basic random
numbers, so the created v4 UUIDs are *not* cryptographically strong!

No fancy OO interface, no plethora of different UUID representation formats
and transformations - just string and binary. Conversion, test and time
functions equally accept UUIDs and UUID strings, so don't bother to convert
UUIDs for them!

Continuing with 1.0x versions all constants and public functions are
exported by default, but this will change in the future (see below).

UUID::Tiny deliberately uses a minimal functional interface for UUID
creation (and conversion/testing), because in this case OO looks like
overkill to me and makes the creation and use of UUIDs unnecessarily
complicated.

If you need raw performance for UUID creation, or the real MAC address in
version 1 UUIDs, or an OO interface, and if you can afford module
compilation and installation on the target system, then better look at
other CPAN UUID modules like Data::UUID.

This module is "fork safe", especially for random UUIDs (it works around
Perl's rand() problem when forking processes).

This module is currently *not* "thread safe". Even though I've incorporated
some changes proposed by Michael G. Schwern (thanks!), Digest::MD5 and
Digest::SHA seem so have trouble with threads. There is a test file for
threads, but it is de-activated. So use at your own risk!

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
%doc Changes README

%changelog
