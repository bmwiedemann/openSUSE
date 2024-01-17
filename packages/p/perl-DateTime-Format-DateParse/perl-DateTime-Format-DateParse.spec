#
# spec file for package perl-DateTime-Format-DateParse
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-DateTime-Format-DateParse
%define cpan_name DateTime-Format-DateParse
Summary:        Parses Date::Parse compatible formats
License:        GPL-2.0 or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        0.05
Release:        0
Url:            http://search.cpan.org/dist/DateTime-Format-DateParse
Source0:        %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Parse) >= 2.27
BuildRequires:  perl(DateTime) >= 0.29
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(DateTime::TimeZone) >= 0.27
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Time::Zone) >= 2.22
Requires:       perl(DateTime) >= 0.29
Requires:       perl(DateTime::Locale)
Requires:       perl(DateTime::TimeZone) >= 0.27
Requires:       perl(Date::Parse) >= 2.27
Requires:       perl(Time::Zone) >= 2.22

%description
This module is a compatibility wrapper around Date::Parse.

  Author:	Joshua Hoblitt (JHOBLITT) <jhoblitt@cpan.org>


%prep
%setup -q -n %{cpan_name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Build.PL --prefix $RPM_BUILD_ROOT/usr --installdirs vendor
./Build

%check
./Build test

%install
./Build install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes LICENSE README

%changelog
