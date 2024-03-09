#
# spec file for package perl-HTML-FromANSI-Tiny
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


%define cpan_name HTML-FromANSI-Tiny
Name:           perl-HTML-FromANSI-Tiny
Version:        0.107.0
Release:        0
%define cpan_version 0.107
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Easily convert colored command line output to HTML
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Parse::ANSIColor::Tiny) >= 0.600
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
Requires:       perl(HTML::Entities)
Requires:       perl(Parse::ANSIColor::Tiny) >= 0.600
Provides:       perl(HTML::FromANSI::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Convert the output from a terminal command that is decorated with ANSI
escape sequences into customizable HTML (with a small amount of code).

This module complements Parse::ANSIColor::Tiny by providing a simple HTML
markup around its output.

Parse::ANSIColor::Tiny returns a data structure that's easy to reformat
into any desired output. Reformatting to HTML seemed simple and common
enough to warrant this module as well.

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
%doc Changes examples README
%license LICENSE

%changelog
