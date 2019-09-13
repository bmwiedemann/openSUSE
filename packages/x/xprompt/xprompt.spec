#
# spec file for package xprompt
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xprompt
%define _prefix %(pkg-config --variable prefix x11 || echo /usr/X11R6)
%if "%_prefix" == "/usr/X11R6"
%define _mandir %_prefix/man
%endif
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
Version:        91.9.28
Release:        0
Summary:        Small tool for prompting users
License:        BSD-3-Clause
Group:          System/X11/Utilities
Source:         xprompt-28sep91.tar.gz
Patch:          warn.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Small tool to ask the user for one or more responses (e.g., from batch
files).



Authors:
--------
    Barry Brachman <brachman@cs.ubc.ca>

%prep
%setup -n xprompt-28sep91
%patch

%build
xmkmf -a
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install install.man

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/man1/*

%changelog
