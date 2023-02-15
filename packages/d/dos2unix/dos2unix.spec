#
# spec file for package dos2unix
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           dos2unix
Version:        7.4.4
Release:        0
Summary:        Text converters to and from DOS/MAC to UNIX
License:        BSD-2-Clause
Group:          Productivity/Text/Convertors
URL:            https://waterlan.home.xs4all.nl/dos2unix.html
Source0:        https://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz
Source1:        https://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz.asc
# http://keys.gnupg.net/pks/lookup?op=get&search=0x38C1F572B12725BE
Source2:        %{name}.keyring
Provides:       unix2dos = %{version}
Obsoletes:      unix2dos < %{version}

%description
Dos2unix is used to convert plain text from DOS (CR/LF) format. Mac2unix
converts plain text from MAC (CR) format to UNIX format (LF).

Unix2dos converts plain text files from UNIX
format to DOS format and unix2dos converts from UNIX to MAC format.

%prep
%setup -q
find . -type f -exec chmod -x '{}' +

%build
export RPM_OPT_FLAGS
%make_build CC="gcc" HTMLEXT="html"

%install
%make_install docdir=%{_defaultdocdir}/%{name} HTMLEXT="html"
%find_lang dos2unix --all-name --with-man
rm %{buildroot}%{_defaultdocdir}/%{name}/COPYING.txt

%files -f dos2unix.lang
%license COPYING.txt
%doc %{_defaultdocdir}/%{name}
%{_bindir}/{%{name},mac2unix,unix2dos,unix2mac}
%{_mandir}/man1/{%{name},mac2unix,unix2dos,unix2mac}.1%{?ext_man}
%dir %{_mandir}/??

%changelog
