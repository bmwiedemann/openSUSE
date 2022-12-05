#
# spec file for package uacme
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           uacme
Version:        1.7.3
Release:        0
Summary:        A minimal ACMEv2 client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/ndilieto/uacme
Source:         https://github.com/ndilieto/uacme/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE suse-www-path.patch
# find . -type f -exec sed -i 's|/var/www|/srv/www/htdocs|g' {} \;
Patch1:         suse-www-path.patch
Patch2:         %{name}-fix-incorrect-return-types.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls) >= 3.3.30
BuildRequires:  pkgconfig(libcurl) >= 7.38.0

%description
uacme is a client for the ACMEv2 protocol described in RFC8555,
written in plain C code with minimal dependencies.
The ACMEv2 protocol allows a Certificate Authority and an
applicant to automate the process of verification and certificate
issuance. The protocol also provides facilities for other
certificate management functions, such as certificate revocation.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
mv %{buildroot}/%{_datadir}/doc/uacme/*.html .

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.md THANKS
%doc uacme.html ualpn.html
%{_bindir}/uacme
%{_bindir}/ualpn
%{_mandir}/man1/uacme.1%{?ext_man}
%{_mandir}/man1/ualpn.1%{?ext_man}
%dir %{_datadir}/uacme
%{_datadir}/uacme/uacme.sh
%{_datadir}/uacme/ualpn.sh
%{_datadir}/uacme/nsupdate.sh

%changelog
