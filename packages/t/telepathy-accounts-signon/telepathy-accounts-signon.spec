#
# spec file for package telepathy-accounts-signon
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


Name:           telepathy-accounts-signon
Version:        1.0
Release:        0
Summary:        A mission control plugin for Telepathy
License:        LGPL-2.1
Group:          System/GUI/KDE
Source:         %{name}-%{version}-a4ae42797a9799fcbecb4c15bd9bd408e34c2eeb.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  kf5-filesystem
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libsignon-glib-devel
BuildRequires:  telepathy-mission-control-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A mission control plugin for Telepathy, integrating with libaccounts and libsignon
to provide IM accounts and authentication. This code is based on Nemo Mobile's
fork of the plugin from Empathy's ubuntu-online-account support.


%prep
%setup -q -n %{name}-%{version}-a4ae42797a9799fcbecb4c15bd9bd408e34c2eeb

%build
  qmake-qt5
  %make_jobs

%install
  make install INSTALL_ROOT=%{buildroot}
  

%files
%defattr(-,root,root)
%doc COPYING COPYING.LGPL NOTES README
%{_libdir}/mission-control-plugins.0/mcp-account-manager-accounts-sso.so

%changelog
