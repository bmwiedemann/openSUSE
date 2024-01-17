#
# spec file for package perl-Test-InDistDir
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Test-InDistDir
Version:        1.112071
Release:        0
%define cpan_name Test-InDistDir
Summary:        test environment setup for development with IDE
License:        SUSE-Permissive
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-InDistDir/
Source:         http://www.cpan.org/authors/id/M/MI/MITHALDU/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module helps run test scripts in IDEs like Komodo.

When running test scripts in an IDE i have to set up a project file
defining the dist dir to run tests in and a lib dir to load additional
modules from. Often I didn't feel like doing that, especially when i only
wanted to do a small patch to a dist. In those cases i added a BEGIN block
to mangle the environment for me.

This module basically is that BEGIN block. It automatically moves up one
directory when it cannot see the test script in "t/$scriptname" and
includes 'lib' in @INC when there's no blib present. That way the test ends
up with almost the same environment it'd get from EUMM/prove/etc., even
when it's actually run inside the t/ directory.

At the same time it will still function correctly when called by
EUMM/prove/etc., since it does not change the environment in those cases.

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
%doc Changes LICENSE README.mkdn

%changelog
