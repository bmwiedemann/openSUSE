#
# spec file for package perl-Test-Script
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Test-Script
Name:           perl-Test-Script
Version:        1.310.0
Release:        0
# 1.31 -> normalize -> 1.310.0
%define cpan_version 1.31
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Basic cross-platform tests for scripts
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Probe::Perl) >= 0.10
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::V0) >= 0.000121
Requires:       perl(Capture::Tiny)
Requires:       perl(Probe::Perl) >= 0.10
Requires:       perl(Test2::API) >= 1.302015
Provides:       perl(Test::Script) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The intent of this module is to provide a series of basic tests for 80% of
the testing you will need to do for scripts in the _script_ (or _bin_ as is
also commonly used) paths of your Perl distribution.

It also provides similar functions for testing programs that are not Perl
scripts.

Further, it aims to provide this functionality with perfect
platform-compatibility, and in a way that is as unobtrusive as possible.

That is, if the program works on a platform, then *Test::Script* should
always work on that platform as well. Anything less than 100% is considered
unacceptable.

In doing so, it is hoped that *Test::Script* can become a module that you
can safely make a dependency of all your modules, without risking that your
module won't install on some platform because of the dependency.

Where a clash exists between wanting more functionality and maintaining
platform safety, this module will err on the side of platform safety.

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
%license LICENSE

%changelog
