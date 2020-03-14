#
# spec file for package perl-Set-IntSpan
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


Name:           perl-Set-IntSpan
Version:        1.19
Release:        0
%define cpan_name Set-IntSpan
Summary:        Manages sets of integers
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Set-IntSpan/
Source:         http://www.cpan.org/authors/id/S/SW/SWMCD/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
%{perl_requires}

%description
'Set::IntSpan' manages sets of integers. It is optimized for sets that have
long runs of consecutive integers. These arise, for example, in .newsrc
files, which maintain lists of articles:

  alt.foo: 1-21,28,31
  alt.bar: 1-14192,14194,14196-14221

A run of consecutive integers is sometimes called a _span_.

Sets are stored internally in a run-length coded form. This provides for
both compact storage and efficient computation. In particular, set
operations can be performed directly on the encoded representation.

'Set::IntSpan' is designed to manage finite sets. However, it can also
represent some simple infinite sets, such as { x | x>n }. This allows
operations involving complements to be carried out consistently, without
having to worry about the actual value of INT_MAX on your machine.

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
%defattr(-,root,root,755)
%doc Changes README

%changelog
