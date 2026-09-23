#
# spec file for package joe
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


Name:           joe
Version:        4.8
Release:        0
Summary:        A Text Editor
License:        GPL-2.0-or-later
URL:            https://joe-editor.sourceforge.net
Source:         https://downloads.sf.net/joe-editor/%{name}-%{version}.tar.gz
Patch2:         joe-3.1-fix_isblanck_argument.patch
Patch3:         joe-3.3-warnings.patch
Patch10:        joe-sigiot.patch
Patch12:        joe-4.6-nonvoid-functions.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(ncurses)

%description
Joe is a powerful, easy to use, modeless text editor. It uses the same
WordStar keybindings used in Borland's development environment.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -W -Wno-unused"
%configure \
  --docdir=%{_defaultdocdir}/%{name}
%make_build

%install
%make_install
for i in jmacs jpico jstar rjoe; do
  ln -s joe.1.gz %{buildroot}%{_mandir}/man1/$i.1.gz
done

# Console app: no .desktop (opensuse-factory 2019-02/msg00377)
rm -rf %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%dir %{_sysconfdir}/joe
%config(noreplace) %{_sysconfdir}/joe/*
%dir %{_datadir}/%{name}
%dir %{_mandir}/ru
%dir %{_mandir}/ru/man1
%{_bindir}/joe
%{_bindir}/jmacs
%{_bindir}/jpico
%{_bindir}/jstar
%{_bindir}/rjoe
%{_datadir}/%{name}/charmaps
%dir %{_datadir}/%{name}/syntax
%{_datadir}/%{name}/syntax/*
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/colors

%changelog
