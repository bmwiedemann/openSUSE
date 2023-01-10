#
# spec file for package perl-libintl-perl
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


%define cpan_name libintl-perl
Name:           perl-libintl-perl
Version:        1.33
Release:        0
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        GPL-3.0-or-later
Summary:        High-Level Interface to Uniforum Message Translation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIDO/%{cpan_name}-%{version}.tar.gz
Source1:        libintl-perl-rpmlintrc
Source2:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(version) >= 0.77
Requires:       perl(version) >= 0.77
Recommends:     perl(File::ShareDir)
%{perl_requires}
# MANUAL BEGIN
Requires:       gettext-runtime >= 0.12.2
# MANUAL END

%description
This is an internationalization library for Perl that aims to be
compatible with the Uniforum message translations system as implemented
for example in GNU gettext.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Credits FAQ NEWS README README.md README-oldversions README.solaris README.win32 REFERENCES THANKS TODO
%license COPYING

%changelog
