#
# spec file for package perl-B-Hooks-OP-Annotation
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-B-Hooks-OP-Annotation
Version:        0.44
Release:        0
%define cpan_name B-Hooks-OP-Annotation
Summary:        annotate and delegate hooked OPs
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/B-Hooks-OP-Annotation/
Source:         http://www.cpan.org/authors/id/C/CH/CHOCOLATE/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.304
Requires:       perl(ExtUtils::Depends) >= 0.304
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
