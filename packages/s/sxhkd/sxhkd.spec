#
# spec file for package sxhkd
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Luke Jones, luke.nukem.jones@gmail.com
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


Name:           sxhkd
Version:        0.6.1
Release:        0
Summary:        Simple X hotkey daemon
License:        BSD-2-Clause
Group:          System/GUI/Other
URL:            https://github.com/baskerville/sxhkd
Source0:        https://github.com/baskerville/sxhkd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/baskerville/bspwm/master/examples/sxhkdrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)

%description
sxhkd is a simple X hotkey daemon with a powerful and compact configuration syntax.

%prep
%setup -q

%build
export CPPFLAGS="%{optflags} -fcommon"
make %{?_smp_mflags} 

%install
%make_install PREFIX=%{_prefix} DOCPREFIX=%{_docdir}/%{name}
install -D -p -m 644 %{SOURCE1} \
        %{buildroot}%{_sysconfdir}/skel/.config/sxhkd/sxhkdrc

%files
%license LICENSE
%{_bindir}/sxhkd
%{_mandir}/man1/sxhkd.1%{?ext_man}
%{_docdir}/%{name}
%{_sysconfdir}/skel/.config/sxhkd
%config %{_sysconfdir}/skel/.config/sxhkd/sxhkdrc

%changelog
