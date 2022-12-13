#
# spec file for package perl-Module-Build
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Module-Build
Name:           perl-Module-Build
Version:        0.423200
Release:        0
%define cpan_version 0.4232
Provides:       perl(Module::Build) = 0.423200
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Build and install Perl modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta) >= 2.142060
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.003
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(Module::Metadata) >= 1.000002
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4401
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(TAP::Harness) >= 3.29
BuildRequires:  perl(version) >= 0.87
Requires:       perl(CPAN::Meta) >= 2.142060
Requires:       perl(ExtUtils::CBuilder) >= 0.27
Requires:       perl(ExtUtils::ParseXS) >= 2.21
Requires:       perl(Module::Metadata) >= 1.000002
Requires:       perl(Perl::OSType) >= 1
Requires:       perl(TAP::Harness) >= 3.29
Requires:       perl(version) >= 0.87
Recommends:     perl(ExtUtils::Manifest) >= 1.54
%{perl_requires}

%description
'Module::Build' is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to 'ExtUtils::MakeMaker'.
Developers may alter the behavior of the module through subclassing. It
also does not require a 'make' on your system - most of the 'Module::Build'
code is pure-perl and written in a very cross-platform way.

See "COMPARISON" for more comparisons between 'Module::Build' and other
installer tools.

To install 'Module::Build', and any other module that uses 'Module::Build'
for its installation process, do the following:

  perl Build.PL       # 'Build.PL' script creates the 'Build' script
  ./Build             # Need ./ to ensure we're using this "Build" script
  ./Build test        # and not another one that happens to be in the PATH
  ./Build install

This illustrates initial configuration and the running of three 'actions'.
In this case the actions run are 'build' (the default action), 'test', and
'install'. Other actions defined so far include:

  build                          manifest
  clean                          manifest_skip
  code                           manpages
  config_data                    pardist
  diff                           ppd
  dist                           ppmdist
  distcheck                      prereq_data
  distclean                      prereq_report
  distdir                        pure_install
  distinstall                    realclean
  distmeta                       retest
  distsign                       skipcheck
  disttest                       test
  docs                           testall
  fakeinstall                    testcover
  help                           testdb
  html                           testpod
  install                        testpodcoverage
  installdeps                    versioninstall

You can run the 'help' action for a complete list of actions.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
# MANUAL BEGIN
# avoid conflict with Perl's own supplied version
mv %{buildroot}/usr/bin/config_data %{buildroot}/usr/bin/config_data-%{version}
rename config_data config_data-%{version} %{buildroot}/%{_mandir}/man1/config_data.*
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
