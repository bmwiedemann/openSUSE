#
# spec file for package perl-Data-Structure-Util
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


Name:           perl-Data-Structure-Util
Version:        0.16
Release:        0
%define cpan_name Data-Structure-Util
Summary:        Change nature of data within a structure
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Structure-Util/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDYA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Pod)
%{perl_requires}

%description
'Data::Structure::Util' is a toolbox to manipulate the data inside a data
structure. It can process an entire tree and perform the operation
requested on each appropriate element.

For example: It can transform all strings within a data structure to utf8
or transform any utf8 string back to the default encoding. It can remove
the blessing on any reference. It can collect all the objects or detect if
there is a circular reference.

It is written in C for decent speed.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES README

%changelog
