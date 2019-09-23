#
# spec file for package cadaver
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cadaver
#BuildRequires:  automake
BuildRequires:  libneon-devel
BuildRequires:  readline-devel
Version:        0.23.3
Release:        0
Summary:        Command Line WebDAV Client for Unix
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.webdav.org/cadaver/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-0.23.2-strncat.patch
Patch1:         cadaver-neon.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cadaver is a command-line WebDAV client for Unix. It supports file
upload, download, on-screen display, namespace operations (move and
copy), collection creation and deletion, and locking operations.

%prep
%setup -q
%patch0
%patch1 -p1
# Forcibly prevent use of bundled neon/expat/gettext sources.
rm -rf lib/neon/*.[ch] lib/intl/*.[ch]

%build
#gettextize --force
#aclocal -I m4 -I m4/neon
#autoconf --force
#autoheader --force
export LDFLAGS=-pie CFLAGS="$RPM_OPT_FLAGS -fPIE -Wall"
%configure \
    --with-ssl \
    --with-libxml2 
make %{?_smp_mflags}

%install
make "DESTDIR=$RPM_BUILD_ROOT" install
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc BUGS COPYING ChangeLog FAQ INTEROP NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
