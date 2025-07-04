#
# spec file for package perl-B-Debug
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


%define cpan_name B-Debug
Name:           perl-B-Debug
Version:        1.260.0
Release:        0
# 1.26 -> normalize -> 1.260.0
%define cpan_version 1.26
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Print debug info about ops
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(deprecate) >= 0.03
Requires:       perl(deprecate) >= 0.03
Provides:       perl(B::Debug) = %{version}
%undefine       __perllib_provides
Recommends:     perl(B::Flags) >= 0.40
%{perl_requires}

%description
See _ext/B/README_ and the newer B::Concise.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%license Artistic Copying

%changelog
