#
# spec file for package wcd
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define wcd_docdir %{_defaultdocdir}/%{name}
Name:           wcd
Version:        6.0.7
Release:        0
Summary:        Chdir for DOS and Unix
License:        GPL-2.0-only
URL:            https://waterlander.net/wcd/
Source:         https://waterlander.net/wcd/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gettext-runtime
BuildRequires:  gettext-tools
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncursesw)

%description
Wcd.   Directory changer for DOS and Unix.  Another Norton
Change Directory (NCD) clone.

Wcd is a command-line program to change directory fast. It
saves time typing at the keyboard.  One needs to type only
a part of a directory  name and wcd  will jump to it.  Wcd
has a fast selection  method  in  case of multiple matches
and allows aliasing and  banning of directories.  Wcd also
includes a full-screen interactive  directory tree browser
with speed search.

%prep
%setup -q

%build
%make_build -C src prefix=%{_prefix} \
  UNINORM=1 \
  UCS=1

%install
make -C src install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} docdir=%{wcd_docdir} bindir=%{_libexecdir}
make -C src install-profile DESTDIR=%{buildroot} prefix=%{_prefix} sysconfdir=%{_sysconfdir} bindir=%{_libexecdir}

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%{_mandir}/man1/wcd.*
%doc %lang(de) %dir %{_mandir}/de
%doc %lang(fr) %dir %{_mandir}/fr
%doc %lang(nl) %dir %{_mandir}/nl
%doc %lang(pt_BR) %dir %{_mandir}/pt_BR
%doc %lang(ro) %dir %{_mandir}/ro
%doc %lang(sr) %dir %{_mandir}/sr
%doc %lang(sv) %dir %{_mandir}/sv
%doc %lang(uk) %dir %{_mandir}/uk
%doc %{wcd_docdir}
%{_libexecdir}/wcd.exe
# Overwrite the old config files. Old config files may break a new
# installation when the name of the binary changes.
%config %{_sysconfdir}/profile.d/wcd.*

%changelog
