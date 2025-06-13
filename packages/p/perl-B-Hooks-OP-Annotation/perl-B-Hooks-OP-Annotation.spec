#
# spec file for package perl-B-Hooks-OP-Annotation
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


%define cpan_name B-Hooks-OP-Annotation
Name:           perl-B-Hooks-OP-Annotation
Version:        0.440.0
Release:        0
# 0.44 -> normalize -> 0.440.0
%define cpan_version 0.44
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Annotate and delegate hooked OPs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.304
Requires:       perl(ExtUtils::Depends) >= 0.304
Provides:       perl(B::Hooks::OP::Annotation) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides a way for XS code that hijacks OP 'op_ppaddr'
functions to delegate to (or restore) the previous functions, whether
assigned by perl or by another module. Typically this should be used in
conjunction with B::Hooks::OP::Check.

'B::Hooks::OP::Annotation' makes its types and functions available to XS
code by means of ExtUtils::Depends. Modules that wish to use these exports
in their XS code should 'use B::OP::Hooks::Annotation' in the Perl module
that loads the XS, and include something like the following in their
Makefile.PL:

    use ExtUtils::MakeMaker;
    use ExtUtils::Depends;

    our %XS_PREREQUISITES = (
        'B::Hooks::OP::Annotation' => '0.44',
        'B::Hooks::OP::Check'      => '0.15',
    );

    our %XS_DEPENDENCIES = ExtUtils::Depends->new(
        'Your::XS::Module',
         keys(%XS_PREREQUISITES)
    )->get_makefile_vars();

    WriteMakefile(
        NAME          => 'Your::XS::Module',
        VERSION_FROM  => 'lib/Your/XS/Module.pm',
        PREREQ_PM => {
            'B::Hooks::EndOfScope' => '0.07',
            %XS_PREREQUISITES
        },
        ($ExtUtils::MakeMaker::VERSION >= 6.46 ?
            (META_MERGE => {
                configure_requires => {
                    'ExtUtils::Depends' => '0.301',
                    %XS_PREREQUISITES
                }})
            : ()
        ),
        %XS_DEPENDENCIES,
        # ...
    );

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
