#
# spec file for package perl-CursesWidgets (Version 1.997)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-CursesWidgets
%define cpan_name CursesWidgets
Summary:        CursesWidgets Perl module
Version:        1.997
Release:        148
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CursesWidgets/
#Source:         http://www.cpan.org/modules/by-module/CursesWidgets/CursesWidgets-%{version}.tar.bz2
Source:         %{cpan_name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl perl-Curses
BuildRequires:  perl-macros

%description
NOTE:  This is **NOT** backwards compatible with the pre-1.99 versions.
       This is entirely OO-based, hence any older scripts relying on the
       old versions will need to be rewritten.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
#%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,-)
%doc CHANGELOG CREDITS LICENSE README

%changelog
