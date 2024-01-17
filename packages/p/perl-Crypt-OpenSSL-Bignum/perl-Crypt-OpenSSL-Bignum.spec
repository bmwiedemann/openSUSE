#
# spec file for package perl-Crypt-OpenSSL-Bignum
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Crypt-OpenSSL-Bignum
Version:        0.09
Release:        0
%define cpan_name Crypt-OpenSSL-Bignum
Summary:        OpenSSL's multiprecision integer arithmetic
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-OpenSSL-Bignum/
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMX/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL
BuildRequires:  openssl-devel

%description
Crypt::OpenSSL::Bignum provides access to OpenSSL multiprecision integer
arithmetic libraries. Presently, many though not all of the arithmetic
operations that OpenSSL provides are exposed to perl. In addition, this
module can be used to provide access to bignum values produced by other
OpenSSL modules, such as key parameters from Crypt::OpenSSL::RSA.

_NOTE_: Many of the methods in this package can croak, so use eval, or
Error.pm's try/catch mechanism to capture errors.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
