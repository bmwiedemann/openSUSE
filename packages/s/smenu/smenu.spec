#
# spec file for package smenu
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


Name:           smenu
Version:        0.9.17
Release:        0
Summary:        A standard input word picker
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/p-gen/%{name}
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This tool reads words from a file or standard input, presents them in an
interactive window after the current line on the terminal, and writes the
selected words, if any, to standard output.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%package tests
Summary:        Testing system for %{name}
Group:          Productivity/Text/Utilities
Requires:       smenu

%description tests
This packages contains some scripts and a number of tests to check the
%{name} tool.

%install
%if 0%{?suse_version} < 1315
make install DESTDIR="%{?buildroot}"
%else
%make_install
%endif

%files tests
%defattr(-,root,root,-)
%doc tests

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/*
%if 0%{?sle_version} < 120300
%doc COPYRIGHT
%else
%license COPYRIGHT
%endif
%doc examples README.rst FAQ
%{_mandir}/man1/*

%changelog
