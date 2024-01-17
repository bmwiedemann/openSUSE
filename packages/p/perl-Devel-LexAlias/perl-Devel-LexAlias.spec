#
# spec file for package perl-Devel-LexAlias
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


Name:           perl-Devel-LexAlias
Version:        0.05
Release:        0
%define cpan_name Devel-LexAlias
Summary:        alias lexical variables
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-LexAlias/
Source:         http://www.cpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Caller) >= 0.03
#BuildRequires: perl(Devel::LexAlias)
Requires:       perl(Devel::Caller) >= 0.03
%{perl_requires}

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

If you don't know why you'd want to do this, I'd suggest that you skip this
module. If you think you have a use for it, I'd insist on it.

Still here?

* lexalias( $where, $name, $variable )

  '$where' refers to the subroutine in which to alias the lexical, it can
  be a coderef or a call level such that you'd give to 'caller'

  '$name' is the name of the lexical within that subroutine

  '$variable' is a reference to the variable to install at that location

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
