#
# spec file for package perl-Devel-PatchPerl
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


%define cpan_name Devel-PatchPerl
Name:           perl-Devel-PatchPerl
Version:        2.140.0
Release:        0
# 2.14 -> normalize -> 2.140.0
%define cpan_version 2.14
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Patch perl source a la Devel::PPPort's buildperl.pl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::pushd) >= 1.0
BuildRequires:  perl(Module::Pluggable)
Requires:       perl(File::pushd) >= 1.0
Requires:       perl(Module::Pluggable)
Provides:       perl(Devel::PatchPerl) = %{version}
Provides:       perl(Devel::PatchPerl::Hints) = %{version}
Provides:       perl(Devel::PatchPerl::Plugin) = %{version}
Provides:       perl(Devel::PatchPerl::Plugin::TEST)
%undefine       __perllib_provides
%{perl_requires}

%description
Devel::PatchPerl is a modularisation of the patching code contained in
Devel::PPPort's 'buildperl.pl'.

It does not build perls, it merely provides an interface to the source
patching functionality.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
