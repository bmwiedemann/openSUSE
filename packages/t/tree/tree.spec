#
# spec file for package tree
#
# Copyright (c) 2024 SUSE LLC
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


Name:           tree
Version:        2.2.1
Release:        0
Summary:        File listing as a tree
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://oldmanprogrammer.net/tar/tree/
Source0:        https://oldmanprogrammer.net/tar/tree/%{name}-%{version}.tgz

%description
Tree is a recursive directory listing command that produces a depth
indented listing of files, which is colorized ala dircolors if the
LS_COLORS environment variable is set and output is to tty.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?_lto_cflags}"
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc CHANGES README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
