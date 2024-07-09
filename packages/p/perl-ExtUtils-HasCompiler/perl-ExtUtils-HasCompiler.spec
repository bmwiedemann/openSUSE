#
# spec file for package perl-ExtUtils-HasCompiler
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


%define cpan_name ExtUtils-HasCompiler
Name:           perl-ExtUtils-HasCompiler
Version:        0.25.0
Release:        0
# 0.025 -> normalize -> 0.25.0
%define cpan_version 0.025
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Check for the presence of a compiler
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(ExtUtils::HasCompiler) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module tries to check if the current system is capable of compiling,
linking and loading an XS module.

*Notice*: this is an early release, interface stability isn't guaranteed
yet.

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
