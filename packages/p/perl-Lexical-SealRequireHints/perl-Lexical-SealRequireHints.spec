#
# spec file for package perl-Lexical-SealRequireHints
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


%define cpan_name Lexical-SealRequireHints
Name:           perl-Lexical-SealRequireHints
Version:        0.012
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Prevent leakage of lexical hints
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
%{perl_requires}

%description
This module works around two historical bugs in Perl's handling of the
'%^H' (lexical hints) variable. One bug causes lexical state in one file to
leak into another that is 'require'd/'use'd/'do'ed from it. This bug, [perl
#68590], was present from Perl 5.6 up to Perl 5.10, fixed in Perl 5.11.0.
The second bug causes lexical state (normally a blank '%^H' once the first
bug is fixed) to leak outwards from 'utf8.pm', if it is automatically
loaded during Unicode regular expression matching, into whatever source is
compiling at the time of the regexp match. This bug, [perl #73174], was
present from Perl 5.8.7 up to Perl 5.11.5, fixed in Perl 5.12.0.

Both of these bugs seriously damage the usability of any module relying on
'%^H' for lexical scoping, on the affected Perl versions. It is in practice
essential to work around these bugs when using such modules. On versions of
Perl that require such a workaround, this module globally changes the
behaviour of 'require', including 'use' and the implicit 'require'
performed in Unicode regular expression matching, and of 'do', so that they
no longer exhibit these bugs.

The workaround supplied by this module takes effect the first time its
'import' method is called. Typically this will be done by means of a 'use'
statement. This should be done as early as possible, because it only
affects 'require'/'use'/'do' statements that are compiled after the
workaround goes into effect. For 'use' statements, and 'require' and 'do'
statements that are executed immediately and only once, it suffices to
invoke the workaround when loading the first module that will set up
vulnerable lexical state. Delayed-action 'require' and 'do' statements,
however, are more troublesome, and can require the workaround to be loaded
much earlier. Ultimately, an affected Perl program may need to load the
workaround as very nearly its first action. Invoking this module multiple
times, from multiple modules, is not a problem: the workaround is only
applied once, and applies to everything subsequently compiled.

This module is implemented in XS, with a pure Perl backup version for
systems that can't handle XS modules. The XS version has a better chance of
playing nicely with other modules that modify 'require' or 'do' handling.
The pure Perl version can't work at all on some Perl versions; users of
those versions must use the XS. On all Perl versions suffering the
underlying hint leakage bug, pure Perl hooking of 'require' breaks the use
of 'require' without an explicit parameter (implicitly using '$_').

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
