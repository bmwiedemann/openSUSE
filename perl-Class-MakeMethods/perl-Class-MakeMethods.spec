#
# spec file for package perl-Class-MakeMethods
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Class-MakeMethods
%define cpan_name Class-MakeMethods
Summary:        Generate common types of methods
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        1.01
Release:        0
Url:            http://search.cpan.org/dist/Class-MakeMethods/
#Source:         http://www.cpan.org/authors/id/E/EV/EVO/Class-MakeMethods-%{version}.tar.gz
Source:         Class-MakeMethods-%{version}-cleaned.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
The Class::MakeMethods framework allows Perl class developers to quickly
define common types of methods. When a module uses Class::MakeMethods or
one of its subclasses, it can select from a variety of supported method
types, and specify a name for each method desired. The methods are
dynamically generated and installed in the calling package.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc CHANGES MakeMethods README tests

%changelog
