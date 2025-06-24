#
# spec file for package perl-App-Rad-Plugin-MoreHelp
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name App-Rad-Plugin-MoreHelp
Name:           perl-App-Rad-Plugin-MoreHelp
Version:        0.0.100
Release:        0
# 0.0001 -> normalize -> 0.0.100
%define cpan_version 0.0001
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        App::Rad plugin for providing extra help info
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Rad)
Requires:       perl(App::Rad)
Provides:       perl(App::Rad::Plugin::MoreHelp) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is an App::Rad plugin for providing extra help info. It provides a
'more_help' method which can be used to provide extra info that will be
appended to to bottom of the help message.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README README.md
%license LICENSE

%changelog
