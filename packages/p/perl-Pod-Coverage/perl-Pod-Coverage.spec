#
# spec file for package perl-Pod-Coverage
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Pod-Coverage
Name:           perl-Pod-Coverage
Version:        0.230.0
Release:        0
# 0.23 -> normalize -> 0.230.0
%define cpan_version 0.23
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Checks if the documentation of a module is comprehensive
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Symdump) >= 2.10
BuildRequires:  perl(Pod::Find) >= 0.210
BuildRequires:  perl(Pod::Parser) >= 1.130
Requires:       perl(Devel::Symdump) >= 2.10
Requires:       perl(Pod::Find) >= 0.210
Requires:       perl(Pod::Parser) >= 1.130
Provides:       perl(Pod::Coverage) = %{version}
Provides:       perl(Pod::Coverage::CountParents)
Provides:       perl(Pod::Coverage::ExportOnly)
Provides:       perl(Pod::Coverage::Extractor)
Provides:       perl(Pod::Coverage::Overloader)
%undefine       __perllib_provides
%{perl_requires}

%description
Developers hate writing documentation. They'd hate it even more if their
computer tattled on them, but maybe they'll be even more thankful in the
long run. Even if not, _perlmodstyle_ tells you to, so you must obey.

This module provides a mechanism for determining if the pod for a given
module is comprehensive.

It expects to find either a '=head(n>1)' or an '=item' block documenting a
subroutine.

Consider: # an imaginary Foo.pm package Foo;

 =item foo

 The foo sub

 = cut

 sub foo {}
 sub bar {}

 1;
 __END__

In this example 'Foo::foo' is covered, but 'Foo::bar' is not, so the 'Foo'
package is only 50% (0.5) covered

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples

%changelog
