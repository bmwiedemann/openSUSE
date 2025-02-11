#
# spec file for package perl-Crypt-URandom
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


%define cpan_name Crypt-URandom
Name:           perl-Crypt-URandom
Version:        0.530.0
Release:        0
# 0.53 -> normalize -> 0.530.0
%define cpan_version 0.53
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provide non blocking randomness
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDICK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.26
BuildRequires:  perl(Test::Pod) >= 1.14
Requires:       perl(Carp) >= 1.26
Provides:       perl(Crypt::URandom) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This Module is intended to provide an interface to the strongest available
source of non-blocking randomness on the current platform. Platforms
currently supported are anything supporting getrandom(2), /dev/urandom and
versions of Windows greater than or equal to Windows 2000.

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
%doc Changes README README.md SECURITY.md
%license LICENSE

%changelog
