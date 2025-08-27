#
# spec file for package perl-Devel-OverloadInfo
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


%define cpan_name Devel-OverloadInfo
Name:           perl-Devel-OverloadInfo
Version:        0.8.0
Release:        0
# 0.008 -> normalize -> 0.8.0
%define cpan_version 0.008
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Introspect overloaded operators
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Package::Stash) >= 0.140
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(MRO::Compat)
Requires:       perl(Package::Stash) >= 0.140
Provides:       perl(Devel::OverloadInfo) = %{version}
Provides:       perl(ExtUtils::HasCompiler) = 0.25.0
%undefine       __perllib_provides
%{perl_requires}

%description
Devel::OverloadInfo returns information about overloaded operators for a
given class (or object), including where in the inheritance hierarchy the
overloads are declared and where the code implementing them is.

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
