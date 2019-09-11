#
# spec file for package perl-Data-Printer
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


Name:           perl-Data-Printer
Version:        0.40
Release:        0
%define cpan_name Data-Printer
Summary:        Colored Pretty-Print of Perl Data Structures and Objects
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Printer/
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(File::HomeDir) >= 0.91
BuildRequires:  perl(Package::Stash) >= 0.3
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Term::ANSIColor) >= 3
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.77
Requires:       perl(Clone::PP)
Requires:       perl(File::HomeDir) >= 0.91
Requires:       perl(Package::Stash) >= 0.3
Requires:       perl(Sort::Naturally)
Requires:       perl(Term::ANSIColor) >= 3
Requires:       perl(Test::More) >= 0.88
Requires:       perl(version) >= 0.77
%{perl_requires}

%description
colored pretty-print of Perl data structures and objects

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
%doc Changes examples README.md

%changelog
