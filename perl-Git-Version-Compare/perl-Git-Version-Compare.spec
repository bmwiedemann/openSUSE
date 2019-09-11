#
# spec file for package perl-Git-Version-Compare
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Git-Version-Compare
Version:        1.004
Release:        0
%define cpan_name Git-Version-Compare
Summary:        Functions to compare Git versions
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Git-Version-Compare/
Source0:        http://www.cpan.org/authors/id/B/BO/BOOK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::NoWarnings)
%{perl_requires}

%description
Git::Version::Compare contains a selection of subroutines that make dealing
with Git-related things (like versions) a little bit easier.

The strings to compare can be version numbers, tags from 'git.git' or the
output of 'git version' or 'git describe'.

These routines collect the knowledge about Git versions that was
accumulated while developing Git::Repository.

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
%doc Changes LICENSE README

%changelog
