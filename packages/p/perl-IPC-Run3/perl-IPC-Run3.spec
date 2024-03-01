#
# spec file for package perl-IPC-Run3
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name IPC-Run3
Name:           perl-IPC-Run3
Version:        0.49.0
Release:        0
%define cpan_version 0.049
#Upstream: SUSE-Public-Domain
License:        Artistic-1.0 OR BSD-2-Clause OR GPL-2.0-or-later
Summary:        Run a subprocess with input/output redirection
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(IPC::Run3) = %{version}
Provides:       perl(IPC::Run3::ProfArrayBuffer) = %{version}
Provides:       perl(IPC::Run3::ProfLogReader) = %{version}
Provides:       perl(IPC::Run3::ProfLogger) = %{version}
Provides:       perl(IPC::Run3::ProfPP) = %{version}
Provides:       perl(IPC::Run3::ProfReporter) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using 'system', 'qx', and 'open3' with a simple, extremely
Perlish API.

Speed, simplicity, and portability are paramount. (That's speed of Perl
code; which is often much slower than the kind of buffered I/O that this
module uses to spool input to and output from the child command.)

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%license LICENSE

%changelog
