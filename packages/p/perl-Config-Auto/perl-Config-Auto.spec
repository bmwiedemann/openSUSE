#
# spec file for package perl-Config-Auto
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Config-Auto
Version:        0.44
Release:        0
%define cpan_name Config-Auto
Summary:        Magical config file parser
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-Auto/
Source:         http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(YAML) >= 0.67
Requires:       perl(Config::IniFiles)
Requires:       perl(IO::String)
Requires:       perl(YAML) >= 0.67
%{perl_requires}

%description
This module was written after having to write Yet Another Config File
Parser for some variety of colon-separated config. I decided "never again".

Config::Auto aims to be the most 'DWIM' config parser available, by
detecting configuration styles, include paths and even config filenames
automagically.

See the the HOW IT WORKS manpage section below on implementation details.

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
%doc Changes README

%changelog
