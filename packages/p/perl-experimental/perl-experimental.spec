#
# spec file for package perl-experimental
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


Name:           perl-experimental
Version:        0.020
Release:        0
%define cpan_name experimental
Summary:        Experimental features made easy
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/experimental/
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(version)
Requires:       perl(version)
%{perl_requires}

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

Every version of perl has some number of features present but considered
"experimental." For much of the life of Perl 5, this was only a designation
found in the documentation. Starting in Perl v5.10.0, and more aggressively
in v5.18.0, experimental features were placed behind pragmata used to
enable the feature and disable associated warnings.

The 'experimental' pragma exists to combine the required incantations into
a single interface stable across releases of perl. For every experimental
feature, this should enable the feature and silence warnings for the
enclosing lexical scope:

  use experimental 'feature-name';

To disable the feature and, if applicable, re-enable any warnings, use:

  no experimental 'feature-name';

The supported features, documented further below, are:

* * 'array_base' - allow the use of '$[' to change the starting index of
  '@array'.

This is supported on all versions of perl.

* * 'autoderef' - allow push, each, keys, and other built-ins on
  references.

This was added in perl 5.14.0 and removed in perl 5.23.1.

* * 'bitwise' - allow the new stringwise bit operators

This was added in perl 5.22.0.

* * 'const_attr' - allow the :const attribute on subs

This was added in perl 5.22.0.

* * 'lexical_topic' - allow the use of lexical '$_' via 'my $_'.

This was added in perl 5.10.0 and removed in perl 5.23.4.

* * 'lexical_subs' - allow the use of lexical subroutines.

This was added in 5.18.0.

* * 'postderef' - allow the use of postfix dereferencing expressions,
  including in interpolating strings

This was added in perl 5.20.0.

* * 're_strict' - enables strict mode in regular expressions

This was added in perl 5.22.0.

* * 'refaliasing' - allow aliasing via '\$x = \$y'

This was added in perl 5.22.0.

* * 'regex_sets' - allow extended bracketed character classes in regexps

This was added in perl 5.18.0.

* * 'signatures' - allow subroutine signatures (for named arguments)

This was added in perl 5.20.0.

* * 'smartmatch' - allow the use of '~~'

This was added in perl 5.10.0, but it should be noted there are significant
incompatibilities between 5.10.0 and 5.10.1.

* * 'switch' - allow the use of '~~', given, and when

This was added in perl 5.10.0.

* * 'win32_perlio' - allows the use of the :win32 IO layer.

This was added on perl 5.22.0.

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
%doc Changes README
%license LICENSE

%changelog
