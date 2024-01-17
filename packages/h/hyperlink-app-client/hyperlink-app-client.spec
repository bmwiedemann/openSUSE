#
# spec file for package hyperlink-app-client
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


%define commit  211516ea81e9459c0056ade52e991c09ade2909e
Name:           hyperlink-app-client
Version:        0.0~git5.211516e
Release:        0
Summary:        Handler program for the app protocol
License:        GPL-3.0-or-later
URL:            https://gitlab.com/darnir/%{name}
Source0:        https://gitlab.com/darnir/%{name}/-/archive/%{commit}/%{name}-%{version}.tar.bz2
Source1:        app-client.desktop

%description
The app protocol defines the behaviour of a terminal emulator when opening a
'app://' hyperlink.

The behaviour is basically to send via TCP/IP the given command to the given
hostname and port.

This behaviour can be extracted in a separate program. A terminal emulator
can simply invoke this program, passing it the URI on standard input. This way,
the protocol logic does not need to be hardwired into any terminal emulator.

This package contains the reference implementation of such a handler program.

%prep
%setup -q -n %{name}-%{commit}

%build
%set_build_flags
%make_build

%install
install -D --target-directory %{buildroot}%{_bindir} --mode 0755 app-client
install -D --target-directory %{buildroot}%{_datadir}/applications --mode 0644 %{SOURCE1}

%files
%license LICENSE
%doc README
%{_bindir}/app-client
%{_datadir}/applications/app-client.desktop

%changelog