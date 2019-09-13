#
# spec file for package perl-syntax
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


Name:           perl-syntax
Version:        0.004
Release:        0
%define cpan_name syntax
Summary:        Activate syntax extensions
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/syntax/
Source:         http://www.cpan.org/authors/id/P/PH/PHAYLON/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::OptList) >= 0.104
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(namespace::clean)
#BuildRequires: perl(syntax)
Requires:       perl(Data::OptList) >= 0.104
Requires:       perl(namespace::clean)
%{perl_requires}

%description
This module activates community provided syntax extensions to Perl. You
pass it a feature name, and optionally a scalar with arguments, and the
dispatching system will load and install the extension in your package.

The import arguments are parsed with the Data::OptList manpage. There are
no standardised options. Please consult the documentation for the specific
syntax feature to find out about possible configuration options.

The passed in feature names are simply transformed: 'function' becomes the
Syntax::Feature::Function manpage and 'foo_bar' would become
'Syntax::Feature::FooBar'.

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
%doc Changes LICENSE README weaver.ini

%changelog
