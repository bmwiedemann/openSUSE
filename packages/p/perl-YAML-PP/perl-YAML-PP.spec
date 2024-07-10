#
# spec file for package perl-YAML-PP
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


%define cpan_name YAML-PP
Name:           perl-YAML-PP
Version:        0.38.0
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        YAML 1.2 Processor
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warn)
Requires:       perl(Module::Load)
%{perl_requires}

%description
YAML::PP is a modular YAML processor.

It aims to support 'YAML 1.2' and 'YAML 1.1'. See https://yaml.org/. Some
(rare) syntax elements are not yet supported and documented below.

YAML is a serialization language. The YAML input is called "YAML Stream". A
stream consists of one or more "Documents", separated by a line with a
document start marker '---'. A document optionally ends with the document
end marker '...'.

This allows one to process continuous streams additionally to a fixed input
file or string.

The YAML::PP frontend will currently load all documents, and return only
the first if called with scalar context.

The YAML backend is implemented in a modular way that allows one to add
custom handling of YAML tags, perl objects and data types. The inner API is
not yet stable. Suggestions welcome.

You can check out all current parse and load results from the
yaml-test-suite here: https://perlpunk.github.io/YAML-PP-p5/test-suite.html

%prep
%autosetup  -n %{cpan_name}-v%{version}

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
%doc Changes CONTRIBUTING.md examples Makefile.dev README.md
%license LICENSE

%changelog
