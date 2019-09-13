#
# spec file for package perl-Archive-Cpio
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


Name:           perl-Archive-Cpio
Version:        0.10
Release:        0
%define cpan_name Archive-Cpio
Summary:        Module for Manipulations of Cpio Archives
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Archive-Cpio/
Source0:        http://www.cpan.org/authors/id/P/PI/PIXEL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source2:        LICENSE
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Archive::Cpio provides a few functions to read and write cpio files.

%prep
%setup -q -n %{cpan_name}-%{version}
cp -a %{SOURCE2} .

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
%doc Changes
%license LICENSE

%changelog
