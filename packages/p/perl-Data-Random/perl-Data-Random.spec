#
# spec file for package perl-Data-Random
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Random
Version:        0.13
Release:        0
%define cpan_name Data-Random
Summary:        Perl module to generate random data
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Random/
Source0:        https://cpan.metacpan.org/authors/id/B/BA/BAREFOOT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Piece) >= 1.16
Requires:       perl(Time::Piece) >= 1.16
Recommends:     perl(GD)
%{perl_requires}

%description
A module used to generate random data. Useful mostly for test programs.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

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
%doc Changes README
%license LICENSE

%changelog
