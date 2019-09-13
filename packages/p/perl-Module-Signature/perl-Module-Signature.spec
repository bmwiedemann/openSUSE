#
# spec file for package perl-Module-Signature
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Module-Signature
Version:        0.83
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name Module-Signature
Summary:        Module signature file manipulation
License:        CC0-1.0 AND (GPL-1.0-or-later OR Artistic-1.0)
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Signature/
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Run)
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

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
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
%doc ANDK2018.pub AUDREYT2018.pub AUTHORS Changes NIKLASHOLM2018.pub PAUSE2019.pub README

%changelog
