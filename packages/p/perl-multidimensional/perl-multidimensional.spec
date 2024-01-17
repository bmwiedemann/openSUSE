#
# spec file for package perl-multidimensional
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


Name:           perl-multidimensional
Version:        0.014
Release:        0
%define cpan_name multidimensional
Summary:        Disables Multidimensional Array Emulation
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/multidimensional/
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.19
BuildRequires:  perl(CPAN::Meta) >= 2.112580
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(B::Hooks::OP::Check) >= 0.19
%{perl_requires}

%description
Perl's multidimensional array emulation stems from the days before the
language had references, but these days it mostly serves to bite you when
you typo a hash slice by using the '$' sigil instead of '@'.

This module lexically makes using multidimensional array emulation a fatal
error at compile time.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
%license LICENSE

%changelog
