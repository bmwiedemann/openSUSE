#
# spec file for package perl-List-SomeUtils-XS
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name List-SomeUtils-XS
Name:           perl-List-SomeUtils-XS
Version:        0.590.0
Release:        0
# 0.59 -> normalize -> 0.590.0
%define cpan_version 0.59
License:        Artistic-2.0
Summary:        XS implementation for List::SomeUtils
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.6
Provides:       perl(List::SomeUtils::XS) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
There are no user-facing parts here. See List::SomeUtils for API details.

You shouldn't have to install this module directly. When you install
List::SomeUtils, it checks whether your system has a compiler. If it does,
then it adds a dependency on this module so that it gets installed and you
have the faster XS implementation.

This distribution requires List::SomeUtils but to avoid a circular
dependency, that dependency is explicitly left out from the this
distribution's metadata. However, without LSU already installed this module
cannot function.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
