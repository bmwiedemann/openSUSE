#
# spec file for package whois
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


Name:           whois
Version:        5.5.15
Release:        0
Summary:        Intelligent WHOIS client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/rfc1036/whois
Source:         https://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.tar.xz
Source2:        https://ftp.debian.org/debian/pool/main/w/whois/%{name}_%{version}.dsc#/%{name}.asc
Source3:        https://db.debian.org/fetchkey.cgi?fingerprint=6791403B68AE2690517C42EAE6FFF1E38DC968B0#/%{name}.keyring
Patch0:         whois-nobsdsource.patch
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(libidn2)
Provides:       ripe-whois-tools
%{perl_requires}
%if 0%{?suse_version} != 1310
BuildRequires:  perl(autodie)
%endif

%description
This package provides a commandline client for the WHOIS (RFC 3912)
protocol, which queries online servers for information such as contact
details for domains and IP address assignments.
It can intelligently select the appropriate WHOIS server for most queries.

The package also contains mkpasswd, a features-rich front end to the
password encryption function crypt(3).

%prep
# the signature is on the Debian .dsc. Extract the checksums and verify against source
echo "`grep -A1 "Files:" %{SOURCE2} | grep %{name}_%{version}.tar.xz | cut -d\  -f2`  %{SOURCE0}" | md5sum -c
echo "`grep -A1 "Checksums-Sha1" %{SOURCE2} | grep %{name}_%{version}.tar.xz | cut -d\  -f2`  %{SOURCE0}" | sha1sum -c
echo "`grep -A1 "Checksums-Sha256" %{SOURCE2} | grep %{name}_%{version}.tar.xz | cut -d\  -f2`  %{SOURCE0}" | sha256sum -c

%setup -q -n %{name}
%patch0 -p1

%build
%make_build all mkpasswd HAVE_LIBIDN2=1 HAVE_ICONV=1 \
%if 0%{?suse_version} <= 1140
	HAVE_XCRYPT=1 \
%else
	HAVE_CRYPT_GENSALT=1 \
%endif
	CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}{%{_prefix}/bin,%{_mandir}/man1}
make BASEDIR=%{buildroot} mandir=%{_mandir} prefix=%{_prefix} \
	install install-mkpasswd install-pos
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README debian/changelog
%{_bindir}/mkpasswd
%{_bindir}/whois
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}

%changelog
