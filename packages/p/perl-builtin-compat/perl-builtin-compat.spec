#
# spec file for package perl-builtin-compat
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


%define cpan_name builtin-compat
Name:           perl-builtin-compat
Version:        0.3.3
Release:        0
# 0.003003 -> normalize -> 0.3.3
%define cpan_version 0.003003
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provide builtin functions for older perl versions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Scalar::Util) >= 1.36
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::clean)
Requires:       perl(Scalar::Util) >= 1.36
Requires:       perl(namespace::clean)
Provides:       perl(builtin::compat) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Provides builtin functions for perl versions that do not include the
builtin module.

No functions are exported by default.

This module does its best to behave similar to builtin, which creates its
exported functions as lexicals. The functions will be created in the
currently compiling scope, not the immediate caller of
'builtin::compat->import'. The functions will also be removed at the end of
the compilation scope using namespace::clean.

The builtin functions will be used directly when they are available.

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
