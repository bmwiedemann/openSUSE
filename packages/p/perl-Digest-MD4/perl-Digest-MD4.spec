#
# spec file for package perl-Digest-MD4
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Digest-MD4
Version:        1.9
Release:        0
%define cpan_name Digest-MD4
Summary:        Perl interface to the MD4 Algorithm
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Digest-MD4/
Source:         http://www.cpan.org/authors/id/M/MI/MIKEM/DigestMD4/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Digest::MD4)
#BuildRequires: perl(Digest::Perl::MD4)
%{perl_requires}

%description
The 'Digest::MD4' module allows you to use the RSA Data Security Inc. MD4
Message Digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.

The 'Digest::MD4' module provides a procedural interface for simple use, as
well as an object oriented interface that can handle messages of arbitrary
length and which can read files directly.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README rfc1320.txt

%changelog
