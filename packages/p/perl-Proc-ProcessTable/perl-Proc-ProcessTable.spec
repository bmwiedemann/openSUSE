#
# spec file for package perl-Proc-ProcessTable
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Proc-ProcessTable
Name:           perl-Proc-ProcessTable
Version:        0.634
Release:        0
#Upstream: Artistic-2.0
Summary:        Perl extension to access the unix process table
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND GPL-2.0-only
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JW/JWB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Perl interface to the unix process table.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README README.aix README.bsdi README.cygwin README.darwin README.dec_osf README.freebsd-kvm README.freebsd-procfs README.hpux README.linux README.md README.MSWin32 README.netbsd README.openbsd README.solaris README.sunos README.unixware

%changelog
