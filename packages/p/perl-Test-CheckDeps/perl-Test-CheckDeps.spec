#
# spec file for package perl-Test-CheckDeps
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


Name:           perl-Test-CheckDeps
Version:        0.010
Release:        0
%define cpan_name Test-CheckDeps
Summary:        Check for presence of dependencies
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-CheckDeps/
Source:         http://www.cpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta) >= 2.120920
BuildRequires:  perl(CPAN::Meta::Check) >= 0.007
BuildRequires:  perl(Test::More) >= 0.88
#BuildRequires: perl(Test::CheckDeps)
Requires:       perl(CPAN::Meta) >= 2.120920
Requires:       perl(CPAN::Meta::Check) >= 0.007
%{perl_requires}

%description
This module adds a test that assures all dependencies have been installed
properly. If requested, it can bail out all testing on error.

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
