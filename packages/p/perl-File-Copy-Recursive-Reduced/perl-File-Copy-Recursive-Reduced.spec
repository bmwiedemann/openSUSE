#
# spec file for package perl-File-Copy-Recursive-Reduced
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


%define cpan_name File-Copy-Recursive-Reduced
Name:           perl-File-Copy-Recursive-Reduced
Version:        0.7.0
Release:        0
%define cpan_version 0.007
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Recursive copying of files and directories within Perl 5 toolchain
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Path::Tiny)
Provides:       perl(File::Copy::Recursive::Reduced) = 0.7.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
This library is intended as a not-quite-drop-in replacement for certain
functionality provided by CPAN distribution
File-Copy-Recursive|http://search.cpan.org/dist/File-Copy-Recursive/. The
library provides methods similar enough to that distribution's 'fcopy()',
'dircopy()' and 'rcopy()' functions to be usable in those CPAN
distributions often described as being part of the Perl toolchain.

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
%doc Changes README Todo
%license LICENSE

%changelog
