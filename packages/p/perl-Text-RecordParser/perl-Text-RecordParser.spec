#
# spec file for package perl-Text-RecordParser
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


Name:           perl-Text-RecordParser
Version:        1.6.5
Release:        0
#Upstream: GPL-1.0+
%define cpan_name Text-RecordParser
Summary:        Read Record-Oriented Files
License:        GPL-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-RecordParser/
Source0:        http://www.cpan.org/authors/id/K/KC/KCLARK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Text::Autoformat)
Requires:       perl(Class::Accessor)
Requires:       perl(IO::Scalar)
Requires:       perl(List::MoreUtils)
Requires:       perl(Readonly)
Requires:       perl(Text::Autoformat)
Recommends:     perl(GraphViz)
Recommends:     perl(Text::TabularDisplay) >= 1.22
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  cairo
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gnome
BuildRequires:  pango
BuildRequires:  perl(GraphViz)
# MANUAL END

%description
This module is for reading record-oriented data in a delimited text file.
The most common example have records separated by newlines and fields
separated by commas or tabs, but this module aims to provide a consistent
interface for handling sequential records in a file however they may be
delimited. Typically this data lists the fields in the first line of the
file, in which case you should call 'bind_header' to bind the field name
(or not, and it will be called implicitly). If the first line contains
data, you can still bind your own field names via 'bind_fields'. Either
way, you can then use many methods to get at the data as arrays or hashes.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
PERL5LIB=. %{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README TODO

%changelog
