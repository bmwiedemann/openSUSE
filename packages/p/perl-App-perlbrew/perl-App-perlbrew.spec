#
# spec file for package perl-App-perlbrew
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


%define cpan_name App-perlbrew
Name:           perl-App-perlbrew
Version:        0.92
Release:        0
Summary:        Manage perl installations in your C<$HOME>
License:        MIT
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Perl::Releases) >= 5.20210320
BuildRequires:  perl(Capture::Tiny) >= 0.36
BuildRequires:  perl(Devel::PatchPerl) >= 2.08
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.22
BuildRequires:  perl(File::Temp) >= 0.2304
BuildRequires:  perl(File::Which) >= 1.21
BuildRequires:  perl(IO::All) >= 0.51
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Path::Class) >= 0.33
BuildRequires:  perl(Pod::Parser) >= 1.63
BuildRequires:  perl(Pod::Usage) >= 1.68
BuildRequires:  perl(Test::Exception) >= 0.320000
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::NoWarnings) >= 1.04
BuildRequires:  perl(Test::Output) >= 1.03
BuildRequires:  perl(Test::Simple) >= 1.001002
BuildRequires:  perl(Test::Spec) >= 0.49
BuildRequires:  perl(Test::TempDir::Tiny) >= 0.016
BuildRequires:  perl(local::lib) >= 2.000014
Requires:       perl(CPAN::Perl::Releases) >= 5.20210320
Requires:       perl(Capture::Tiny) >= 0.36
Requires:       perl(Devel::PatchPerl) >= 2.08
Requires:       perl(ExtUtils::MakeMaker) >= 7.22
Requires:       perl(File::Temp) >= 0.2304
Requires:       perl(JSON::PP)
Requires:       perl(Pod::Parser) >= 1.63
Requires:       perl(Pod::Usage) >= 1.68
Requires:       perl(local::lib) >= 2.000014
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  curl
BuildRequires:  groff
BuildRequires:  wget
# MANUAL END

%description
perlbrew is a program to automate the building and installation of perl in
an easy way. It provides multiple isolated perl environments, and a
mechanism for you to switch between them.

Everything are installed unter '~/perl5/perlbrew'. You then need to include
a bashrc/cshrc provided by perlbrew to tweak the PATH for you. You then can
benefit from not having to run 'sudo' commands to install cpan modules
because those are installed inside your 'HOME' too.

For the documentation of perlbrew usage see perlbrew command on at
https://metacpan.org/, or by running 'perlbrew help', or by visiting at
https://perlbrew.pl/. The following documentation features the API of
'App::perlbrew' module, and may not be remotely close to what your want to
read.

%prep
%autosetup  -n %{cpan_name}-%{version}
# MANUAL BEGIN
chmod a+x t/fake-bin/curl
# MANUAL END

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
