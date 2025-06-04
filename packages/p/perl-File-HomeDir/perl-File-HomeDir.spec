#
# spec file for package perl-File-HomeDir
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


%define cpan_name File-HomeDir
Name:           perl-File-HomeDir
Version:        1.6.0
Release:        0
# 1.006 -> normalize -> 1.6.0
%define cpan_version 1.006
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Find your home and other directories on any platform
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.01
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(File::Which) >= 0.50
BuildRequires:  perl(Test::More) >= 0.9
Requires:       perl(File::Path) >= 2.01
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(File::Which) >= 0.50
Provides:       perl(File::HomeDir) = %{version}
Provides:       perl(File::HomeDir::Darwin) = %{version}
Provides:       perl(File::HomeDir::Darwin::Carbon) = %{version}
Provides:       perl(File::HomeDir::Darwin::Cocoa) = %{version}
Provides:       perl(File::HomeDir::Driver) = %{version}
Provides:       perl(File::HomeDir::FreeDesktop) = %{version}
Provides:       perl(File::HomeDir::MacOS9) = %{version}
Provides:       perl(File::HomeDir::Test) = %{version}
Provides:       perl(File::HomeDir::Unix) = %{version}
Provides:       perl(File::HomeDir::Windows) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
*File::HomeDir* is a module for locating the directories that are "owned"
by a user (typically your user) and to solve the various issues that arise
trying to find them consistently across a wide variety of platforms.

The end result is a single API that can find your resources on any
platform, making it relatively trivial to create Perl software that works
elegantly and correctly no matter where you run it.

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
%doc Changes README.md
%license LICENSE

%changelog
