#
# spec file for package perl-Data-Clone
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


Name:           perl-Data-Clone
Version:        0.004
Release:        0
%define cpan_name Data-Clone
Summary:        Polymorphic data cloning
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Clone/
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/%{cpan_name}-%{version}.tar.gz
Source1:        perl-Data-Clone-rpmlintrc
Source2:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires) >= 0.03
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
'Data::Clone' does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also with
blessed references (i.e. objects). When 'clone()' finds an object, it calls
a 'clone' method of the object if the object has a 'clone', otherwise it
makes a surface copy of the object. That is, this module does polymorphic
data cloning.

Although there are several modules on CPAN which can clone data, this
module has a different cloning policy from almost all of them. See Cloning
policy and Comparison to other cloning modules for details.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes example README

%changelog
