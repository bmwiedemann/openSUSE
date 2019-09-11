#
# spec file for package perl-Test-WriteVariants
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


Name:           perl-Test-WriteVariants
Version:        0.014
Release:        0
%define cpan_name Test-WriteVariants
Summary:        Dynamic generation of tests in nested combinations of contexts
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Tumbler) >= 0.002
BuildRequires:  perl(Module::Pluggable::Object) >= 4.9
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::Directory) >= 0.041
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Most)
Requires:       perl(Data::Tumbler) >= 0.002
Requires:       perl(Module::Pluggable::Object) >= 4.9
Requires:       perl(Module::Runtime)
Recommends:     perl(File::Find::Rule) >= 0.34
%{perl_requires}

%description
Test::WriteVariants is a utility to create variants of a common test.

Given the situation - like in DBI where some tests are the same for
DBI::SQL::Nano and it's drop-in replacement SQL::Statement. Or a
distribution duo having a Pure-Perl and an XS variant - and the same test
shall be used to ensure XS and PP version are really drop-in replacements
for each other.

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
%doc Changes GPL-1 GPL-2.0 README.md TODO
%license ARTISTIC-1.0 LICENSE

%changelog
