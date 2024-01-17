#
# spec file for package perl-Variable-Magic
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


%define cpan_name Variable-Magic
Name:           perl-Variable-Magic
Version:        0.63
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Associate user-defined magic to variables from Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Magic is Perl's way of enhancing variables. This mechanism lets the user
add extra data to any variable and hook syntactical operations (such as
access, assignment or destruction) that can be applied to it. With this
module, you can add your own magic to any variable without having to write
a single line of XS.

You'll realize that these magic variables look a lot like tied variables.
It is not surprising, as tied variables are implemented as a special kind
of magic, just like any 'irregular' Perl variable : scalars like '$!', '$('
or '$^W', the '%ENV' and '%SIG' hashes, the '@ISA' array, 'vec()' and
'substr()' lvalues, threads::shared variables... They all share the same
underlying C API, and this module gives you direct access to it.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README samples

%changelog
