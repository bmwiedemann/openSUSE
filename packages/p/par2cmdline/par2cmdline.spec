#
# spec file for package par2cmdline
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


Name:           par2cmdline
Version:        0.8.1
Release:        0
Summary:        A PAR 2.0 compatible file creation, verification, and repair tool
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://github.com/Parchive/par2cmdline
Source:         https://github.com/Parchive/par2cmdline/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
# The following 2 provides/obsoletes lines have been added becase at one point
# the 'par' package was updated to use the 'par2cmdline' sources. Any package
# that depends on 'par' version 0.8.0 should actually depend on 'par2cmdline'
# version 0.8.0.  The last/latest version of 'par' package should be 1.1 which
# makes this "relatively" safe to do.
Provides:       par = 0.8.0
Obsoletes:      par < 0.8.0
Provides:       par2 = %{version}

%description
par2cmdline is a program for creating and using PAR2 files to detect damage in
data files and repair them if necessary. It can be used with any kind of file.

%prep
%setup -q
# Remove executable permission from text files
chmod -x ChangeLog configure.ac INSTALL Makefile.am NEWS stamp-h.in

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1%{?ext_man}

%changelog
