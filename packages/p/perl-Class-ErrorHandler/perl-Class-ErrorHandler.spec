#
# spec file for package perl-Class-ErrorHandler
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


Name:           perl-Class-ErrorHandler
Version:        0.04
Release:        0
%define cpan_name Class-ErrorHandler
Summary:        Base class for error handling
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-ErrorHandler/
Source0:        http://www.cpan.org/authors/id/T/TO/TOKUHIROM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
_Class::ErrorHandler_ provides an error-handling mechanism that's generic
enough to be used as the base class for a variety of OO classes. Subclasses
inherit its two error-handling methods, _error_ and _errstr_, to
communicate error messages back to the calling program.

On failure (for whatever reason), a subclass should call _error_ and return
to the caller; _error_ itself sets the error message internally, then
returns 'undef'. This has the effect of the method that failed returning
'undef' to the caller. The caller should check for errors by checking for a
return value of 'undef', and calling _errstr_ to get the value of the error
message on an error.

As demonstrated in the the SYNOPSIS manpage, _error_ and _errstr_ work as
both class methods and object methods.

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
%doc Changes LICENSE minil.toml README.md

%changelog
