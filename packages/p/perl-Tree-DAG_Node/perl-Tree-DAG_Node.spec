#
# spec file for package perl-Tree-DAG_Node
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


%define cpan_name Tree-DAG_Node
Name:           perl-Tree-DAG_Node
Version:        1.330.0
Release:        0
# 1.33 -> normalize -> 1.330.0
%define cpan_version 1.33
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        An N-ary tree
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{cpan_version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.7
BuildRequires:  perl(File::Slurper) >= 0.14.0
BuildRequires:  perl(File::Spec) >= 3.4
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(ExtUtils::MakeMaker) >= 7.7
Requires:       perl(File::Slurper) >= 0.14.0
Provides:       perl(Tree::DAG_Node) = %{version}
%undefine       __perllib_provides
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
%doc Changes README SECURITY.md
%license LICENSE

%changelog
