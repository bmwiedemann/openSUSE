#
# spec file for package perl-Devel-Caller
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Devel-Caller
Version:        2.06
Release:        0
%define cpan_name Devel-Caller
Summary:        meatier versions of C<caller>
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-Caller/
Source:         http://www.cpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(PadWalker) >= 0.08
Requires:       perl(PadWalker) >= 0.08
%{perl_requires}

%description
* caller_cv($level)

  'caller_cv' gives you the coderef of the subroutine being invoked at the
  call frame indicated by the value of $level

* caller_args($level)

  Returns the arguments passed into the caller at level $level

* caller_vars( $level, $names )
  =item called_with($level, $names)

  'called_with' returns a list of references to the original arguments to
  the subroutine at $level. if $names is true, the names of the variables
  will be returned instead

  constants are returned as 'undef' in both cases

* called_as_method($level)

  'called_as_method' returns true if the subroutine at $level was called as
  a method.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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

%changelog
