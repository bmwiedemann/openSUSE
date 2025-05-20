#
# spec file for package perl-Devel-GlobalDestruction
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


%define cpan_name Devel-GlobalDestruction
Name:           perl-Devel-GlobalDestruction
Version:        0.140.0
Release:        0
# 0.14 -> normalize -> 0.140.0
%define cpan_version 0.14
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provides function returning the equivalent of ${^GLOBAL_PHASE} eq 'DESTR[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001011
Requires:       perl(Sub::Exporter::Progressive) >= 0.001011
Provides:       perl(Devel::GlobalDestruction) = %{version}
Provides:       perl(ExtUtils::HasCompiler) = 0.16.0
%undefine       __perllib_provides
%{perl_requires}

%description
Perl's global destruction is a little tricky to deal with WRT finalizers
because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happening you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

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
