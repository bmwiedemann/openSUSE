#
# spec file for package perl-FFI-CheckLib
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-FFI-CheckLib
Version:        0.27
Release:        0
%define cpan_name FFI-CheckLib
Summary:        Check that a library is available for FFI
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require::EnvVar) >= 0.000060
BuildRequires:  perl(Test2::Require::Module) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
%{perl_requires}

%description
This module checks whether a particular dynamic library is available for
FFI to use. It is modeled heavily on Devel::CheckLib, but will find dynamic
libraries even when development packages are not installed. It also
provides a find_lib function that will return the full path to the found
dynamic library, which can be feed directly into FFI::Platypus or another
FFI system.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc author.yml Changes example README
%license LICENSE

%changelog
