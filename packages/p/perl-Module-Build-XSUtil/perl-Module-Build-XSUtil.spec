#
# spec file for package perl-Module-Build-XSUtil
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Module-Build-XSUtil
Version:        0.19
Release:        0
%define cpan_name Module-Build-XSUtil
Summary:        Module::Build class for building XS modules
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HI/HIDEAKIO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cwd::Guard)
BuildRequires:  perl(Devel::CheckCompiler)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Copy::Recursive::Reduced) >= 0.002
BuildRequires:  perl(Module::Build) >= 0.400500
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(parent)
Requires:       perl(Devel::CheckCompiler)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(parent)
%{perl_requires}

%description
Module::Build::XSUtil is subclass of Module::Build for support building XS
modules.

This is a list of a new parameters in the Module::Build::new method:

* needs_compiler_c99

This option checks C99 compiler's availability. If it's not available,
Build.PL exits by 0.

* needs_compiler_cpp

This option checks C++ compiler's availability. If it's not available,
Build.PL exits by 0.

In addition, append 'extra_compiler_flags' and 'extra_linker_flags' for
C++.

* generate_ppport_h

Genereate ppport.h by Devel::PPPort.

* generate_xshelper_h

Genereate xshelper.h which is a helper header file to include EXTERN.h,
perl.h, XSUB.h and ppport.h, and defines some portability stuff which are
not supported by ppport.h.

It is porting from Module::Install::XSUtil.

* cc_warnings

Enable compiler warnings flag. It is enable by default.

* -g options

If invoke Build.PL with '-g' option, It will build with debug options.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes minil.toml README.md
%license LICENSE

%changelog
