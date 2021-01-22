#
# spec file for package perl-File-chdir
#
# Copyright (c) 2021 SUSE LLC
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


Name:           perl-File-chdir
Version:        0.1011
Release:        0
%define cpan_name File-chdir
Summary:        More sensible way to change directories
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd) >= 3.16
BuildRequires:  perl(File::Spec::Functions) >= 3.27
Requires:       perl(Cwd) >= 3.16
Requires:       perl(File::Spec::Functions) >= 3.27
%{perl_requires}

%description
Perl's 'chdir()' has the unfortunate problem of being very, very, very
global. If any part of your program calls 'chdir()' or if any library you
use calls 'chdir()', it changes the current working directory for the
*whole* program.

This sucks.

File::chdir gives you an alternative, '$CWD' and '@CWD'. These two
variables combine all the power of 'chdir()', File::Spec and Cwd.

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
%doc Changes CONTRIBUTING.mkdn examples README
%license LICENSE

%changelog
