#
# spec file for package perl-Parse-ANSIColor-Tiny
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Parse-ANSIColor-Tiny
Name:           perl-Parse-ANSIColor-Tiny
Version:        0.700
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Determine attributes of ANSI-Colored string
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
%{perl_requires}

%description
Parse a string colored with ANSI escape sequences into a structure suitable
for reformatting (into HTML, for example).

The output of terminal commands can be marked up with colors and formatting
that in some instances you'd like to preserve.

This module is essentially the inverse of Term::ANSIColor. The array refs
returned from parse can be passed back in to 'Term::ANSIColor::colored'.
The strings may not match exactly due to different ways the attributes can
be specified, but the end result should be colored the same.

This is a '::Tiny' module... it attempts to be correct for most cases with
a small amount of code. It may not be 100% correct, especially in complex
cases. It only handles the 'm' escape sequence ('\033[0m') which produces
colors and simple attributes (bold, underline) (like what can be produced
with Term::ANSIColor). Other escape sequences are removed by default but
you can disable this by passing 'remove_escapes => 0' to the constructor.

If you do find bugs please submit tickets (with patches, if possible).

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
