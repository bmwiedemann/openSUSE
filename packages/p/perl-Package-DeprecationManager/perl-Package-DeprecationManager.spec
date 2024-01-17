#
# spec file for package perl-Package-DeprecationManager
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


%define cpan_name Package-DeprecationManager
Name:           perl-Package-DeprecationManager
Version:        0.18
Release:        0
License:        Artistic-2.0
Summary:        Manage deprecation warnings for your distribution
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Package::Stash)
Requires:       perl(Params::Util)
Requires:       perl(Sub::Install)
Requires:       perl(Sub::Util)
%{perl_requires}

%description
This module allows you to manage a set of deprecations for one or more
modules.

When you import 'Package::DeprecationManager', you must provide a set of
'-deprecations' as a hash ref. The keys are "feature" names, and the values
are the version when that feature was deprecated.

In many cases, you can simply use the fully qualified name of a subroutine
or method as the feature name. This works for cases where the whole
subroutine is deprecated. However, the feature names can be any string.
This is useful if you don't want to deprecate an entire subroutine, just a
certain usage.

You can also provide an optional array reference in the '-ignore'
parameter.

The values to be ignored can be package names or regular expressions (made
with 'qr//'). Use this to ignore packages in your distribution that can
appear on the call stack when a deprecated feature is used.

As part of the import process, 'Package::DeprecationManager' will export
two subroutines into its caller. It provides an 'import()' sub for the
caller and a 'deprecated()' sub.

The 'import()' sub allows callers of _your_ class to specify an
'-api_version' parameter. If this is supplied, then deprecation warnings
are only issued for deprecations with API versions earlier than the one
specified.

You must call the 'deprecated()' sub in each deprecated subroutine. When
called, it will issue a warning using 'Carp::cluck()'.

The 'deprecated()' sub can be called in several ways. If you do not pass
any arguments, it will generate an appropriate warning message. If you pass
a single argument, this is used as the warning message.

Finally, you can call it with named arguments. Currently, the only allowed
names are 'message' and 'feature'. The 'feature' argument should correspond
to the feature name passed in the '-deprecations' hash.

If you don't explicitly specify a feature, the 'deprecated()' sub uses
'caller()' to identify its caller, using its fully qualified subroutine
name.

A given deprecation warning is only issued once for a given package. This
module tracks this based on both the feature name _and_ the error message
itself. This means that if you provide several different error messages for
the same feature, all of those errors will appear.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
