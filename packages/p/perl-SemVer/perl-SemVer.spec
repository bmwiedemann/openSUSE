#
# spec file for package perl-SemVer
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


Name:           perl-SemVer
Version:        0.10.0
Release:        0
%define cpan_name SemVer
Summary:        Use semantic version numbers
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DW/DWHEELER/%{cpan_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.300000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.82
Requires:       perl(version) >= 0.82
Recommends:     perl(Test::Pod) >= 1.41
Recommends:     perl(Test::Pod::Coverage) >= 1.06
%{perl_requires}

%description
Use semantic version numbers

%prep
%setup -q -n %{cpan_name}-v%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md

%changelog
