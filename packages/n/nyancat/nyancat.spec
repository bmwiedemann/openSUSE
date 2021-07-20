#
# spec file for package nyancat
#
# Copyright (c) 2021 SUSE LLC
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


Name:           nyancat
Version:        1.5.2
Release:        0
Summary:        The flying rainbow cat rendered in a terminal
License:        NCSA
Group:          Amusements/Toys/Other
URL:            https://github.com/klange/nyancat
Source:         %{URL}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         add_destdir.patch

%description
nyancat is an animated ANSI/xterm-88 color text program that renders a loop of
the classic Nyan Cat animation. It includes a telnet server.

%prep
%autosetup -p0

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
