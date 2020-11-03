#
# spec file for package perl-ExtUtils-CBuilder
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


Name:           perl-ExtUtils-CBuilder
Version:        0.280235
Release:        0
%define cpan_name ExtUtils-CBuilder
Summary:        Compile and link C code for Perl modules
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Spec) >= 3.13
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Perl::OSType) >= 1
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(IPC::Cmd)
Requires:       perl(Perl::OSType) >= 1
%{perl_requires}

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the 'Module::Build' project, but may be useful for other
purposes as well. However, it is _not_ intended as a general cross-platform
interface to all your C building needs. That would have been a much more
ambitious goal!

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING README README.mkdn README.patching README.release
%license LICENSE

%changelog
