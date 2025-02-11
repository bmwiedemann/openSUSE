#
# spec file for package perl-Alien-Libxml2
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


%define cpan_name Alien-Libxml2
Name:           perl-Alien-Libxml2
Version:        0.190.0
Release:        0
# 0.19 -> normalize -> 0.190.0
%define cpan_version 0.19
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Install the C libxml2 library on your system
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Base) >= 2.370
BuildRequires:  perl(Alien::Build) >= 2.370
BuildRequires:  perl(Alien::Build::MM) >= 2.370
BuildRequires:  perl(Alien::Build::Plugin::Build::SearchDep) >= 0.350
BuildRequires:  perl(Alien::Build::Plugin::Download::GitLab)
BuildRequires:  perl(Alien::Build::Plugin::Prefer::BadVersion) >= 1.50.0
BuildRequires:  perl(Alien::Build::Plugin::Probe::Vcpkg)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien)
Requires:       perl(Alien::Base) >= 2.370
Provides:       perl(Alien::Libxml2) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  perl-URI
BuildRequires:  perl(Mojo::DOM58)
BuildRequires:  perl(Sort::Versions)
# MANUAL END

%description
This module provides 'libxml2' for other modules to use.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc alienfile Changes README
%license LICENSE

%changelog
