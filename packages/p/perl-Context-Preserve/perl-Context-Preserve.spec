#
# spec file for package perl-Context-Preserve
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Context-Preserve
Name:           perl-Context-Preserve
Version:        0.30.0
Release:        0
# 0.03 -> normalize -> 0.30.0
%define cpan_version 0.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Run code after a subroutine call, preserving the context the subroutine [cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(ok)
Provides:       perl(Context::Preserve) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Sometimes you need to call a function, get the results, act on the results,
then return the result of the function. This is painful because of
contexts; the original function can behave different if it's called in
void, scalar, or list context. You can ignore the various cases and just
pick one, but that's fragile. To do things right, you need to see which
case you're being called in, and then call the function in that context.
This results in 3 code paths, which is a pain to type in (and maintain).

This module automates the process. You provide a coderef that is the
"original function", and another coderef to run after the original runs.
You can modify the return value (aliased to @_) here, and do whatever else
you need to do. 'wantarray' is correct inside both coderefs; in "after",
though, the return value is ignored and the value 'wantarray' returns is
related to the context that the original function was called in.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
