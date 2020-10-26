#
# spec file for package perl-ExtUtils-MakeMaker
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-ExtUtils-MakeMaker
Version:        7.50
Release:        0
%define cpan_name ExtUtils-MakeMaker
Summary:        Create a module Makefile
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Do_not_set_RPATH_by_default.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This utility is designed to write a Makefile for an extension module from a
Makefile.PL. It is based on the Makefile.SH model provided by Andy
Dougherty and the perl5-porters.

It splits the task of generating the Makefile into several subroutines that
can be individually overridden. Each subroutine returns the text it wishes
to have written to the Makefile.

As there are various Make programs with incompatible syntax, which use
operating system shells, again with incompatible syntax, it is important
for users of this module to know which flavour of Make a Makefile has been
written for so they'll use the correct one and won't have to face the
possibly bewildering errors resulting from using the wrong one.

On POSIX systems, that program will likely be GNU Make; on Microsoft
Windows, it will be either Microsoft NMake, DMake or GNU Make. See the
section on the L</"MAKE"> parameter for details.

ExtUtils::MakeMaker (EUMM) is object oriented. Each directory below the
current directory that contains a Makefile.PL is treated as a separate
object. This makes it possible to write an unlimited number of Makefiles
with a single invocation of WriteMakefile().

All inputs to WriteMakefile are Unicode characters, not just octets. EUMM
seeks to handle all of these correctly. It is currently still not possible
to portably use Unicode characters in module names, because this requires
Perl to handle Unicode filenames, which is not yet the case on Windows.

See L<ExtUtils::MakeMaker::FAQ> for details of the design and usage.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
%patch0 -p1

%build
export BUILDING_AS_PACKAGE=1
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}
%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
rm $RPM_BUILD_ROOT/usr/bin/instmodsh
rm $RPM_BUILD_ROOT/usr/share/man/man1/instmodsh.1
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README README.packaging

%changelog
