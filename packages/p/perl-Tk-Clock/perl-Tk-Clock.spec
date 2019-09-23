#
# spec file for package perl-Tk-Clock
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


Name:           perl-Tk-Clock
Version:        0.40
Release:        0
%define cpan_name Tk-Clock
Summary:        Clock widget with analog and digital display
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Tk-Clock/
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Tk) >= 402.000
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Widget)
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::NoWarnings)
Requires:       perl(Tk) >= 402.000
Requires:       perl(Tk::Canvas)
Requires:       perl(Tk::Derived)
Requires:       perl(Tk::Widget)
Recommends:     perl(Encode) >= 2.84
Recommends:     perl(Test::More) >= 1.302015
Recommends:     perl(Tk) >= 804.033
%{perl_requires}

%description
This module implements a Canvas-based clock widget for perl-Tk with lots of
options to change the appearance.

Both analog and digital clocks are implemented.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's,/pro/bin/perl,/usr/bin/perl,' examples/*pl
# MANUAL END

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
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
