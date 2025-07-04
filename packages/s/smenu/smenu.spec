#
# spec file for package smenu
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


Name:           smenu
Version:        1.5.0
Release:        0
Summary:        A standard input word picker
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/p-gen/%{name}
Source:         https://github.com/p-gen/smenu/releases/download/v%{version}/smenu-%{version}.tar.bz2
# https://github.com/p-gen/smenu/issues/46
BuildRequires:  ncurses-devel

%description
This tool reads words from a file or standard input, presents them in an
interactive window after the current line on the terminal, and writes the
selected words, if any, to standard output.

%prep
%autosetup -p1

%build
%configure
%if (0%{?sle_version} >= 150000 && !0%{?is_opensuse})
    || (0%{?suse_version} >= 150000 && 0%{?is_opensuse})
    || (0%{?rhel_version} > 600)
%make_build
%else
make %{?_smp_mflags}
%endif

%package tests
Summary:        Testing system for %{name}
Group:          Productivity/Text/Utilities
Requires:       smenu
BuildArch:      noarch

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
%doc tests

%files
%attr(0755,root,root) %{_bindir}/*
%if 0%{?sle_version} < 120300
%doc COPYRIGHT
%else
%license COPYRIGHT
%endif
%doc examples README.rst FAQ
%{_mandir}/man1/*

%changelog
