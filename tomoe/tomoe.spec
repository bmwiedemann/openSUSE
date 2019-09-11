#
# spec file for package tomoe
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


Name:           tomoe
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  python
BuildRequires:  ruby-devel
Version:        0.6.0
Release:        0
Url:            http://sourceforge.net/projects/tomoe/
Source:         http://dfn.dl.sourceforge.net/sourceforge/tomoe/tomoe-0.6.0.tar.bz2
Patch0:         glib-include-fixes.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Japanese handwriting recognition engine
License:        LGPL-2.1+
Group:          System/I18n/Japanese

%description
Japanese handwriting recognition engine (Tegaki Online MOji-ninshiki
Engine)



Authors:
--------
    Hiroyuki Komatsu <komatsu@taiyaki.org>
    Hiroaki Nakamura <hnakamur@good-day.co.jp>

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          System/I18n/Japanese
Requires:       %{name} = %{version} glib2-devel

%description devel
Include Files and Libraries mandatory for Development



Authors:
--------
    Hiroyuki Komatsu <komatsu@taiyaki.org>
    Hiroaki Nakamura <hnakamur@good-day.co.jp>

%package doc
Summary:        Japanese handwriting recognition engine
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}

%description doc
Japanese handwriting recognition engine (Tegaki Online MOji-ninshiki
Engine)



Authors:
--------
    Hiroyuki Komatsu <komatsu@taiyaki.org>
    Hiroaki Nakamura <hnakamur@good-day.co.jp>

%prep
%setup -q
%patch0 -p1

%build
touch INSTALL README ; autoreconf --force --install
%if %suse_version > 1030
export CFLAGS="$RPM_OPT_FLAGS"
%else
export CFLAGS="$RPM_OPT_FLAGS -O0"
%endif
%configure --disable-static --with-pic
make %{?jobs:-j%jobs}

%install
%makeinstall
%find_lang tomoe
find %{buildroot} -name "*.la" -delete -print

%clean
rm -rf $RPM_BUILD_ROOT 

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f tomoe.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS TODO
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
%defattr(-,root,root)
%{_includedir}/tomoe
%{_libdir}/pkgconfig/tomoe.pc

%files doc
%defattr(-,root,root)
%{_datadir}/gtk-doc/html/tomoe

%changelog
