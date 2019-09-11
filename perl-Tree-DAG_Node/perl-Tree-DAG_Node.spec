#
# spec file for package perl-Tree-DAG_Node
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


%define cpan_name Tree-DAG_Node
Name:           perl-Tree-DAG_Node
Version:        1.31
Release:        0
Summary:        An N-ary tree
License:        Artistic-1.0 OR GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Tree-DAG_Node/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Slurp::Tiny) >= 0.003
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(File::Slurp::Tiny) >= 0.003
BuildArch:      noarch
%{perl_requires}

%description
This class encapsulates/makes/manipulates objects that represent nodes in a
tree structure. The tree structure is not an object itself, but is emergent
from the linkages you create between nodes. This class provides the methods
for making linkages that can be used to build up a tree, while preventing
you from ever making any kinds of linkages which are not allowed in a tree
(such as having a node be its own mother or ancestor, or having a node have
two mothers).

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
