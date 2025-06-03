#
# spec file for package perl-Fennec-Lite
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


%define cpan_name Fennec-Lite
Name:           perl-Fennec-Lite
Version:        0.4.0
Release:        0
# 0.004 -> normalize -> 0.4.0
%define cpan_version 0.004
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Minimalist Fennec, the commonly used bits
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.36
Provides:       perl(Fennec::Lite) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Fennec does a ton, but it may be hard to adopt it all at once. It also is a
large project, and has not yet been fully split into component projects.
Fennec::Lite takes a minimalist approach to do for Fennec what Mouse does
for Moose.

Fennec::Lite is a single module file with no non-core dependencies. It can
easily be used by any project, either directly, or by copying it into your
project. The file itself is less than 300 lines of code at the time of this
writing, that includes whitespace.

This module does not cover any of the more advanced features such as result
capturing or SPEC workflows. This module only covers test grouping and
group randomization. You can also use the FENNEC_ITEM variable with a group
name or line number to run a specific test group only. Test::Builder is
used under the hood for TAP output.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc README

%changelog
