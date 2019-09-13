#
# spec file for package perl-DBD-ODBC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-DBD-ODBC
Version:        1.60
Release:        0
%define cpan_name DBD-ODBC
Summary:        ODBC Driver for DBI
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MJ/MJEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-DBD-ODBC-1.29-Makefile.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.21
BuildRequires:  perl(Test::Simple) >= 0.90
Requires:       perl(DBI) >= 1.609
Requires:       perl(Test::Simple) >= 0.90
Recommends:     perl(Test::Version) >= 1.002001
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  unixODBC-devel
# MANUAL END

%description
ODBC Driver for DBI

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p0
# MANUAL BEGIN
for file in README.af README.unicode; do
  perl -p -i -e "s|\r\n|\n|" "$file"
done
pushd examples
#rpmlint: wrong-file-end-of-line-encoding
find -type f -exec perl -p -i -e "s|\r\n|\n|" {} \;
#rpmlint: wrong-script-interpreter
for ex in *; do
  sed -i -e 's,^#!*perl\(.*\),#!/usr/bin/perl\1,' "$ex"
  sed -i -e 's,perl.exe -w,perl -w,' "$ex"
done
popd
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples FAQ if_you_are_taking_over_this_code.txt README README.adabas README.af README.hpux README.informix README.osx README.RH9 README.sqlserver README.unicode README.windows test_results.txt TO_DO

%changelog
