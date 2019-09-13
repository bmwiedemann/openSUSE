#
# spec file for package perl-Crypt-OpenSSL-Guess
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


Name:           perl-Crypt-OpenSSL-Guess
Version:        0.11
Release:        0
%define cpan_name Crypt-OpenSSL-Guess
Summary:        Guess OpenSSL include path
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKIYM/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes minil.toml README.md
%license LICENSE

%changelog
