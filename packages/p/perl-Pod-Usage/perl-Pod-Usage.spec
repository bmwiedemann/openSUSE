#
# spec file for package perl-Pod-Usage
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


Name:           perl-Pod-Usage
Version:        2.01
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
%define cpan_name Pod-Usage
Summary:        Extracts POD documentation and shows usage information
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Pod::Perldoc) >= 3.28
BuildRequires:  perl(Pod::Simple) >= 3.40
BuildRequires:  perl(Pod::Text) >= 4.00
Requires:       perl(Pod::Perldoc) >= 3.28
Requires:       perl(Pod::Simple) >= 3.40
Requires:       perl(Pod::Text) >= 4.00
%{perl_requires}

%description
*pod2usage* will print a usage message for the invoking script (using its
embedded pod documentation) and then exit the script with the desired exit
status. The usage message printed may have any one of three levels of
"verboseness": If the verbose level is 0, then only a synopsis is printed.
If the verbose level is 1, then the synopsis is printed along with a
description (if present) of the command line options and arguments. If the
verbose level is 2, then the entire manual page is printed.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
VERSION=$(echo %{version} | sed -e "s|\.|_|g")
pushd %buildroot%_bindir >/dev/null
for file in *; do
    mv -v $file $file-${VERSION}
done
popd >/dev/null
pushd %buildroot%_mandir/man1
for file in *.1; do
    mv -v $file ${file/.1/}-${VERSION}.1
done
popd >/dev/null
pushd %buildroot%_mandir/man3
for file in *.3pm; do
    mv -v $file ${file/.3pm/}-${VERSION}.3pm
done
popd >/dev/null
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
