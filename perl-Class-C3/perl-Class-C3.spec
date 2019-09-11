#
# spec file for package perl-Class-C3
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


Name:           perl-Class-C3
Version:        0.34
Release:        0
%define cpan_name Class-C3
Summary:        Pragma to Use the C3 Method Resolution Order Algorithm
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-C3/
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::C3) >= 0.07
Requires:       perl(Algorithm::C3) >= 0.07
%{perl_requires}

%description
This is pragma to change Perl 5's standard method resolution order from
depth-first left-to-right (a.k.a - pre-order) to the more sophisticated C3
method resolution order.

*NOTE:* YOU SHOULD NOT USE THIS MODULE DIRECTLY - The feature provided is
integrated into perl version >= 5.9.5, and you should use MRO::Compat
instead, which will use the core implementation in newer perls, but
fallback to using this implementation on older perls.

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
%doc Changes README

%changelog
