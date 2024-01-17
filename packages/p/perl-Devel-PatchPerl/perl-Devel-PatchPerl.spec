#
# spec file for package perl-Devel-PatchPerl
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


%define cpan_name Devel-PatchPerl
Name:           perl-Devel-PatchPerl
Version:        2.08
Release:        0
Summary:        Patch perl source a la Devel::PPPort's buildperl.pl
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::pushd) >= 1.00
BuildRequires:  perl(Module::Pluggable)
Requires:       perl(File::pushd) >= 1.00
Requires:       perl(Module::Pluggable)
%{perl_requires}

%description
Devel::PatchPerl is a modularisation of the patching code contained in
Devel::PPPort's 'buildperl.pl'.

It does not build perls, it merely provides an interface to the source
patching functionality.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
