#
# spec file for package perl-Proc-ProcessTable
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.637.0
Release:        0
# 0.637 -> normalize -> 0.637.0
%define cpan_version 0.637
#Upstream: Artistic-2.0
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND GPL-2.0-only
Summary:        Perl extension to access the unix process table
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JW/JWB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Proc::Killall) = 1.0.0
Provides:       perl(Proc::Killfam) = 1.0.0
Provides:       perl(Proc::ProcessTable) = %{version}
Provides:       perl(Proc::ProcessTable::Process) = 0.20.0
%undefine       __perllib_provides
%{perl_requires}

%description
Perl interface to the unix process table.

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
%doc Changes README README.aix README.bsdi README.cygwin README.darwin README.dec_osf README.freebsd-kvm README.freebsd-procfs README.hpux README.linux README.md README.MSWin32 README.netbsd README.openbsd README.solaris README.sunos README.unixware

%changelog
