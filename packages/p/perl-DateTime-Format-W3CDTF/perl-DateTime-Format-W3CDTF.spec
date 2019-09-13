#
# spec file for package perl-DateTime-Format-W3CDTF
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


Name:           perl-DateTime-Format-W3CDTF
Version:        0.07
Release:        0
%define cpan_name DateTime-Format-W3CDTF
Summary:        Parse and format W3CDTF datetime strings
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DateTime-Format-W3CDTF/
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime)
Requires:       perl(DateTime)
%{perl_requires}

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

It can be used to parse these formats in order to create the appropriate
objects.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes examples README
%license LICENSE

%changelog
