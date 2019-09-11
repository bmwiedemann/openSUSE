#
# spec file for package perl-Crypt-RC4
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Pascal Bleser
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



Name:           perl-Crypt-RC4
Version:        2.02
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Summary:        Perl implementation of the RC4 encryption algorithm
Url:            http://search.cpan.org/dist/Crypt-RC4/
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/S/SI/SIFUKURT/Crypt-RC4-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
A simple implementation of the RC4 algorithm, developed by RSA Security, Inc.
Here is the description from RSA's website:

RC4 is a stream cipher designed by Rivest for RSA Data Security (now RSA
Security). It is a variable key-size stream cipher with byte-oriented
operations. The algorithm is based on the use of a random permutation. Analysis
shows that the period of the cipher is overwhelmingly likely to be greater than
10100. Eight to sixteen machine operations are required per output byte, and
the cipher can be expected to run very quickly in software. Independent
analysts have scrutinized the algorithm and it is considered secure.

%prep
%setup -q -n "Crypt-RC4-%{version}"
sed -i '/^auto_install/d' Makefile.PL

%build
perl Makefile.PL PREFIX="%{_prefix}"
make %{?jobs:-j%{jobs}}

%install
%perl_make_install
%perl_process_packlist

%check
make test

%clean
%{?buildroot:rm -rf %{buildroot}}

%files
%defattr(-,root,root)
%doc Changes
%dir %{perl_vendorlib}/Crypt
%{perl_vendorlib}/Crypt/RC4.pm
%dir %{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/auto/Crypt/RC4
%doc %{perl_man3dir}/Crypt::RC4.%{perl_man3ext}%{ext_man}

%changelog
