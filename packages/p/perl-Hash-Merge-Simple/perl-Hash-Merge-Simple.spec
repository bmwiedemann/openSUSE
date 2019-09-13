#
# spec file for package perl-Hash-Merge-Simple
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Hash-Merge-Simple
Version:        0.051
Release:        0
%define cpan_name Hash-Merge-Simple
Summary:        Recursively merge two or more hashes, simply
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Hash-Merge-Simple/
#Source:         http://www.cpan.org/authors/id/R/RO/ROKR/Hash-Merge-Simple-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(Test::Most)
Requires:       perl(Clone)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
Hash::Merge::Simple will recursively merge two or more hashes and return
the result as a new hash reference. The merge function will descend and
merge hashes that exist under the same node in both the left and right
hash, but doesn't attempt to combine arrays, objects, scalars, or anything
else. The rightmost hash also takes precedence, replacing whatever was in
the left hash if a conflict occurs.

This code was pretty much taken straight from the Catalyst::Utils manpage,
and modified to handle more than 2 hashes at the same time.

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README

%changelog
