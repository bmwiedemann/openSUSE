#
# spec file for package perl-Crypt-OpenSSL-Guess
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


%define cpan_name Crypt-OpenSSL-Guess
Name:           perl-Crypt-OpenSSL-Guess
Version:        0.13
Release:        0
Summary:        Guess OpenSSL include path
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKIYM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 0.98
%{perl_requires}

%description
Crypt::OpenSSL::Guess provides helpers to guess OpenSSL include path on any
platforms.

Often MacOS's homebrew OpenSSL cause a problem on installation due to
include path is not added. Some CPAN module provides to modify include path
with configure-args, but Carton or Module::CPANfile is not supported to
pass configure-args to each modules. Crypt::OpenSSL::* modules should use
it on your Makefile.PL.

This module resolves the include path by Net::SSLeay's workaround. Original
code is taken from 'inc/Module/Install/PRIVATE/Net/SSLeay.pm' by
Net::SSLeay.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes minil.toml README.md
%license LICENSE

%changelog
