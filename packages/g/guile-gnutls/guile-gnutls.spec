#
# spec file for package guile-gnutls
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


Name:           guile-gnutls
Version:        3.7.11
Release:        0
Summary:        Guile bindings to GnuTLS
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
URL:            https://gitlab.com/gnutls/guile
Source0:        https://ftp.gnu.org/gnu/gnutls/guile-gnutls-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gnutls/guile-gnutls-%{version}.tar.gz.sig
# curl 'https://josefsson.org/key-20190320.txt' | gpg --import - | gpg --export -a "51722B08FE4745A2" > guile-gnutls.keyring
Source2:        guile-gnutls.keyring
BuildRequires:  automake
BuildRequires:  guile-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libtool
BuildRequires:  makeinfo
Provides:       gnutls-guile
Obsoletes:      gnutls-guile

%description
GnuTLS wrappers for GNU Guile, a dialect of Scheme.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%doc README
%license COPYING
%{_datadir}/guile/site/*
%{_infodir}/gnutls-guile.info.gz
%{_libdir}/guile/*

%changelog
