#
# spec file for package perl-Class-XPath
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Class-XPath
Name:           perl-Class-XPath
Version:        1.400.0
Release:        0
# 1.4 -> normalize -> 1.400.0
%define cpan_version 1.4
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Adds xpath matching to object trees
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Class::XPath) = %{version}
Provides:       perl(Simple)
%undefine       __perllib_provides
%{perl_requires}

%description
This module adds XPath-style matching to your object trees. This means that
you can find nodes using an XPath-esque query with 'match()' from anywhere
in the tree. Also, the 'xpath()' method returns a unique path to a given
node which can be used as an identifier.

To use this module you must already have an OO implementation of a tree.
The tree must be a true tree - all nodes have a single parent and the tree
must have a single root node. Also, the order of children within a node
must be stable.

*NOTE:* This module is not yet a complete XPath implementation. Over time I
expect the subset of XPath supported to grow. See the SYNTAX documentation
for details on the current level of support.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
