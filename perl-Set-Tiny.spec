#
# spec file for package perl-Set-Tiny
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


%define cpan_name Set-Tiny
Name:           perl-Set-Tiny
Version:        0.50.0
Release:        0
# 0.05 -> normalize -> 0.50.0
%define cpan_version 0.05
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple sets of strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARFREITAS/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Set::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Set::Tiny is a thin wrapper around regular Perl hashes to perform often
needed set operations, such as testing two sets of strings for equality, or
checking whether one is contained within the other.

For a more complete implementation of mathematical set theory, see
Set::Scalar. For sets of arbitrary objects, see Set::Object.

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
%doc Changes examples README README.md
%license LICENSE

%changelog
