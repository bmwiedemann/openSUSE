#
# spec file for package perl-Graph
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Graph
Name:           perl-Graph
Version:        0.9729
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Graph data structures and algorithms
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Heap) >= 0.80
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Set::Object) >= 1.40
BuildRequires:  perl(Test::More) >= 0.82
Requires:       perl(Heap) >= 0.80
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Set::Object) >= 1.40
%{perl_requires}

%description
graph data structures and algorithms

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes DESIGN README RELEASE TODO util

%changelog
