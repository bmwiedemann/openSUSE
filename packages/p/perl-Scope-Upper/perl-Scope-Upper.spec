#
# spec file for package perl-Scope-Upper
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Scope-Upper
Version:        0.32
Release:        0
%define cpan_name Scope-Upper
Summary:        Act on upper scopes
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module lets you defer actions _at run-time_ that will take place when
the control flow returns into an upper scope. Currently, you can:

  * hook an upper scope end with reap ;

  * localize variables, array/hash values or deletions of elements in higher
contexts with respectively localize, localize_elem and localize_delete ;

  * return values immediately to an upper level with unwind, yield and leave ;

  * gather information about an upper context with want_at and context_info ;

  * execute a subroutine in the setting of an upper subroutine stack frame with
uplevel ;

  * uniquely identify contexts with uid and validate_uid.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README samples

%changelog
