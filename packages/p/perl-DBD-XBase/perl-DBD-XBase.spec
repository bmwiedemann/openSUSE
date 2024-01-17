#
# spec file for package perl-DBD-XBase
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DBD-XBase
Version:        1.08
Release:        0
#Upstream: CHECK(GPL-1.0+ or Artistic-1.0)
%define cpan_name DBD-XBase
Summary:        Reads and writes XBase (dbf) files, includes DBI support
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBD-XBase/
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JANPAZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
DBI compliant driver for module XBase. Please refer to DBI(3) documentation
for how to actually use the module. In the *connect* call, specify the
directory containing the dbf files (and other, memo, etc.) as the third
part of the connect string. It defaults to the current directory.

Note that with dbf, there is no database server that the driver would talk
to. This DBD::XBase calls methods from XBase.pm module to read and write
the files on the disk directly, so any limitations and features of XBase.pm
apply to DBD::XBase as well. DBD::XBase basically adds SQL, DBI compliant
interface to XBase.pm.

The DBD::XBase doesn't make use of index files at the moment. If you really
need indexed access, check XBase(3) for notes about support for variour
index types.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes driver_characteristics new-XBase README ToDo

%changelog
