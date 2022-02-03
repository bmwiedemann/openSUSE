#
# spec file for package dtach
#
# Copyright (c) 2022 SUSE LLC
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


Name:           dtach
Version:        0.9+2.748020b
Release:        0
Summary:        Background processes and reattach to them
License:        GPL-2.0-or-later
Group:          System/Console
URL:            http://dtach.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
Patch0:         dtach-remove-date-time-compile-macros.patch

%description
dtach wraps a command in a sort of process container with new
terminal device and session, allowing to "detach" from it,
essentially backgrounding the process, and later re-attach to it,
similar to the eponymous feature of GNU screen.

dtach avoids interpreting most of the input and output between attached
terminals and the program under its control. Though multi display mode (like
screen -x) is available, different terminal types or even sizes are not
handled.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
install -D -p -m 755 %{name} \
    %{buildroot}/%{_bindir}/%{name}
install -D -p -m 644 %{name}.1 \
    %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
