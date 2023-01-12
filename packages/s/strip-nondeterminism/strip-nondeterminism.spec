#
# spec file for package strip-nondeterminism
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


Name:           strip-nondeterminism
Version:        1.12.0
Release:        0
Summary:        A tool for stripping non-deterministic information
License:        GPL-3.0-or-later
Group:          Development/Libraries/Perl
URL:            https://anonscm.debian.org/git/reproducible/strip-nondeterminism.git
Source:         https://reproducible-builds.org/_lfs/releases/strip-nondeterminism/strip-nondeterminism-%{version}.tar.bz2
Source1:        https://reproducible-builds.org/_lfs/releases/strip-nondeterminism/strip-nondeterminism-%{version}.tar.bz2.asc
Source2:        rpmmacros
Source3:        strip-all-nondeterminism
Source4:        %{name}.keyring
Patch0:         https://salsa.debian.org/reproducible-builds/strip-nondeterminism/-/commit/f1017c67.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl-base
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Cpio)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Sub::Override)
Requires:       perl-base
Requires:       perl(Archive::Zip)
Requires:       perl(Sub::Override)
Recommends:     perl(Archive::Cpio)
%{perl_requires}

%description
File::StripNondeterminism is a Perl module for stripping bits of
non-deterministic information, such as timestamps and file system
order, from files such as gzipped files, ZIP archives, and Jar files.
It can be used as a post-processing step to make a build reproducible,
when the build process itself cannot be made deterministic.  It is used
as part of the Reproducible Builds project.

strip-nondeterminism contains the File::StripNondeterminism Perl module,
and the strip-nondeterminism command line utility.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
mkdir -p %buildroot%{_rpmmacrodir} %buildroot/%{_bindir}/
install -p %{SOURCE2} -m 644 %buildroot%{_rpmmacrodir}/macros.strip-nondeterminism
install -p %{SOURCE3} -m 755 %buildroot/%{_bindir}/
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc README TODO
%license COPYING
%{_rpmmacrodir}/macros.strip-nondeterminism

%changelog
