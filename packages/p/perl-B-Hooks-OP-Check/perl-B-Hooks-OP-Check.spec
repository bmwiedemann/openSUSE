#
# spec file for package perl-B-Hooks-OP-Check
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


%define cpan_name B-Hooks-OP-Check
Name:           perl-B-Hooks-OP-Check
Version:        0.220.0
Release:        0
# 0.22 -> normalize -> 0.220.0
%define cpan_version 0.22
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Wrap OP check callbacks
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        perl-B-Hooks-OP-Check-rpmlintrc
Source2:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
BuildRequires:  perl(parent)
Requires:       perl(parent)
Provides:       perl(B::Hooks::OP::Check) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides a C API for XS modules to hook into the callbacks of
'PL_check'.

ExtUtils::Depends is used to export all functions for other XS modules to
use. Include the following in your Makefile.PL:

    my $pkg = ExtUtils::Depends->new('Your::XSModule', 'B::Hooks::OP::Check');
    WriteMakefile(
        ... # your normal makefile flags
        $pkg->get_makefile_vars,
    );

Your XS module can now include 'hook_op_check.h'.

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
