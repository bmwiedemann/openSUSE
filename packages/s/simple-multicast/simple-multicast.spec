#
# spec file for package simple-multicast
#
# Copyright (c) 2020 SUSE LLC
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


Name:           simple-multicast
Version:        0.2.4
Release:        0
Summary:        Multicast Server and Client application
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://sourceforge.net/projects/simplemulticast/
Source:         http://sourceforge.net/projects/simplemulticast/files/%{version}/multicast-%{version}.zip
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  unzip

%description
Simple multicast Server/Client application.
Supports:

 * IPv4 AND IPv6
 * Multicast Server
 * Multicast client
 * Source Specific Multicast client

%prep
%setup -q -n multicast-%{version}

%build
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc/multicast

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_bindir}/multicast

%changelog
