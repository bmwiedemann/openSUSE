#
# spec file for package enchive
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           enchive
Version:        3.5
Release:        0
Summary:        Long-term archive encryption tool
License:        Unlicense
Group:          Productivity/Networking/Security
URL:            https://github.com/skeeto/enchive
#Git-Clone:     https://github.com/skeeto/enchive.git
Source:         https://github.com/skeeto/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         enchive-obey-cflags.patch

%description
Enchive is a tool to encrypt files to yourself for long-term archival.
It's a focused, simple alternative to more complex solutions such as
GnuPG or encrypted filesystems.

Files are secured with ChaCha20, Curve25519, and HMAC-SHA256.

%prep
%setup -q
%patch0 -p1


%build
export CFLAGS='%{optflags}'
make %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%license UNLICENSE
%doc NEWS.md README.md
%{_bindir}/enchive
%{_mandir}/man1/enchive.1%{?ext_man}

%changelog
