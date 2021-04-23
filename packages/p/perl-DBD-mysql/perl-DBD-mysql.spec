#
# spec file for package perl-DBD-mysql
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DBD-mysql
Version:        4.050
Release:        0
%define cpan_name DBD-mysql
Summary:        MySQL driver for the Perl5 Database Interface (DBI)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DV/DVEEDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.609
BuildRequires:  perl(Devel::CheckLib) >= 1.09
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Simple) >= 0.90
Requires:       perl(DBI) >= 1.609
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libmariadb-devel
BuildRequires:  zlib-devel
# MANUAL END

%description
*DBD::mysql* is the Perl5 Database Interface driver for the MySQL database.
In other words: DBD::mysql is an interface between the Perl programming
language and the MySQL programming API that comes with the MySQL relational
database management system. Most functions provided by this programming API
are supported. Some rarely used functions are missing, mainly because
no-one ever requested them. :-)

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes Makefile.PL.embedded myld README.md
%license LICENSE

%changelog
