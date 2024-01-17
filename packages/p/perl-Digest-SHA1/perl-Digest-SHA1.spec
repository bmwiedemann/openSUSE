#
# spec file for package perl-Digest-SHA1
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


Name:           perl-Digest-SHA1
%define cpan_name Digest-SHA1
Summary:        Perl Interface to the SHA-1 Algorithm
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Version:        2.13
Release:        0
Url:            http://search.cpan.org/perldoc?Digest::SHA1
Source:         http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description

 %{cpan_name} module for perl
  The Digest::SHA1 module allows the use of the NIST SHA-1 message digest
  algorithm from within Perl programs. The algorithm takes a message of
  arbitrary length as input and produces a 160-bit fingerprint or message
  digest of the input as output.
  Authors:
		Peter C. Gutmann,
		Uwe Hollerbach <uh@alumni.caltech.edu>,
		Gisle Aas <gisle@aas.no>

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes README fip180-1.gif fip180-1.html

%changelog
