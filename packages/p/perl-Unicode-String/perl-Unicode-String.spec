#
# spec file for package perl-Unicode-String
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


Name:           perl-Unicode-String
Version:        2.10
Release:        0
%define cpan_name Unicode-String
Summary:        String of Unicode characters (UTF-16BE)
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Unicode-String/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/GAAS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
A 'Unicode::String' object represents a sequence of Unicode characters.
Methods are provided to convert between various external formats
(encodings) and 'Unicode::String' objects, and methods are provided for
common string manipulations.

The functions utf32be(), utf32le(), utf16be(), utf16le(), utf8(), utf7(),
latin1(), uhex(), uchr() can be imported from the 'Unicode::String' module
and will work as constructors initializing strings of the corresponding
encoding.

The 'Unicode::String' objects overload various operators, which means that
they in most cases can be treated like plain strings.

Internally a 'Unicode::String' object is represented by a string of 2 byte
numbers in network byte order (big-endian). This representation is not
visible by the API provided, but it might be useful to know in order to
predict the efficiency of the provided methods.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
