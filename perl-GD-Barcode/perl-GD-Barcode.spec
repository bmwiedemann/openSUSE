#
# spec file for package perl-GD-Barcode
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-GD-Barcode
Version:        1.15
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name GD-Barcode
Summary:        Create barcode image with GD
Url:            http://search.cpan.org/dist/GD-Barcode/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/K/KW/KWITKNR/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(GD)
%{perl_requires}

%description
GD::Barcode is a subclass of GD and allows you to create barcode image with
GD. This module based on "Generate Barcode Ver 1.02 By Shisei Hanai
97/08/22".

From 1.14, you can use this module even if no GD (except plot method).

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
