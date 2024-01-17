#
# spec file for package perl-Text-TabularDisplay
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Text-TabularDisplay
Version:        1.38
Release:        0
%define cpan_name Text-TabularDisplay
Summary:        Display text in formatted table output
License:        GPL-2.0
Group:          Development/Libraries/Perl
# MANUAL License
Url:            http://search.cpan.org/dist/Text-TabularDisplay/
Source:         http://www.cpan.org/authors/id/D/DA/DARREN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Text::TabularDisplay simplifies displaying textual data in a table. The
output is identical to the columnar display of query results in the mysql
text monitor. For example, this data:

    1, "Tom Jones", "(666) 555-1212"
    2, "Barnaby Jones", "(666) 555-1213"
    3, "Bridget Jones", "(666) 555-1214"

Used like so:

    my $t = Text::TabularDisplay->new(qw(id name phone));
    $t->add(1, "Tom Jones", "(666) 555-1212");
    $t->add(2, "Barnaby Jones", "(666) 555-1213");
    $t->add(3, "Bridget Jones", "(666) 555-1214");
    print $t->render;

Produces:

    +----+---------------+----------------+
    | id | name          | phone          |
    +----+---------------+----------------+
    | 1  | Tom Jones     | (666) 555-1212 |
    | 2  | Barnaby Jones | (666) 555-1213 |
    | 3  | Bridget Jones | (666) 555-1214 |
    +----+---------------+----------------+

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
%doc COPYING examples README

%changelog
