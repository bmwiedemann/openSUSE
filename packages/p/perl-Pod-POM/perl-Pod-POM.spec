#
# spec file for package perl-Pod-POM
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


Name:           perl-Pod-POM
Version:        2.01
Release:        0
%define cpan_name Pod-POM
Summary:        POD Object Model
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Pod-POM/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Slurper) >= 0.004
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
This module implements a parser to convert Pod documents into a simple
object model form known hereafter as the Pod Object Model. The object model
is generated as a hierarchical tree of nodes, each of which represents a
different element of the original document. The tree can be walked manually
and the nodes examined, printed or otherwise manipulated. In addition,
Pod::POM supports and provides view objects which can automatically
traverse the tree, or section thereof, and generate an output
representation in one form or another.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes examples LICENSE README.md TODO

%changelog
