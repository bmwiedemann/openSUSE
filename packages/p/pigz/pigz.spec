#
# spec file for package pigz
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pigz
Version:        2.4
Release:        0
Summary:        Multi-core gzip version
License:        Zlib
Group:          Productivity/Archiving/Compression
URL:            http://www.zlib.net/pigz/
Source0:        http://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  zlib-devel

%description
A parallel implementation of gzip for modern multi-processor, multi-core machines

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%check
make tests %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -Dpm 0755 pigz \
  %{buildroot}%{_bindir}/pigz
install -Dpm 0644 pigz.1 \
  %{buildroot}%{_mandir}/man1/pigz.1
ln -sv pigz %{buildroot}%{_bindir}/unpigz

%files
%doc README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_mandir}/man1/pigz.1%{?ext_man}

%changelog
