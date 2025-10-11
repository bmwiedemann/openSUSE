#
# spec file for package perl-Test-TCP
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


%define cpan_name Test-TCP
Name:           perl-Test-TCP
Version:        2.220.0
Release:        0
# 2.22 -> normalize -> 2.220.0
%define cpan_version 2.22
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Testing TCP program
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork) >= 0.290
Requires:       perl(IO::Socket::IP)
Requires:       perl(Test::SharedFork) >= 0.290
Provides:       perl(Net::EmptyPort)
Provides:       perl(Test::TCP) = %{version}
Provides:       perl(Test::TCP::CheckPort)
%undefine       __perllib_provides
%{perl_requires}

%description
Test::TCP is a test utility to test TCP/IP-based server programs.

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
%doc Changes README.md
%license LICENSE

%changelog
