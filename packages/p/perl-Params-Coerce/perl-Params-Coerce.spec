#
# spec file for package perl-Params-Coerce
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Params-Coerce
Version:        0.14
Release:        0
%define cpan_name Params-Coerce
Summary:        Allows your classes to do coercion of parameters
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Params-Coerce/
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Params::Util) >= 0.05
Requires:       perl(Params::Util) >= 0.05
%{perl_requires}

%description
A big part of good API design is that we should be able to be flexible in
the ways that we take parameters.

Params::Coerce attempts to encourage this, by making it easier to take a
variety of different arguments, while adding negligable additional
complexity to your code.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
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
