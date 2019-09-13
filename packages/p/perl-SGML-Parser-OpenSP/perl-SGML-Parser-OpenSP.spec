#
# spec file for package perl-SGML-Parser-OpenSP
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-SGML-Parser-OpenSP
%define cpan_name SGML-Parser-OpenSP
Summary:        Perl interface to the OpenSP SGML and XML parser
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Version:        0.994
Release:        0
Url:            http://search.cpan.org/dist/SGML-Parser-OpenSP
Source0:        %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  opensp-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Class::Accessor)

%description
SGML::Parser::OpenSP provides a native Perl interface, written in C++
and XS, to the OpenSP SGML and XML parser.

 Authors:	Bjoern Hoehrmann, <bjoern@hoehrmann.de>

%prep
%setup -q -n %{cpan_name}-%{version}
find -type f -exec chmod 0644 {} \;
find -type d -exec chmod 0755 {} \;
for i in Changes README lib/SGML/Parser/OpenSP/Tools.pm lib/SGML/Parser/OpenSP.pm; do
  dos2unix $i
done

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes README

%changelog
