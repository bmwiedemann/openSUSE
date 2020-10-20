#
# spec file for package dos2unix
#
# Copyright (c) 2020 SUSE LLC
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
Version:        7.4.2
Release:        0
Summary:        Text converters to and from DOS/MAC to UNIX
License:        BSD-2-Clause
Group:          Productivity/Text/Convertors
URL:            https://waterlan.home.xs4all.nl/dos2unix.html
Source:         https://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz
Source2:        https://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz.asc
# http://keys.gnupg.net/pks/lookup?op=get&search=0x38C1F572B12725BE
Source3:        %{name}.keyring
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

%files -f dos2unix.lang
%defattr(-,root,root,0755)
%doc %{_defaultdocdir}/%{name}
%{_bindir}/*
%{_mandir}/*/*.1%{?ext_man}
%doc %lang(de) %dir %{_mandir}/de
%doc %lang(es) %dir %{_mandir}/es
%doc %lang(fr) %dir %{_mandir}/fr
%doc %lang(nl) %dir %{_mandir}/nl
%doc %lang(pl) %dir %{_mandir}/pl
%doc %lang(pt_BR) %dir %{_mandir}/pt_BR
%doc %lang(sv) %dir %{_mandir}/sv
%doc %lang(uk) %dir %{_mandir}/uk
%doc %lang(zh_CN) %dir %{_mandir}/zh_CN

%changelog
