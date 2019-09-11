#
# spec file for package mktorrent
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


Name:           mktorrent
Version:        1.1
Release:        0
Summary:        Command line utility to create BitTorrent metainfo files
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/Rudde/mktorrent
Source:         https://github.com/Rudde/mktorrent/archive/v1.1.tar.gz#/mktorrent-%{version}.tar.gz
BuildRequires:  openssl-devel

%description
Mktorrent can be used to create BitTorrent metainfo (.torrent) files from the
command line.

%prep
%setup -q

%build
make %{?_smp_mflags} \
    CFLAGS="%{optflags}" \
    PREFIX=%{_prefix} \
    USE_PTHREADS=1 \
    USE_LONG_OPTIONS=1 \
%ifnarch x86_64
    USE_LARGE_FILES=1 \
%endif
    USE_OPENSSL=1

%install
%make_install \
    CFLAGS="%{optflags}" \
    PREFIX=%{_prefix} \
    USE_PTHREADS=1 \
    USE_LONG_OPTIONS=1 \
%ifnarch x86_64
    USE_LARGE_FILES=1 \
%endif
    USE_OPENSSL=1

%files
%license COPYING
%{_bindir}/mktorrent

%changelog
