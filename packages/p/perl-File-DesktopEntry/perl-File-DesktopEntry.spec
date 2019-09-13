#
# spec file for package perl-File-DesktopEntry
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-File-DesktopEntry
Version:        0.22
Release:        0
%define cpan_name File-DesktopEntry
Summary:        Object to handle .desktop files
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-DesktopEntry/
Source0:        http://www.cpan.org/authors/id/M/MI/MICHIELB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::BaseDir) >= 0.03
BuildRequires:  perl(URI::Escape)
Requires:       perl(File::BaseDir) >= 0.03
Requires:       perl(URI::Escape)
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md

%changelog
