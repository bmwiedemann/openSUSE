#
# spec file for package mpop
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Fabrice Bauzac.
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


%global _description %{expand:
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a
very fast POP3 implementation, many authentication methods, good
TLS/SSL support, IPv6 support, and more.
}
%bcond_with gnome-keyring
Name:           mpop
Version:        1.4.18
Release:        0
Summary:        Lightweight and featureful POP3 Client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://marlam.de/mpop/
Source:         https://marlam.de/mpop/releases/mpop-%{version}.tar.xz
BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  libsecret-devel
BuildRequires:  pkgconfig
# For an unknown reason, rpmlint says:
#
#   invalid-suse-version-check 1315
#
# However, this suse_version value is actually documented in
# https://en.opensuse.org/openSUSE:Packaging_for_Leap.  Which is
# correct, rpmlint or the documentation?
%if 0%{?suse_version} > 1315
BuildRequires:  libgnutls-devel
%else
# mpop recommends gnutls over openssl:
#
#   configure: WARNING: Using OpenSSL is discouraged; consider using GnuTLS instead
#
# However, it requires gnutls >= 3.4 while SLE-12 only has 3.2.15.
#
# I see two solutions in the case of SLE-12:
# - switch to openssl
# - try using SLE-12-SP5 which might have a newer version of gnutls
#
# Let's opt for the first solution: openssl.
BuildRequires:  libopenssl-devel
%endif
%if %{with gnome-keyring}
BuildRequires:  pkgconfig(gnome-keyring-1)
%endif

%description %{_description}

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc %{_description}

This package contains documentation and sample configuration files.

%prep
%setup -q

%build
%if 0%{?suse_version} > 1000
export CFLAGS="%{optflags} -fstack-protector"
%endif

%if 0%{?suse_version} > 1315
tls_lib=gnutls
%else
tls_lib=openssl
%endif

%configure --with-tls=$tls_lib --with-libgsasl --docdir="%{_docdir}/%{name}"
%make_build -O

%install
%make_install V=1
%find_lang %{name}

for f in \
COPYING \
; do
    ff="${f##*/}"
    install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
done

echo -n >docfiles.lst
for f in \
AUTHORS ChangeLog* NEWS README* THANKS NOTES \
doc/*.example \
; do
    ff="${f##*/}"
    install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
    echo "%doc %{_docdir}/%{name}/$ff" >>docfiles.lst
done

%files -f %{name}.lang
%doc %dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/COPYING
%{_bindir}/mpop
%{_bindir}/mpopd
%{_infodir}/mpop.info%{?ext_info}
%{_mandir}/man1/mpop.1%{?ext_man}
%{_mandir}/man1/mpopd.1%{?ext_man}

%files doc -f docfiles.lst

%changelog
