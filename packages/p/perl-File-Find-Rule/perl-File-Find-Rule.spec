#
# spec file for package perl-File-Find-Rule
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


%define cpan_name File-Find-Rule
Name:           perl-File-Find-Rule
Version:        0.350.0
Release:        0
# 0.35 -> normalize -> 0.350.0
%define cpan_version 0.35
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Alternative interface to File::Find
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Text::Glob) >= 0.70
Requires:       perl(Number::Compare)
Requires:       perl(Text::Glob) >= 0.70
Provides:       perl(File::Find::Rule) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
File::Find::Rule is a friendlier interface to File::Find. It allows you to
build rules which specify the desired files and directories.

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
%doc Changes findrule

%changelog
