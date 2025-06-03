#
# spec file for package perl-IO-TieCombine
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


%define cpan_name IO-TieCombine
Name:           perl-IO-TieCombine
Version:        1.5.0
Release:        0
# 1.005 -> normalize -> 1.5.0
%define cpan_version 1.005
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Produce tied (and other) separate but combined variables
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
Provides:       perl(IO::TieCombine) = %{version}
Provides:       perl(IO::TieCombine::Handle) = %{version}
Provides:       perl(IO::TieCombine::Scalar) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
produce tied (and other) separate but combined variables

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
