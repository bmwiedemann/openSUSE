#
# spec file for package perl-Cairo
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


Name:           perl-Cairo
Version:        1.106
Release:        0
%define cpan_name Cairo
Summary:        Perl interface to the cairo 2d vector graphics library
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Cairo/
Source0:        http://www.cpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1
Requires:       perl(ExtUtils::Depends) >= 0.2
Requires:       perl(ExtUtils::PkgConfig) >= 1
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(cairo)
# MANUAL END

%description
Perl interface to the cairo 2d vector graphics library

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test || :

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc cairo-perl.typemap ChangeLog.pre-git doctypes examples LICENSE NEWS perl-Cairo.doap README TODO

%changelog
