#
# spec file for package perl-Devel-LexAlias
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Devel-LexAlias
Name:           perl-Devel-LexAlias
Version:        0.50.0
Release:        0
# 0.05 -> normalize -> 0.50.0
%define cpan_version 0.05
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Alias lexical variables
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Caller) >= 0.30
Requires:       perl(Devel::Caller) >= 0.30
Provides:       perl(Devel::LexAlias) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

If you don't know why you'd want to do this, I'd suggest that you skip this
module. If you think you have a use for it, I'd insist on it.

Still here?

* lexalias( $where, $name, $variable )

'$where' refers to the subroutine in which to alias the lexical, it can be
a coderef or a call level such that you'd give to 'caller'

'$name' is the name of the lexical within that subroutine

'$variable' is a reference to the variable to install at that location

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
