#
# spec file for package rox-filer
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  libxml2-devel
BuildRequires:  shared-mime-info
%if 0%{suse_version} > 1210
BuildRequires:  libSM-devel
%endif
Name:           rox-filer
Version:        2.11
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        rox.in
# add -ldl to linker options to include dlsym()
Patch0:         rox-filer-2.10-dso.patch

Requires:       shared-mime-info
Summary:        Minimalist file manager
License:        GPL-2.0+
Group:          Productivity/File utilities
Url:            http://rox.sourceforge.net/

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ROX-Filer is a fast and powerful graphical file manager for the X Window System.
You can use it as a small and fast filer within your current desktop, or get it
to manage your pinboard, panels and applications.

%prep
%setup -q
%patch0

%build
ROX-Filer/AppRun --compile

%install
rm -rf ROX-Filer/{build,src}
rm -rf ROX-Filer/ROX-Filer.dbg
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
cp -r ROX-Filer $RPM_BUILD_ROOT/%{_libdir}
sed 's@##libdir##@%{_libdir}@' %{S:1} > rox
install -D -m 0755 rox $RPM_BUILD_ROOT/%{_bindir}/rox

%files
%defattr(-,root,root)
%{_libdir}/ROX-Filer
%attr(0755,root,root) %{_bindir}/rox

%changelog
