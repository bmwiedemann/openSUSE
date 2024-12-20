#
# spec file for package perl-lib-relative
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name lib-relative
Name:           perl-lib-relative
Version:        1.2.0
Release:        0
%define cpan_version 1.002
Provides:       perl(lib::relative) = 1.2.0
License:        Artistic-2.0
Summary:        Add paths relative to the current file to @INC
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.88
%undefine       __perllib_provides
%{perl_requires}

%description
Adding a path to @INC to load modules from a local directory may seem
simple, but has a few common pitfalls to be aware of. Directly adding a
relative path to '@INC' means that any later code that changes the current
working directory will change where modules are loaded from. This applies
to the '.' path that used to be in '@INC' by default until perl 5.26.0, or
a relative path added in code like 'use lib 'path/to/lib'', and may be a
vulnerability if such a location is not supposed to be writable.
Additionally, the commonly used FindBin module relies on interpreter state
and the path to the original script invoked by the perl interpreter,
sometimes requiring workarounds in uncommon cases like generated or
embedded code. This module proposes a more straightforward method: take a
path relative to the current file, absolutize it, and add it to '@INC'.

If this module is already available to be loaded, it can be used as with
lib.pm, passing relative paths, which will be absolutized relative to the
current file then passed on to lib. Multiple arguments will be separately
absolutized, and absolute paths will be passed on unchanged.

For cases where this module cannot be loaded beforehand, the last section
of the "SYNOPSIS" can be copy-pasted into a file to perform the same task.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
