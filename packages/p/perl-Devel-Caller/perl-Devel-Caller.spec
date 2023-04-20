#
# spec file for package perl-Devel-Caller
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


%define cpan_name Devel-Caller
Name:           perl-Devel-Caller
Version:        2.07
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Meatier versions of caller
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
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

'called_with' returns a list of references to the original arguments to the
subroutine at $level. if $names is true, the names of the variables will be
returned instead

constants are returned as 'undef' in both cases

* called_as_method($level)

'called_as_method' returns true if the subroutine at $level was called as a
method.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
