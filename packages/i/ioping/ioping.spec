#
# spec file for package ioping
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


Name:           ioping
Version:        1.3
Release:        0
Summary:        A tool to monitor I/O latency in real time
License:        GPL-3.0-or-later
Group:          System/Benchmark
URL:            https://github.com/koct9i/ioping
Source:         https://github.com/koct9i/ioping/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
A tool to monitor I/O latency in real time. It shows disk latency in the
same way as ping shows network latency.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags} -std=gnu99"

%install
install -D -p -m 0755 %{name} \
  %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md changelog
%{_bindir}/ioping
%{_mandir}/man1/ioping.1%{?ext_man}

%changelog
