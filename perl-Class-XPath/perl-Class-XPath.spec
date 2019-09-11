#
# spec file for package perl-Class-XPath
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Class-XPath
%define cpan_name Class-XPath
Summary:        Adds xpath matching to object trees
Version:        1.4
Release:        144
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-XPath/
#Source:         http://www.cpan.org/authors/id/S/SA/SAMTREGAR/Class-XPath-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(HTML::TreeBuilder)
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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README

%changelog
