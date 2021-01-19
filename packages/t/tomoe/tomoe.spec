#
# spec file for package tomoe
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


Name:           tomoe
Version:        0.6.0
Release:        0
Summary:        Japanese handwriting recognition engine
License:        LGPL-2.1-or-later
Group:          System/I18n/Japanese
URL:            https://sourceforge.net/projects/tomoe/
Source:         http://dfn.dl.sourceforge.net/sourceforge/tomoe/tomoe-0.6.0.tar.bz2

Patch0:         glib-include-fixes.diff
Patch1:         tomoe-0.6.0-fixes-set-parse-error.patch
Patch2:         tomoe-0.6.0-strerror.patch

BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  python
BuildRequires:  ruby-devel

%description
Japanese handwriting recognition engine (Tegaki Online MOji-ninshiki
Engine)

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}
Requires:       glib2-devel

%description devel
Include Files and Libraries mandatory for Development

%package doc
Summary:        Japanese handwriting recognition engine
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}

%description doc
Japanese handwriting recognition engine (Tegaki Online MOji-ninshiki
Engine)

%prep
%autosetup -p1

%build
touch INSTALL README ; autoreconf --force --install
export CFLAGS="%{optflags}"
%configure \
	--disable-static \
	--with-pic \
	%{nil}
%make_build

%install
%make_install
%find_lang tomoe
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f tomoe.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO
%{_datadir}/tomoe
%{_libdir}/*.so
%{_libdir}/*.so.*
%dir %{_libdir}/tomoe
%dir %{_libdir}/tomoe/module/
%dir %{_libdir}/tomoe/module/dict
%{_libdir}/tomoe/module/dict/*.so
%dir %{_libdir}/tomoe/module/recognizer
%{_libdir}/tomoe/module/recognizer/*.so
%{_sysconfdir}/tomoe

%files devel
%{_includedir}/tomoe
%{_libdir}/pkgconfig/tomoe.pc

%files doc
%{_datadir}/gtk-doc/html/tomoe

%changelog
