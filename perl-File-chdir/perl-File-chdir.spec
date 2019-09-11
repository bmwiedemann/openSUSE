#
# spec file for package perl-File-chdir
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-File-chdir
Version:        0.1010
Release:        0
%define cpan_name File-chdir
Summary:        More Sensible Way to Change Directories
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-chdir/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
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
variables combine all the power of 'chdir()', the File::Spec manpage and
the Cwd manpage.

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
%doc Changes CONTRIBUTING.mkdn examples LICENSE README

%changelog
