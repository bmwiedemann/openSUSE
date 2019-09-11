#
# spec file for package perl-Sub-Delete
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


Name:           perl-Sub-Delete
Version:        1.00002
Release:        0
#Upstream:  This program is free software; you may redistribute or modify it (or both) under the same terms as perl.
%define cpan_name Sub-Delete
Summary:        Perl module enabling one to delete subroutines
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPROUT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides one function, 'delete_sub', that deletes the
subroutine whose name is passed to it. (To load the module without
importing the function, write 'use Sub::Delete();'.)

This does more than simply undefine the subroutine in the manner of 'undef
&foo', which leaves a stub that can trigger AUTOLOAD (and, consequently,
won't work for deleting methods). The subroutine is completely obliterated
from the symbol table (though there may be references to it elsewhere,
including in compiled code).

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
