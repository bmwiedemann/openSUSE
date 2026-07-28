#
# spec file for package perl-WWW-PAUSE-CleanUpHomeDir
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name WWW-PAUSE-CleanUpHomeDir
Name:           perl-WWW-PAUSE-CleanUpHomeDir
Version:        1.001003
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        The module to clean up old dists from your PAUSE home directory
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/%{cpan_name}-%{version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Devel::TakeHashArgs)
BuildRequires:  perl(HTML::TokeParser::Simple)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(URI)
BuildRequires:  perl(WWW::Mechanize)
Requires:       perl(Class::Accessor::Grouped)
Requires:       perl(Devel::TakeHashArgs)
Requires:       perl(HTML::TokeParser::Simple)
Requires:       perl(Sort::Versions)
Requires:       perl(URI)
Requires:       perl(WWW::Mechanize)
%{perl_requires}

%description
The module provides means to clean up your PAUSE home directory from old
distributions with ability to undelete files if you so prefer.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

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
%doc Changes examples README README.md
%license LICENSE

%changelog
