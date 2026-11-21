#
# spec file for package perl-Crypt-SysRandom
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


%define cpan_name Crypt-SysRandom
Name:           perl-Crypt-SysRandom
Version:        0.8.0
Release:        0
# 0.008 -> normalize -> 0.8.0
%define cpan_version 0.008
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to system randomness
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MIME::Base64) >= 3.11
Requires:       perl(MIME::Base64) >= 3.11
Provides:       perl(Crypt::SysRandom) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Crypt::SysRandom::XS) >= 0.11
%{perl_requires}

%description
This module uses whatever interface is available to procure
cryptographically random data from the system. All functions are optionally
exported.

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
%license LICENSE

%changelog
