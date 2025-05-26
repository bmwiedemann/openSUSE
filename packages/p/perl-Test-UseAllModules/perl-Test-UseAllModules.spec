#
# spec file for package perl-Test-UseAllModules
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


%define cpan_name Test-UseAllModules
Name:           perl-Test-UseAllModules
Version:        0.170.0
Release:        0
# 0.17 -> normalize -> 0.170.0
%define cpan_version 0.17
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Do use_ok() for all the MANIFESTed modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Test::UseAllModules) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
I'm sick of writing 00_load.t (or something like that) that'll do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distro. This module reads MANIFEST to find modules to
be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
