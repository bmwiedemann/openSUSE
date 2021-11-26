#
# spec file for package mpop
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Fabrice Bauzac.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
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


%bcond_with gnome-keyring

Name:           mpop
Version:        1.4.14
Release:        0

# On SLE-12, this should be GPL-3.0+; if we indicate
# "GPL-3.0-or-later", rpmlint issues this warning:
#
#   invalid-license GPL-3.0-or-later
#
# However, I'm on a Tumbleweed 2021-11, and whenever I write
# "GPL-3.0+", something (what?) overwrites my .spec to replace the
# license with "GPL-3.0-or-later", and I don't know how to disable
# this annoying replacement.
#
# For now, I'm keeping "GPL-3.0-or-later", and I'll ignore the rpmlint
# warning....
License:        GPL-3.0-or-later

Group:          Productivity/Networking/Email/Utilities

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# For an unknown reason, rpmlint says:
#
#   invalid-suse-version-check 1315
#
# However, this suse_version value is actually documented in
# https://en.opensuse.org/openSUSE:Packaging_for_Leap.  Which is
# correct, rpmlint or the documentation?
%if %suse_version > 1315
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

BuildRequires:  libgsasl-devel
BuildRequires:  libidn-devel
BuildRequires:  libsecret-devel
BuildRequires:  pkgconfig
%if %{with gnome-keyring}
BuildRequires:  pkgconfig(gnome-keyring-1)
%endif
URL:            https://marlam.de/mpop/
Source:         https://marlam.de/mpop/releases/mpop-1.4.14.tar.xz

Summary:        Lightweight and featureful POP3 Client

%global _description %{expand:
mpop is a small and fast POP3 client. Features include mail filtering,
delivery to mbox files, maildir folders or a mail delivery agent, a
very fast POP3 implementation, many authentication methods, good
TLS/SSL support, IPv6 support, and more.
}

%description %_description

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc %_description

This package contains documentation and sample configuration files.

%prep
%setup -q

%build
%if 0%{?suse_version} > 1000
export CFLAGS="%{optflags} -fstack-protector"
%endif

%if %suse_version > 1315
tls_lib=gnutls
%else
tls_lib=openssl
%endif

%configure --with-tls=$tls_lib --with-libgsasl --docdir="%{_docdir}/%{name}"
make -O %{?_smp_mflags} V=1 VERBOSE=1

%install
%makeinstall V=1
%find_lang %{name}

for f in \
COPYING \
; do
    ff="${f##*/}"
    %__install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
done

echo -n >docfiles.lst
for f in \
AUTHORS ChangeLog* NEWS README* THANKS NOTES \
doc/*.example \
; do
    ff="${f##*/}"
    %__install -D -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$ff"
    echo "%doc %{_docdir}/%{name}/$ff" >>docfiles.lst
done

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/COPYING
%{_bindir}/mpop
%{_infodir}/mpop.info%{ext_info}
%{_mandir}/man1/mpop.1%{ext_man}

%files doc -f docfiles.lst
%defattr(-,root,root,-)

%changelog
