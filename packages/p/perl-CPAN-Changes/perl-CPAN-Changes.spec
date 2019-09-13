#
# spec file for package perl-CPAN-Changes
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


Name:           perl-CPAN-Changes
Version:        0.400002
Release:        0
%define cpan_name CPAN-Changes
Summary:        Read and write Changes files
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CPAN-Changes/
Source0:        http://www.cpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
#BuildRequires:  perl(version) >= 0.9906
#Requires:       perl(version) >= 0.9906
%{perl_requires}

%description
It is standard practice to include a Changes file in your distribution. The
purpose the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (the CPAN::Changes::Spec manpage) to
encourage module authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

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
