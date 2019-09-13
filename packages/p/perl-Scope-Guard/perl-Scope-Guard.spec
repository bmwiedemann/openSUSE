#
# spec file for package perl-Scope-Guard
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


Name:           perl-Scope-Guard
Version:        0.21
Release:        0
%define cpan_name Scope-Guard
Summary:        Lexically-Scoped Resource Management
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Scope-Guard/
Source0:        http://www.cpan.org/authors/id/C/CH/CHOCOLATE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides a convenient way to perform cleanup or other forms of
resource management at the end of a scope. It is particularly useful when
dealing with exceptions: the 'Scope::Guard' constructor takes a reference
to a subroutine that is guaranteed to be called even if the thread of
execution is aborted prematurely. This effectively allows lexically-scoped
"promises" to be made that are automatically honoured by perl's garbage
collector.

For more information, see: the http://www.drdobbs.com/cpp/184403758 manpage

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
