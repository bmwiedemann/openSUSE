#
# spec file for package perl-PAR-Packer
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


%define cpan_name PAR-Packer
Name:           perl-PAR-Packer
Version:        1.057
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        PAR Packager
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.02
BuildRequires:  perl(Compress::Zlib) >= 1.30
BuildRequires:  perl(Digest::SHA) >= 5.40
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Getopt::ArgvFile) >= 1.07
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(Module::ScanDeps) >= 1.21
BuildRequires:  perl(PAR) >= 1.016
BuildRequires:  perl(PAR::Dist) >= 0.22
Requires:       perl(Archive::Zip) >= 1.02
Requires:       perl(Compress::Zlib) >= 1.30
Requires:       perl(Digest::SHA) >= 5.40
Requires:       perl(Getopt::ArgvFile) >= 1.07
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Module::ScanDeps) >= 1.21
Requires:       perl(PAR) >= 1.016
Requires:       perl(PAR::Dist) >= 0.22
Recommends:     perl(Module::Signature)
Recommends:     perl(Tk)
Recommends:     perl(Tk::ColoredButton)
Recommends:     perl(Tk::EntryCheck)
Recommends:     perl(Tk::Getopt)
%{perl_requires}

%description
This module implements the *App::Packer::Backend* interface, for generating
stand-alone executables, perl scripts and PAR files.

Currently, this module is used by the command line tool *pp* internally, as
well as by the contributed _contrib/gui_pp/gpp_ program.

Since version 0.97 of PAR, this module and its related tools such as 'pp'
have been stripped from the PAR distribution and are now distributed as the
'PAR-Packer' distribution so that PAR users need not necessarily have a C
compiler.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
# build system busted - only supporting serial build
%{__make} -j1

%check
export PERL_TEST_POD=1
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc AUTHORS Changes README
%license LICENSE

%changelog
