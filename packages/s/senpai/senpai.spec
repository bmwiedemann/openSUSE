#
# spec file for <package name>
#
# Copyright (c) 2023 SUSE LLC
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


Name:           senpai
Version:        0.4.0
Release:        0
Summary:        Your everyday IRC student
License:        ISC
Group:          Productivity/Networking/Instant Messenger
URL:            https://sr.ht/~delthas/senpai
Source:         https://git.sr.ht/~delthas/senpai/archive/v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  scdoc
BuildRequires:  zstd

%description
senpai is an IRC client that works best with bouncers:

 * no logs are kept,
 * history is fetched from the server via CHATHISTORY,
 * networks are fetched from the server via bouncer-networks,
 * messages can be searched in logs via SEARCH,
 * files can be uploaded via FILEHOST (with drag & drop!)

%prep
%autosetup -p1 -a1 -n %{name}-v%{version}

%build
make GOFLAGS="-mod=vendor -buildmode=pie"

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -m0644 doc/%{name}.5 %{buildroot}%{_mandir}/man5/%{name}.5

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*%{?ext_man}

%changelog
