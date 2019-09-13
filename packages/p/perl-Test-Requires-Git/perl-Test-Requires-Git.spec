#
# spec file for package perl-Test-Requires-Git
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Test-Requires-Git
Version:        1.008
Release:        0
%define cpan_name Test-Requires-Git
Summary:        Check your test requirements against the available version of Git
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Requires-Git/
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Git::Version::Compare) >= 1.003
Requires:       perl(Git::Version::Compare) >= 1.003
%{perl_requires}

%description
Test::Requires::Git checks if the version of Git available for testing
meets the given requirements. If the checks fail, then all tests will be
_skipped_.

'use Test::Requires::Git' always calls 'test_requires_git' with the given
arguments. If you don't want 'test_requires_git' to be called at import
time, write this instead:

    use Test::Requires::Git -nocheck;

Passing the 'git' parameter (see test_requires_git below) to 'use
Test::Requires::Git' will override it for the rest of the program run.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
