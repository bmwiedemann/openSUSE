#
# spec file for package perl-Sort-Key
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Sort-Key
Version:        1.33
Release:        0
%define cpan_name Sort-Key
Summary:        the fastest way to sort anything in Perl
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sort-Key/
Source:         http://www.cpan.org/authors/id/S/SA/SALVA/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Sort::Key provides a set of functions to sort lists of values by some
calculated key value.

It is faster (usually *much faster*) and uses less memory than other
alternatives implemented around perl sort function (ST, GRT, etc.).

Multi-key sorting functionality is also provided via the companion modules
the Sort::Key::Multi manpage, the Sort::Key::Maker manpage and the
Sort::Key::Register manpage.

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

%changelog
