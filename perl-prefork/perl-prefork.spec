#
# spec file for package perl-prefork
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-prefork
Version:        1.04
Release:        0
%define cpan_name prefork
Summary:        Optimized module loading for forking or non-forking processes
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/prefork/
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         fix-build.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The 'prefork' pragma is intended to allow module writers to optimise module
loading for *both* scenarios with as little additional code as possible.

prefork.pm is intended to serve as a central and optional marshalling point
for state detection (are we running in compile-time or run-time mode) and
to act as a relatively light-weight module loader.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

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
