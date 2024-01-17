#
# spec file for package rox-filer
#
# Copyright (c) 2021 SUSE LLC
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


Name:           rox-filer
Version:        2.11
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        rox.in
# add -ldl to linker options to include dlsym()
Patch0:         rox-filer-2.10-dso.patch

Requires:       shared-mime-info
Summary:        Minimalist file manager
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://rox.sourceforge.net/
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  libxml2-devel
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(sm)

%description
ROX-Filer is a fast and powerful graphical file manager for the X Window System.
You can use it as a small and fast filer within your current desktop, or get it
to manage your pinboard, panels and applications.

%prep
%autosetup -p0

%build
mkdir ROX-Filer/src/build2
pushd ROX-Filer/src/build2/
%define _configure ../configure
%configure CFLAGS="%{optflags} -fcommon"
%make_build
popd

%install
# no make install provided
mkdir -p %{buildroot}/%{_libdir}
cp -r ROX-Filer %{buildroot}/%{_libdir}
rm -rf %{buildroot}/%{_libdir}/ROX-Filer/build
rm -rf %{buildroot}/%{_libdir}/ROX-Filer/src
rm -rf %{buildroot}/%{_libdir}/ROX-Filer/ROX-Filer.dbg
sed 's@##libdir##@%{_libdir}@' %{S:1} > rox
install -D -m 0755 rox %{buildroot}/%{_bindir}/rox
%fdupes %{buildroot}/%{_prefix}

%files
%{_libdir}/ROX-Filer
%{_bindir}/rox
%license ROX-Filer/Help/COPYING

%changelog
