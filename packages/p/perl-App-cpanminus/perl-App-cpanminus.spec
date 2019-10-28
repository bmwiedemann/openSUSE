#
# spec file for package perl-App-cpanminus
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-App-cpanminus
Version:        1.7043
Release:        0
%define cpan_name App-cpanminus
Summary:        Get, Unpack, Build and Install Modules From Cpan
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-cpanminus/
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        http://pkgs.fedoraproject.org/cgit/perl-App-cpanminus.git/plain/fatunpack
Source2:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
# Run-time:
# Nothing special. The tests are very poor. But we run perl -c at built-time
# to check for correct unpacking. So we need non-optional run-time
# dependencies at build-time too:
BuildRequires:  perl(Config)
BuildRequires:  perl(aliased)
BuildRequires:  perl(constant)
# CPAN::DistnameInfo not needed for compilation
# CPAN::Meta not needed for copmilation
# CPAN::Meta::Check not needed for compilation
# CPAN::Meta::Prereqs not needed for compilation
BuildRequires:  perl(CPAN::Meta::Requirements)
# CPAN::Meta::YAML not needed for compilation
BuildRequires:  perl(Cwd)
# Digest::SHA not needed for compilation
# Dumpvalue not needed for compilation
# ExtUtils::Manifest not needed for compilation
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
# File::pushd not needed for compilation
BuildRequires:  perl(File::Temp)
# HTTP::Tiny not needed for compilation
# JSON::PP not needed for compilation
# local::lib not needed for compilation
# Module::CoreList not needed for compilation
# Module::CPANfile not needed for compilation
# Module::Metadata not needed for compilation
BuildRequires:  perl(Parse::CPAN::Meta)
# POSIX not needed for compilation
# Safe not needed for compilation
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(version)
# version::vpp not needed for compilation
BuildRequires:  perl(warnings::register)
# YAML not needed for compilation
# Tests:
BuildRequires:  perl(Test::More)
# Current dependency generator cannot parse compressed code. Use PPI to find
# them, and list them manually:
# Archive::Tar is optional
# Archive::Zip is optional
# Compress::Zlib is optional
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::Meta::Check)
Requires:       perl(CPAN::Meta::Prereqs)
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::Install) >= 1.46
Requires:       perl(ExtUtils::MakeMaker) >= 6.31
Requires:       perl(ExtUtils::Manifest)
# File::HomeDir is optional
Requires:       perl(File::pushd)
# HTTP getter by LWP::UserAgent or wget or curl or HTTP::Tiny
Requires:       perl(HTTP::Tiny)
Requires:       perl(Parse::PMFile)
Requires:       perl(local::lib)
# LWP::Protocol::https is optional
# LWP::UserAgent is optional
Requires:       perl(Module::Build)
Requires:       perl(Module::CPANfile)
Requires:       perl(Module::CoreList)
Requires:       perl(Module::Metadata)
# Module::Signature is optional
Requires:       perl(String::ShellQuote)
# Win32 not used
Requires:       perl(YAML)

Provides:       cpanm = %{version}-%{release}
Obsoletes:      cpanm <= 1.5010
# MANUAL END

%description
cpanminus is a script to get, unpack, build and install modules from CPAN
and does nothing else.

It's dependency free (can bootstrap itself), requires zero configuration,
and stands alone. When running, it requires only 10MB of RAM.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
# Unbundle fat-packed modules
podselect lib/App/cpanminus.pm > lib/App/cpanminus.pod

for F in bin/cpanm lib/App/cpanminus/fatscript.pm; do
   perl %{SOURCE1} --libdir lib --filter '^App/cpanminus' "$F" > "${F}.stripped"
   perl -c -Ilib "${F}.stripped"
   mv "${F}.stripped" "$F"
done
# MANUAL END

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
