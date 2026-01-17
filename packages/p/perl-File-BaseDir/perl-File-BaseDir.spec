#
# spec file for package perl-File-BaseDir
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


%define cpan_name File-BaseDir
Name:           perl-File-BaseDir
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Use the Freedesktop.org base directory specification
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(IPC::System::Simple)
Provides:       perl(File::BaseDir) = %{version}
Provides:       perl(File::IconTheme) = %{version}
Provides:       perl(File::UserDirs) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module can be used to find directories and files as specified by the
Freedesktop.org Base Directory Specification. This specifications gives a
mechanism to locate directories for configuration, application data and
cache data. It is suggested that desktop applications for e.g. the GNOME,
KDE or Xfce platforms follow this layout. However, the same layout can just
as well be used for non-GUI applications.

This module forked from File::MimeInfo.

This module follows version 0.6 of BaseDir specification.

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
%doc Changes README
%license LICENSE

%changelog
