#
# spec file for package perl-App-FatPacker
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


%define cpan_name App-FatPacker
Name:           perl-App-FatPacker
Version:        0.10.8
Release:        0
# 0.010008 -> normalize -> 0.10.8
%define cpan_version 0.010008
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Pack your dependencies onto your script file
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.82
Provides:       perl(App::FatPacker) = %{version}
Provides:       perl(App::FatPacker::Trace)
%undefine       __perllib_provides
%{perl_requires}

%description
pack your dependencies onto your script file

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
