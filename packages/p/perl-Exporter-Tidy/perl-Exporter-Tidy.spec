#
# spec file for package perl-Exporter-Tidy
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


%define cpan_name Exporter-Tidy
Name:           perl-Exporter-Tidy
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
#Upstream:  This software may be redistributed under the terms of the GPL, LGPL, modified BSD, or Artistic license, or any of the other OSI approved licenses listed at http://www.opensource.org/licenses/alphabetical. Distribution is allowed under all of these licenses, or any smaller subset of multiple or just one of these licenses. When using a packaged version, please refer to the package metadata to see under which license terms it was distributed. Alternatively, a distributor may choose to replace the LICENSE section of the documentation and/or include a LICENSE file to reflect the license(s) they chose to redistribute under.
License:        SUSE-Public-Domain
Summary:        Another way of exporting symbols
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Exporter::Tidy) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module serves as an easy, clean alternative to Exporter. Unlike
Exporter, it is not subclassed, but it simply exports a custom import()
into your namespace.

With Exporter::Tidy, you don't need to use any package global in your
module. Even the subs you export can be lexically scoped.

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
