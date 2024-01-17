#
# spec file for package perl-Log-Dispatch-Array
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Log-Dispatch-Array
Name:           perl-Log-Dispatch-Array
Version:        1.005
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Log events to an array (reference)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Log::Dispatch::Output)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(Log::Dispatch::Output)
Requires:       perl(parent)
%{perl_requires}

%description
This provides a Log::Dispatch log output system that appends logged events
to an array reference. This is probably only useful for testing the logging
of your code.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
