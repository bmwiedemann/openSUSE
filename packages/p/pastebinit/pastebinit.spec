#
# spec file for package pastebinit
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


Name:           pastebinit
Version:        1.7.1
Release:        0
URL:            https://github.com/pastebinit/pastebinit
BuildRequires:  asciidoc
BuildRequires:  gettext-tools
BuildArch:      noarch
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz
# Patches submitted upstream:
# https://github.com/pastebinit/pastebinit/pull/13
Patch0:         0001-Default-to-paste.opensuse.org-when-on-suse.patch
Patch1:         0002-paste.opensuse.org-add-conf-for-openSUSE-paste.patch
Summary:        Script to Send Data to Pastebin Sites
License:        GPL-2.0-only
Group:          Productivity/Networking/Web/Utilities
Requires:       python3-distro

%description
This software lets you send a file or simply the result of a command directly
to the pastebin you want (if it's supported) and gives you the URL in return.

%prep
%setup -q
%autopatch -p1

%build
sed -e 's;#!/usr/bin/env python3;#!/usr/bin/python3;1' -i pastebinit
a2x -f manpage pastebinit.xml
%__make -C po/

%install
%__install -d %{buildroot}%{_datadir}/pastebin.d
%__install -m0644 pastebin.d/* %{buildroot}%{_datadir}/pastebin.d/
%__install -D -m0755 pastebinit %{buildroot}%{_bindir}/pastebinit
%__install -D -m0644 pastebinit.1 %{buildroot}%{_mandir}/man1/pastebinit.1
%__install -d %{buildroot}%{_datadir}/locale
%__cp -r po/mo/* %{buildroot}%{_datadir}/locale/
%__install -D README.md %{buildroot}%{_defaultdocdir}/%{name}/README.md

%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README.md
%license COPYING
%dir %{_datadir}/pastebin.d
%{_datadir}/pastebin.d/*.conf
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1%{ext_man}

%changelog
