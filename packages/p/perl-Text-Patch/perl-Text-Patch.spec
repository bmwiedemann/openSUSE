#
# spec file for package perl-Text-Patch
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


%define cpan_name Text-Patch
Name:           perl-Text-Patch
Version:        1.800.0
Release:        0
# 1.8 -> normalize -> 1.800.0
%define cpan_version 1.8
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        GPL-2.0-or-later
Summary:        Patches text with given patch
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CADE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Text::Diff)
Requires:       perl(Text::Diff)
Provides:       perl(Text::Patch) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Text::Patch combines source text with given diff (difference) data. Diff
data is produced by Text::Diff module or by the standard diff utility (man
diff, see -u option).

* patch( $source, $diff, options... )

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
%doc ChangeLog README
%license COPYING

%changelog
