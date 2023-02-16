#
# spec file for package perl-Tk-Clock
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Tk-Clock
Name:           perl-Tk-Clock
Version:        0.44
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Clock widget with analog and digital display
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Tk) >= 402.000
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Widget)
Requires:       perl(Test::More) >= 0.9
Requires:       perl(Test::NoWarnings)
Requires:       perl(Tk) >= 402.000
Requires:       perl(Tk::Canvas)
Requires:       perl(Tk::Derived)
Requires:       perl(Tk::Widget)
Recommends:     perl(Encode) >= 3.19
Recommends:     perl(Tk) >= 804.036
%{perl_requires}

%description
This module implements a Canvas-based clock widget for perl-Tk with lots of
options to change the appearance.

Both analog and digital clocks are implemented.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's,/pro/bin/perl,/usr/bin/perl,' examples/*pl
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
