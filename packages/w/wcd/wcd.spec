#
# spec file for package wcd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        6.0.3
Release:        0
Summary:        Chdir for DOS and Unix
License:        GPL-2.0-only
Group:          Productivity/File utilities
Url:            http://waterlan.home.xs4all.nl/
Source:         http://waterlan.home.xs4all.nl/wcd/%{name}-%{version}.tar.gz
BuildRequires:  gettext-runtime
BuildRequires:  gettext-tools
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1310
BuildRequires:  libunistring-devel
%endif

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
make -C src %{?_smp_mflags} prefix=%{_prefix} \
%if 0%{?suse_version} >= 1310
  UNINORM=1 \
%endif
  UCS=1

%install
make -C src install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} docdir=%{wcd_docdir} bindir=%{_libexecdir}
make -C src install-profile DESTDIR=%{buildroot} prefix=%{_prefix} sysconfdir=%{_sysconfdir} bindir=%{_libexecdir}

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_mandir}/man1/wcd.*
%doc %lang(de) %dir %{_mandir}/de
%doc %lang(fr) %dir %{_mandir}/fr
%doc %lang(nl) %dir %{_mandir}/nl
%doc %lang(pt_BR) %dir %{_mandir}/pt_BR
%doc %lang(uk) %dir %{_mandir}/uk
%doc %{wcd_docdir}
%{_libexecdir}/wcd.exe
# Overwrite the old config files. Old config files may break a new
# installation when the name of the binary changes.
%config %{_sysconfdir}/profile.d/wcd.*

%changelog
