#
# spec file for package perl-DateTime-Format-MySQL
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DateTime-Format-MySQL
Version:        0.06
Release:        0
%define cpan_name DateTime-Format-MySQL
Summary:        Parse and format MySQL dates and times
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DateTime-Format-MySQL/
Source0:        http://www.cpan.org/authors/id/X/XM/XMIKEW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder) >= 0.6
BuildRequires:  perl(Module::Build) >= 0.420000
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Builder) >= 0.6
%{perl_requires}

%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in
order to create DateTime objects, and it can take a DateTime object and
produce a string representing it in the MySQL format.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
