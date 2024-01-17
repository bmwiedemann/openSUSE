#
# spec file for package perl-Test-Fork
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Test-Fork
Name:           perl-Test-Fork
Version:        0.02
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Test code which forks
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.280800
%{perl_requires}

%description
*THIS IS ALPHA CODE!* The implementation is unreliable and the interface is
subject to change.

Because each test has a number associated with it, testing code which forks
is problematic. Coordinating the test number amongst the parent and child
processes is complicated. Test::Fork provides a function to smooth over the
complications.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
