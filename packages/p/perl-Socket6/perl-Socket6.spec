#
# spec file for package perl-Socket6
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


%define cpan_name Socket6
Name:           perl-Socket6
Version:        0.290.0
Release:        0
# 0.29 -> normalize -> 0.290.0
%define cpan_version 0.29
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        BSD-3-Clause
Summary:        IPv6 related part of the C socket.h defines and structure manipulators
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/U/UM/UMEMOTO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Socket6) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides glue routines to the various IPv6 functions.

If you use the Socket6 module, be sure to specify "use Socket" as well as
"use Socket6".

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc aclocal.m4 ChangeLog ftpmirror-1.96.diff im-140.diff README

%changelog
