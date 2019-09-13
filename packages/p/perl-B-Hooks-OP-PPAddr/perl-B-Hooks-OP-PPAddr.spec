#
# spec file for package perl-B-Hooks-OP-PPAddr
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-B-Hooks-OP-PPAddr
Version:        0.06
Release:        0
%define cpan_name B-Hooks-OP-PPAddr
Summary:        Hook into opcode execution
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/B-Hooks-OP-PPAddr/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        perl-B-Hooks-OP-PPAddr-rpmlintrc
Source2:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
This module provides a C API for XS modules to hook into the execution of
perl opcodes.

ExtUtils::Depends is used to export all functions for other XS modules to
use. Include the following in your _Makefile.PL_:

    my $pkg = ExtUtils::Depends->new('Your::XSModule', 'B::Hooks::OP::PPAddr');
    WriteMakefile(
        ... # your normal makefile flags
        $pkg->get_makefile_vars,
    );

Your XS module can now include 'hook_op_ppaddr.h'.

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
