#
# spec file for package perl-Unicode-Map
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Unicode-Map
Version:        0.112
Release:        1
License:        GPL-2.0+ or Artistic-1.0
%define cpan_name Unicode-Map
Summary:        maps charsets from and to utf16 unicode
Url:            http://search.cpan.org/dist/Unicode-Map/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/M/MS/MSCHWARTZ/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module converts strings from and to 2-byte Unicode UCS2 format. All
mappings happen via 2 byte UTF16 encodings, not via 1 byte UTF8 encoding.
To transform these use Unicode::String.

For historical reasons this module coexists with Unicode::Map8. Please use
Unicode::Map8 unless you need to care for two byte character sets, e.g.
chinese GB2312. Anyway, if you stick to the basic functionality (see
documentation) you can use both modules equivalently.

Practically this module will disappear from earth sooner or later as
Unicode mapping support needs somehow to get into perl's core. If you like
to work on this field please don't hesitate contacting Gisle Aas!

This module can't deal directly with utf8. Use Unicode::String to convert
utf8 to utf16 and vice versa.

Character mapping is according to the data of binary mapfiles in
Unicode::Map hierarchy. Binary mapfiles can also be created with this
module, enabling you to install own specific character sets. Refer to
mkmapfile or file REGISTRY in the Unicode::Map hierarchy.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
%defattr(-,root,root,755)
%doc Changes COPYING README

%changelog
