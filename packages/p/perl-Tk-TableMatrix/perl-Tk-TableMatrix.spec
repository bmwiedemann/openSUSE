#
# spec file for package perl-Tk-TableMatrix
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


%define cpan_name Tk-TableMatrix
Name:           perl-Tk-TableMatrix
Version:        1.29
Release:        0
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND TCL
Summary:        Table/Matrix Widget Extension to perl/tk
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(Tk) >= 800.022
BuildRequires:  perl(Tk::MMutil)
Requires:       perl(Tk) >= 800.022
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl-Tk-devel
BuildRequires:  xorg-x11-devel
# MANUAL END

%description
Tk::TableMatrix is a table/matrix widget extension to perl/tk
for displaying data in a table (or spreadsheet) format.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
if test "%{_lib}" = "lib64" ; then
  sed -i -e "s,/lib>,/lib64>," -e "s,/lib\",/lib64\"," myConfig
fi
# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' ChangeLog Changes README demos/*

# Copy license
cp -a pTk/license.terms license.terms.pTk
cp -a pTk/mTk/license.terms license.terms.mTk
# MANUAL END

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
%doc ChangeLog Changes demos README
%license COPYING license.terms.mTk license.terms.pTk
%exclude %{perl_vendorarch}/auto/Tk/pTk

%changelog
