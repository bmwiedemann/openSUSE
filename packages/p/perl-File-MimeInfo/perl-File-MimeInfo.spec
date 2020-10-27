#
# spec file for package perl-File-MimeInfo
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


Name:           perl-File-MimeInfo
Version:        0.30
Release:        0
%define cpan_name File-MimeInfo
Summary:        Determine file type from the file name
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(File::BaseDir) >= 0.03
BuildRequires:  perl(File::DesktopEntry) >= 0.04
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  shared-mime-info
Requires:       shared-mime-info
Requires:       perl(File::BaseDir) >= 0.03
# MANUAL END

%description
This module can be used to determine the mime type of a file. It tries to
implement the freedesktop specification for a shared MIME database.

For this module shared-mime-info-spec 0.13 was used.

This package only uses the globs file. No real magic checking is used. The
File::MimeInfo::Magic package is provided for magic typing.

If you want to determine the mimetype of data in a memory buffer you should
use File::MimeInfo::Magic in combination with IO::Scalar.

This module loads the various data files when needed. If you want to hash
data earlier see the 'rehash' methods below.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes mimeopen mimetype README.md

%changelog
