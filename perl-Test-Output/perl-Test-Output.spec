#
# spec file for package perl-Test-Output
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


Name:           perl-Test-Output
Version:        1.031
Release:        0
%define cpan_name Test-Output
Summary:        Utilities to test STDOUT and STDERR messages
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Output/
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(File::Temp) >= 0.17
BuildRequires:  perl(Test::Tester) >= 0.107
Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(File::Temp) >= 0.17
%{perl_requires}

%description
Test::Output provides a simple interface for testing output sent to
'STDOUT' or 'STDERR'. A number of different utilities are included to try
and be as flexible as possible to the tester.

Likewise, Capture::Tiny provides a much more robust capture mechanism
without than the original Test::Output::Tie.

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
%doc Changes
%license LICENSE

%changelog
