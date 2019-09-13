#
# spec file for package scim-uim
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


Name:           scim-uim
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  scim-devel
BuildRequires:  uim-devel
Version:        0.2.0
Release:        0
# Provides:       locale(scim:ja)
Url:            http://www.scim-im.org/
Source0:        http://mesh.dl.sourceforge.net/sourceforge/scim/scim-uim-0.2.0.tar.bz2
Patch0:         commit-when-focus-out.patch
Patch1:         missing-includes.patch
Patch2:         scim-uim-1.5.6-build-fixes.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        UIM Input Method Engine for SCIM
License:        GPL-2.0+
Group:          System/I18n/Japanese

%description
UIM Input Method Engine for SCIM.



Authors:
--------
    James Su <suzhe@tsinghua.org.cn>

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
libtoolize --force
autoreconf --force --install --verbose
export CXXFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=/usr \
            --sysconfdir=%{_sysconfdir} \
	    --libdir=%{_libdir} \
            --disable-static \
	    --enable-debug
make %{?jobs:-j %jobs}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f $RPM_BUILD_ROOT/%{_libdir}/scim-1.0/*/IMEngine/uim.*a
# %find_lang scim-uim

%clean
#[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/scim-1.0
%{_datadir}/scim/icons

%changelog
