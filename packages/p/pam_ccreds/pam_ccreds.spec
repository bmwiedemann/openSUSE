#
# spec file for package pam_ccreds
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pam_ccreds
Version:        10
Release:        0
Summary:        Pam module to cache login credentials
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://www.padl.com/OSS/pam_ccreds.html

Source:         pam_ccreds-%{version}.tar.bz2
Source2:        baselibs.conf
Patch1:         pam_ccreds-readme-fix.dif
Patch2:         pam_ccreds-db6.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
Requires:       db
Requires:       pam

%description
The pam_ccreds module provides the means for Linux workstations to
locally authenticate using an enterprise identity when the network is
unavailable. Used in conjunction with the nss_updatedb utility, it
provides a mechanism for disconnected use of network directories.

%prep
%setup -q
%patch -P 1 -p0
%patch -P 2 -p1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
autoreconf --verbose --force --install
%configure --libdir=/%{_lib} --with-pamdir=/%{_lib}/security
make %{?_smp_mflags}

%install
install -d 755 $RPM_BUILD_ROOT/%{_lib}/security
install -m 755 pam_ccreds.so $RPM_BUILD_ROOT/%{_lib}/security

%files
%defattr(444,root,root,755)
%doc README COPYING pam.conf
%attr(555,root,root) /%{_lib}/security/pam_ccreds.so

%changelog
