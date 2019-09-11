#
# spec file for package perl-PAR-Packer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-PAR-Packer
Version:        1.039
Release:        0
%define cpan_name PAR-Packer
Summary:        PAR Packager
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PAR-Packer/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         50ff73f26855151910e039b8480473024ae08b8a.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.02
BuildRequires:  perl(Compress::Zlib) >= 1.30
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Getopt::ArgvFile) >= 1.07
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::ScanDeps) >= 1.21
BuildRequires:  perl(PAR) >= 1.014
BuildRequires:  perl(PAR::Dist) >= 0.22
Requires:       perl(Archive::Zip) >= 1.02
Requires:       perl(Compress::Zlib) >= 1.30
Requires:       perl(Getopt::ArgvFile) >= 1.07
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Module::ScanDeps) >= 1.21
Requires:       perl(PAR) >= 1.014
Requires:       perl(PAR::Dist) >= 0.22
Recommends:     perl(Digest::SHA)
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1

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
%defattr(-,root,root,755)
%doc AUTHORS Changes README
%license LICENSE

%changelog
