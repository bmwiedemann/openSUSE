#
# spec file for package perl-B-Utils
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


%define cpan_name B-Utils
Name:           perl-B-Utils
Version:        0.270.0
Release:        0
# 0.27 -> normalize -> 0.270.0
%define cpan_version 0.27
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Helper functions for op tree manipulation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        perl-B-Utils-rpmlintrc
Source2:        cpanspec.yml
Patch0:         parent-impl.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Depends) >= 0.301
BuildRequires:  perl(Task::Weaken)
Requires:       perl(Task::Weaken)
Provides:       perl(B::Utils) = %{version}
Provides:       perl(B::Utils::OP) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Helper functions for op tree manipulation

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license LICENSE

%changelog
