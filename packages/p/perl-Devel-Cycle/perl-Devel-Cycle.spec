#
# spec file for package perl-Devel-Cycle
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


%define cpan_name Devel-Cycle
Name:           perl-Devel-Cycle
Version:        1.120.0
Release:        0
# 1.12 -> normalize -> 1.120.0
%define cpan_version 1.12
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Find memory cycles in objects
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Devel-Cycle-pm.patch
Patch1:         Devel-Cycle-t.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Devel::Cycle) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is a simple developer's tool for finding circular references in
objects and other types of references. Because of Perl's reference-count
based memory management, circular references will cause memory leaks.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -N

%patch -P0
%patch -P1

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
