#
# spec file for package unifdef
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           unifdef
Summary:        Removes ifdefs from C files
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        2.11
Release:        0
Url:            http://dotat.at/prog/unifdef/
Source:         http://dotat.at/prog/unifdef/unifdef-%{version}.tar.xz
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unifdef is useful for removing ifdef'ed lines from a file while otherwise
leaving the file alone.  Unifdef acts on #ifdef, #ifndef, #else, and #endif
lines, and it knows only enough about C to know when one of these is
inactive because it is inside a comment, or a single or double quote.



%prep
%setup -q
sed -i Makefile \
	-e 's,^\(prefix\).*=.*,\1 =\t%{_prefix},' \
	-e 's,^\(bindir\).*=.*,\1 =\t%{_bindir},' \
	-e 's,^\(mandir\).*=.*,\1 =\t%{_mandir},'

%build
make CFLAGS="%optflags"

%check
make test

%install
%{?make_install} %{!?make_install:make install DESTDIR=%{buildroot}}

%files
%defattr(-,root,root)
%{_bindir}/unifdef
%{_bindir}/unifdefall
%{_mandir}/man1/unifdef.1*
%{_mandir}/man1/unifdefall.1*
%doc Changelog COPYING README

%changelog
