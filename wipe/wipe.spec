#
# spec file for package wipe
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wipe
Version:        2.3.1
Release:        0
Summary:        Secure Erasure of Data
License:        GPL-2.0+
Group:          Productivity/File utilities
Url:            http://wipe.sourceforge.net/
Source0:        http://sourceforge.net/projects/wipe/files/wipe/%{version}/%{name}-%{version}.tar.bz2
Source1:        http://sourceforge.net/projects/wipe/files/wipe/%{version}/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE wipe-2.2.0-makefile.diff -- Fix for Makefile.in to correct the install permissions and to don't strip binaries
Patch0:         %{name}-2.2.0-makefile.diff
# PATCH-FIX-OPENSUSE wipe-2.2.0-errno.diff --
Patch1:         %{name}-2.2.0-errno.diff
# PATCH-FIX-OPENSUSE wipe-2.2.0-include.diff --
Patch2:         %{name}-2.2.0-include.diff
BuildRequires:  automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Wipe is a tool that attempts to effectively degauses the surface of
a hard disk, making it virtually impossible to retrieve the data
that was stored on it. This tool is designed to make sure secure
data that is erased from a hard drive is unrecoverable.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
autoreconf -fi
%configure
make CFLAGS="%{optflags} -Wall -I. -DLINUX $(DEFINES) -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README TODO copyright
%{_mandir}/man?/*
%{_bindir}/*

%changelog
