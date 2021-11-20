#
# spec file for package perl-Types-Path-Tiny
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


Name:           perl-Types-Path-Tiny
Version:        0.006
Release:        0
%define cpan_name Types-Path-Tiny
Summary:        Path::Tiny types and coercions for Moose and Moo
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Types-Path-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Type::Library) >= 0.008
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::TypeTiny) >= 0.004
Requires:       perl(Path::Tiny)
Requires:       perl(Type::Library) >= 0.008
Requires:       perl(Type::Utils)
Requires:       perl(Types::Standard)
Requires:       perl(Types::TypeTiny) >= 0.004
%{perl_requires}

%description
This module provides Path::Tiny types for Moose, Moo, etc.

It handles two important types of coercion:

  * coercing objects with overloaded stringification

  * coercing to absolute paths

It also can check to ensure that files or directories exist.

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
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
