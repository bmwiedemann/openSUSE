#
# spec file for package perl-Module-Signature
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Module-Signature
Name:           perl-Module-Signature
Version:        0.890.0
Release:        0
# 0.89 -> normalize -> 0.890.0
%define cpan_version 0.89
#Upstream: SUSE-Public-Domain
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND CC0-1.0
Summary:        Module signature file manipulation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(IPC::Run)
Provides:       perl(Module::Signature) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gpg
Requires:       gpg
# MANUAL END

%description
*Module::Signature* adds cryptographic authentications to CPAN
distributions, via the special _SIGNATURE_ file.

If you are a module user, all you have to do is to remember to run
'cpansign -v' (or just 'cpansign') before issuing 'perl Makefile.PL' or
'perl Build.PL'; that will ensure the distribution has not been tampered
with.

Module authors can easily add the _SIGNATURE_ file to the distribution
tarball; see NOTES below for how to do it as part of 'make dist'.

If you _really_ want to sign a distribution manually, simply add
'SIGNATURE' to _MANIFEST_, then type 'cpansign -s' immediately before 'make
dist'. Be sure to delete the _SIGNATURE_ file afterwards.

Please also see NOTES about _MANIFEST.SKIP_ issues, especially if you are
using *Module::Build* or writing your own _MANIFEST.SKIP_.

Signatures made with Module::Signature prior to version 0.82 used the SHA1
algorithm by default. SHA1 is now considered broken, and therefore module
authors are strongly encouraged to regenerate their _SIGNATURE_ files.
Users verifying old SHA1 signature files will receive a warning.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ANDK2020.pub AUDREYT2018.pub AUTHORS Changes NIKLASHOLM2018.pub PAUSE2022.pub README TIMLEGGE2024.pub

%changelog
