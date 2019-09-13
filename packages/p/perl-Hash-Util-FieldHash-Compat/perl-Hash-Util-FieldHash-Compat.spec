#
# spec file for package perl-Hash-Util-FieldHash-Compat
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Hash-Util-FieldHash-Compat
Version:        0.11
Release:        0
%define cpan_name Hash-Util-FieldHash-Compat
Summary:        Use Hash::Util::FieldHash or ties, depending on availability
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Hash-Util-FieldHash-Compat/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
Under older perls this module provides a drop-in compatible API to
Hash::Util::FieldHash using perltie. When Hash::Util::FieldHash is
available it will use that instead.

This way code requiring field hashes can benefit from fast, robust field
hashes on Perl 5.10 and newer, but still run on older perls that don't ship
with that module.

See Hash::Util::FieldHash for all the details of the API.

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
