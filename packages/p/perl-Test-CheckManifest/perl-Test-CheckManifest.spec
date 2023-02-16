#
# spec file for package perl-Test-CheckManifest
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Test-CheckManifest
Name:           perl-Test-CheckManifest
Version:        1.43
Release:        0
License:        Artistic-2.0
Summary:        Check if your Manifest matches your distro
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/RENEEB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Cwd) >= 3.75
BuildRequires:  perl(Pod::Coverage::TrustPod)
Requires:       perl(Cwd) >= 3.75
%{perl_requires}

%description
Check if your Manifest matches your distro

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
touch dummy.list
mv *.files *.list ..
%{__make} test
mv ../*.files ../*.list .

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md CONTRIBUTORS README
%license LICENSE

%changelog
