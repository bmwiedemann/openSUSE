#
# spec file for package dex
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


Name:           dex
Version:        0.7
Release:        0
Summary:        DesktopEntry Execution
License:        GPL-3.0+
Group:          System/X11/Utilities
Url:            https://github.com/jceb/dex
Source:         https://github.com/jceb/dex/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3-Sphinx
Requires:       python3
BuildArch:      noarch

%description
A simple utility to handle XDG autostart entries.

%prep
%setup -q

%build
make %{?_smp_mflags} V=1

%install
%make_install \
  PREFIX=%{_prefix}            \
  DOCPREFIX=%{_docdir}/%{name} \
  MANPREFIX=%{_mandir}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
