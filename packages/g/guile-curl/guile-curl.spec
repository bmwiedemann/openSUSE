#
# spec file for package guile-curl
#
# Copyright (c) 2026 SUSE LLC
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


Name:           guile-curl
Version:        0.10
Release:        0
Summary:        CURL bindings for GNU Guile
License:        GPL-3.0-or-later
URL:            https://github.com/spk121/guile-curl
Source0:        https://github.com/spk121/guile-curl/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  texinfo
BuildRequires:  pkgconfig(guile-3.0) >= 3.0
BuildRequires:  pkgconfig(libcurl)
Requires:       guile >= 3.0

%description
guile-curl allows Guile programs to perform client-side URL transfers,
like requesting documents from http or ftp servers. It is based on
the libcurl library.

%prep
%autosetup -p1
chmod 644 COPYING

%build
autoreconf -fiv
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post
%install_info --info-dir=%{_infodir} %{_infodir}/guile-curl.info%{?ext_info}

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/guile-curl.info%{?ext_info}

%files
%license COPYING
%doc AUTHORS NEWS README
%dir %{_datadir}/doc/guile-curl
%{_datadir}/doc/guile-curl/*
%dir %{_datadir}/guile/site/*
%{_datadir}/guile/site/*/curl.scm
%{_infodir}/guile-curl.info%{?ext_info}
%dir %{_libdir}/guile/*/extensions
%{_libdir}/guile/*/extensions/libguile-curl.so*
%dir %{_libdir}/guile/*/site-ccache
%{_libdir}/guile/*/site-ccache/curl.go

%changelog
