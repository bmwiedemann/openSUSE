#
# spec file for package perl-List-AllUtils
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


%define cpan_name List-AllUtils
Name:           perl-List-AllUtils
Version:        0.19
Release:        0
Summary:        Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized[cut]
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::SomeUtils) >= 0.58
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(List::UtilsBy) >= 0.11
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(List::SomeUtils) >= 0.58
Requires:       perl(List::Util) >= 1.56
Requires:       perl(List::UtilsBy) >= 0.11
%{perl_requires}

%description
Are you sick of trying to remember whether a particular helper is defined
in List::Util, List::SomeUtils or List::UtilsBy? I sure am. Now you don't
have to remember. This module will export all of the functions that either
of those three modules defines.

Note that all function documentation has been shamelessly copied from
List::Util, List::SomeUtils and List::UtilsBy.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md precious.toml README.md
%license LICENSE

%changelog
