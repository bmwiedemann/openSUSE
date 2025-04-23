#
# spec file for package perl-Inline-Lua
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Inline-Lua
Name:           perl-Inline-Lua
Version:        0.170.0
Release:        0
# 0.17 -> normalize -> 0.170.0
%define cpan_version 0.17
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for embedding Lua scripts into Perl code
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHOELZ/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         fix_Makefile_args.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Inline)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Inline)
Requires:       perl(Test::Exception)
Provides:       perl(Inline::Lua) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  lua54-devel
# MANUAL END

%description
Inline::Lua allows you to write functions in Lua. Those of you who are not
yet familiar with Lua should have a cursory glance at http://www.lua.org/
to get a taste of this language. In short:

Lua was designed to be embedded into other applications and not so much as
a language on its own. However, despite its small set of language features,
it is an extremely powerful and expressive language. Its strong areas are
an elegant and yet concise syntax, good overall performance and a beautiful
implementation of some concepts from the world of functional programming.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" INC=-I/usr/include/lua5.4 LIBS=-llua5.4
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README TODO
%license LICENSE

%changelog
