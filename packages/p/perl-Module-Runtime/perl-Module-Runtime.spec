#
# spec file for package perl-Module-Runtime
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


%define cpan_name Module-Runtime
Name:           perl-Module-Runtime
Version:        0.17.0
Release:        0
# 0.017 -> normalize -> 0.17.0
%define cpan_version 0.017
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Runtime module handling
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Module::Runtime) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time. This module avoids
using any other modules, so that it can be used in low-level
infrastructure.

The parts of this module that work with module names apply the same syntax
that is used for barewords in Perl source. In principle this syntax can
vary between versions of Perl, and this module applies the syntax of the
Perl on which it is running. In practice the usable syntax hasn't changed
yet. There's some intent for Unicode module names to be supported in the
future, but this hasn't yet amounted to any consistent facility.

The functions of this module whose purpose is to load modules include
workarounds for three old Perl core bugs regarding 'require'. These
workarounds are applied on any Perl version where the bugs exist, except
for a case where one of the bugs cannot be adequately worked around in pure
Perl.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README TODO
%license LICENSE

%changelog
