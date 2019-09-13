#
# spec file for package lemonbar
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lemonbar
Version:        1.3
Release:        0
Summary:        An X11 bar
License:        MIT
Group:          System/GUI/Other
Url:            https://github.com/LemonBoy/bar
Source0:        https://github.com/LemonBoy/bar/archive/v%{version}.tar.gz
BuildRequires:  libxcb-devel

%description
lemonbar is a bar entirely based on XCB. It provides full UTF-8
support, basic formatting, RandR and Xinerama support and EWMH
compliance.

%prep
%setup -q -n bar-%{version}

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%defattr (-, root, root)
%doc LICENSE
%{_bindir}/lemonbar
%{_mandir}/man1/lemonbar.1%{ext_man}

%changelog
