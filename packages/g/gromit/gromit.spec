# spec file for package gromit (version 20041213)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           gromit
Version:        20041213
Release:        1
License:        GPL-2.0+
Summary:        Tool to make annotations on the screen
Url:            http://www.home.unix-ag.org/simon/gromit/
Group:          Amusements/Toys/Other
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE gromit-cflags.patch vuntz@novell.com -- Use CFLAGS when compiling
Patch0:         gromit-cflags.patch
# PATCH-FIX-UPSTREAM gromit-no-DISABLE_DEPRECATED.patch vuntz@opensuse.org -- Remove *_DISABLE_DEPRECATED flags to fix build
Patch1:         gromit-no-DISABLE_DEPRECATED.patch
# PATCH-FIX-UPSTREAM gromit-link-x11.patch vuntz@opensuse.org -- Link to libX11 and libm to fix build
Patch2:         gromit-link-x11.patch
BuildRequires:  gtk2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gromit (GRaphics Over MIscellaneous Things) is a small tool to make
annotations on the screen.

It is useful for recording presentations.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
%__make %{?jobs:-j%jobs}

%install
install -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING gromitrc gromitrc_gsr README
%{_bindir}/%{name}

%changelog
