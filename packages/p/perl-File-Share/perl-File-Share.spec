#
# spec file for package perl-File-Share
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


%define cpan_name File-Share
Name:           perl-File-Share
Version:        0.27
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extend File::ShareDir to Local Libraries
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir) >= 1.03
BuildRequires:  perl(Readonly) >= 2.05
Requires:       perl(File::ShareDir) >= 1.03
Requires:       perl(Readonly) >= 2.05
%{perl_requires}

%description
This module is a dropin replacement for File::ShareDir. It supports the
'dist_dir' and 'dist_file' functions, except these functions have been
enhanced to understand when the developer's local './share/' directory
should be used.

NOTE: module_dist and module_file are not yet supported, because (afaik)
there is no well known way to populate per-module share files. This may
change in the future. Please contact me if you know how to do this.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
