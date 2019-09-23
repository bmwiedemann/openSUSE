#
# spec file for package perl-Text-WrapI18N
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


Name:           perl-Text-WrapI18N
Version:        0.06
Release:        0
Summary:        Line Wrapping Module
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-WrapI18N
Source:         http://search.cpan.org/CPAN/authors/id/K/KU/KUBOTA/Text-WrapI18N-%{version}.tar.gz
BuildRequires:  perl-macros
BuildRequires:  perl(Text::CharWidth)
Requires:       perl(Text::CharWidth)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildArch:      noarch

%description
Line wrapping module with support for multibyte, fullwidth, and combining
characters and languages without whitespaces between words.

%prep
%setup -q -n "Text-WrapI18N-%{version}"
sed -i '/^auto_install/d' Makefile.PL

%build
perl Makefile.PL PREFIX="%{_prefix}"
make %{?_smp_flags}

%install
%perl_make_install
%perl_process_packlist

%check
make test

%clean
%{?buildroot:rm -rf %{buildroot}}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/Text
%{perl_vendorlib}/Text/WrapI18N.pm
%doc %{perl_man3dir}/Text::WrapI18N.%{perl_man3ext}%{ext_man}

%changelog
