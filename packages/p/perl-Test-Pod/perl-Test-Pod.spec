#
# spec file for package perl-Test-Pod
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


%define cpan_name Test-Pod
Name:           perl-Test-Pod
Version:        1.520.0
Release:        0
# 1.52 -> normalize -> 1.520.0
%define cpan_version 1.52
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-2.0 OR GPL-2.0-only
Summary:        Check for POD errors in files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Pod::Simple) >= 3.05
Requires:       perl(Pod::Simple) >= 3.05
Provides:       perl(Test::Pod) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Check POD files for errors or warnings in a test file, using 'Pod::Simple'
to do the heavy lifting.

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
%doc Changes README

%changelog
