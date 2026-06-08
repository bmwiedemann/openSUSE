#
# spec file for package perl-File-DesktopEntry
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name File-DesktopEntry
Name:           perl-File-DesktopEntry
Version:        0.230.0
Release:        0
# 0.23 -> normalize -> 0.230.0
%define cpan_version 0.23
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Module to handle .desktop files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::BaseDir) >= 0.30
BuildRequires:  perl(URI::Escape)
Requires:       perl(File::BaseDir) >= 0.30
Requires:       perl(URI::Escape)
Provides:       perl(File::DesktopEntry) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is designed to work with _.desktop_ files. The format of these
files is specified by the freedesktop "Desktop Entry" specification. This
module can parse these files but also knows how to run the applications
defined by these files.

For this module version 1.0 of the specification was used.

This module was written to support File::MimeInfo::Applications.

Please remember: case is significant for the names of Desktop Entry keys.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README.md

%changelog
