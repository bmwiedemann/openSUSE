#
# spec file for package dos2unix
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


Name:           dos2unix
Summary:        Text converters to and from DOS/MAC to UNIX
License:        BSD-2-Clause
Group:          Productivity/Text/Convertors
Version:        7.4.0
Release:        0
Url:            http://waterlan.home.xs4all.nl/dos2unix.html
Source:         http://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz
Provides:       unix2dos = %{version}
Obsoletes:      unix2dos < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
make %{?_smp_mflags} CC="%{__cc}" HTMLEXT="html"

%install
%makeinstall docdir=%{_defaultdocdir}/%{name} HTMLEXT="html"
%{find_lang} dos2unix --all-name --with-man

%files -f dos2unix.lang
%defattr(-,root,root,0755)
%doc %{_defaultdocdir}/%{name}
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2mac
%{_bindir}/unix2dos
%doc %{_mandir}/*/dos2unix.1*
%doc %{_mandir}/*/mac2unix.1*
%doc %{_mandir}/*/unix2mac.1*
%doc %{_mandir}/*/unix2dos.1*
%doc %lang(de) %dir %_mandir/de
%doc %lang(es) %dir %_mandir/es
%doc %lang(fr) %dir %_mandir/fr
%doc %lang(nl) %dir %_mandir/nl
%doc %lang(pl) %dir %_mandir/pl
%doc %lang(pt_BR) %dir %_mandir/pt_BR
%doc %lang(sv) %dir %_mandir/sv
%doc %lang(uk) %dir %_mandir/uk
%doc %lang(zh_CN) %dir %_mandir/zh_CN

%changelog
