#
# spec file for package perl-ExtUtils-InstallPaths
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


%define cpan_name ExtUtils-InstallPaths
Name:           perl-ExtUtils-InstallPaths
Version:        0.14.0
Release:        0
# 0.014 -> normalize -> 0.14.0
%define cpan_version 0.014
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Build.PL install path logic made easy
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Config) >= 0.9.0
Requires:       perl(ExtUtils::Config) >= 0.9.0
Provides:       perl(ExtUtils::InstallPaths) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module tries to make install path resolution as easy as possible.

When you want to install a module, it needs to figure out where to install
things. The nutshell version of how this works is that default installation
locations are determined from ExtUtils::Config, and they may be
individually overridden by using the 'install_path' attribute. An
'install_base' attribute lets you specify an alternative installation root
like _/home/foo_ and 'prefix' does something similar in a rather different
(and more complicated) way. 'destdir' lets you specify a temporary
installation directory like _/tmp/install_ in case you want to create
bundled-up installable packages.

The following types are supported by default.

* * lib

Usually pure-Perl module files ending in _.pm_ or _.pod_.

* * arch

"Architecture-dependent" module files, usually produced by compiling XS,
Inline, or similar code.

* * script

Programs written in pure Perl. In order to improve reuse, you may want to
make these as small as possible - put the code into modules whenever
possible.

* * bin

"Architecture-dependent" executable programs, i.e. compiled C code or
something. Pretty rare to see this in a perl distribution, but it happens.

* * bindoc

Documentation for the stuff in 'script' and 'bin'. Usually generated from
the POD in those files. Under Unix, these are manual pages belonging to the
'man1' category. Unless explicitly set, this is only available on platforms
supporting manpages.

* * libdoc

Documentation for the stuff in 'lib' and 'arch'. This is usually generated
from the POD in _.pm_ and _.pod_ files. Under Unix, these are manual pages
belonging to the 'man3' category. Unless explicitly set, this is only
available on platforms supporting manpages.

* * binhtml

This is the same as 'bindoc' above, but applies to HTML documents. Unless
explicitly set, this is only available when perl was configured to do so.

* * libhtml

This is the same as 'libdoc' above, but applies to HTML documents. Unless
explicitly set, this is only available when perl was configured to do so.

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
%doc Changes README
%license LICENSE

%changelog
