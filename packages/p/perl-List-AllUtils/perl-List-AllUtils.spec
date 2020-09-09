#
# spec file for package perl-List-AllUtils
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-List-AllUtils
Version:        0.18
Release:        0
%define cpan_name List-AllUtils
Summary:        Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized[cut]
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::SomeUtils) >= 0.56
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(List::UtilsBy) >= 0.11
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(List::SomeUtils) >= 0.56
Requires:       perl(List::Util) >= 1.45
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
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
