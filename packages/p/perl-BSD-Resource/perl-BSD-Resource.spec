#
# spec file for package perl-BSD-Resource
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


%define cpan_name BSD-Resource
Name:           perl-BSD-Resource
Version:        1.291.100
Release:        0
# 1.2911 -> normalize -> 1.291.100
%define cpan_version 1.2911
#Upstream:  This module free software; you can redistribute it and/or modify it under the terms of the Artistic License 2.0 or GNU Lesser General Public License 2.0. For more details, see the full text of the licenses at <http://www.perlfoundation.org/artistic_license_2_0>, and <http://www.gnu.org/licenses/gpl-2.0.html>.
License:        Artistic-2.0 OR LGPL-2.0-only
Summary:        BSD process resource limit and priority functions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(BSD::Resource) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
BSD process resource limit and priority functions

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README
%license LICENSE

%changelog
