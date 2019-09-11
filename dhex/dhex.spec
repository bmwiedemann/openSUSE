#
# spec file for package dhex
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dhex
Version:        0.69
Release:        0
Summary:        Hexeditor with a Diff-mode for ncurses
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://www.dettus.net/dhex/
Source0:        http://www.dettus.net/%{name}/%{name}_%{version}.tar.gz
Source1:        dhex-themes.tar.bz2
BuildRequires:  ncurses-devel

%description
DHEX is just another Hexeditor with a Diff mode for ncurses. It makes
heavy use of colors and is themeable.

%prep
%setup -qn %{name}_%{version} -a1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -std=c99"

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -dm 0755 %{buildroot}%{_mandir}/{man1,man5}
install -pm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/
install -pm 0644 %{name}*.5 %{buildroot}%{_mandir}/man5/

%files
%license gpl.txt
%doc README.txt themes todo.txt
%{_bindir}/%{name}
%{_mandir}/man?/*

%changelog
