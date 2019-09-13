#
# spec file for package perl-Cache-LRU
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Cache-LRU
Version:        0.04
Release:        0
%define cpan_name Cache-LRU
Summary:        Simple, Fast Implementation of Lru Cache in Pure Perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Cache-LRU/
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl526.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
%{perl_requires}

%description
Cache::LRU is a simple, fast implementation of an in-memory LRU cache in
pure perl.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

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
%doc Changes README

%changelog
