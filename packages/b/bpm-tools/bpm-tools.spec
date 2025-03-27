#
# spec file for package bpm-tools
#
# Copyright (c) 2025 SUSE LLC
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


Name:           bpm-tools
Version:        0.3
Release:        0
Summary:        Automatic calculating and tagging the tempo of music files
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://www.pogo.org.uk/~mark/bpm-tools/
Source0:        http://www.pogo.org.uk/~mark/bpm-tools/releases/%{name}-%{version}.tar.gz
Patch0:         bpm-graph-so-reference.patch
Requires:       gnuplot
Requires:       sox
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Automatic calculating and tagging the tempo (in beats-per-minute) of music files.

%prep
%autosetup -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{_prefix}
chmod -x %{buildroot}%{_mandir}/man1/*

%files
%defattr(-,root,root,-)
%license COPYING
%doc README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
