#
# spec file for package pyzy
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


Name:           pyzy
Version:        1.0git20120805
Release:        0
Summary:        The Chinese PinYin and Bopomofo conversion library
License:        LGPL-2.1
Group:          System/I18n/Chinese
Url:            http://code.google.com/p/pyzy
Source0:        %{name}-%{version}.tar.gz
Source1:        pyzy-database-1.0.0.tar.bz2
Source2:        pinyin-database-1.2.99.tar.bz2
# PATCH-FIX-UPSTREAM autofix.diff jengelh@inai.de -- resolve build errors with old automake
Patch1:         autofix.diff
# PATCH-FIX-UPSTREAM pyzy-opencc-1_0_2-build.patch hillwood@opensuse.org  -- Use opencc 1.0.2
Patch2:         pyzy-opencc-1_0_2-build.patch
# PATCH-FIX-UPSTREAM signed-char.patch schwab@suse.de -- Fix -Wnarrowing warning
Patch3:         signed-char.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.24.0
BuildRequires:  gnome-common
BuildRequires:  googletest-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  opencc
BuildRequires:  opencc-devel
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  sqlite
BuildRequires:  sqlite-devel
BuildRequires:  wget
Requires:       opencc

# Requires(post): sqlite

%description
The Chinese Pinyin and Bopomofo conversion library.

%package -n lib%{name}-1_0-0
Summary:        Libraries for pyzy
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n lib%{name}-1_0-0
The Chinese Pinyin and Bopomofo conversion library.

%package    devel
Summary:        Development tools for pyzy
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel

%description devel
The pyzy-devel package contains the header files for pyzy.

%package    db-open-phrase
Summary:        The open phrase database for pyzy
Group:          System/I18n/Chinese
BuildArch:      noarch
Provides:       pyzy-db
Requires(post): sqlite

%description db-open-phrase
The phrase database for pyzy from open-phrase project.

%package    db-android
Summary:        The android phrase database for pyzy
Group:          System/I18n/Chinese
BuildArch:      noarch
Provides:       pyzy-db
Requires(post): sqlite

%description db-android
The phrase database for pyzy from android project.

%prep
%setup -q
%patch -P 1 -p1
%patch2 -p1
%patch3 -p1
cp %{SOURCE1} data/db/open-phrase
cp %{SOURCE2} data/db/open-phrase

%build
./autogen.sh
%configure --disable-static \
           --enable-db-open-phrase \
           --enable-opencc
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
# make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n lib%{name}-1_0-0 -p /sbin/ldconfig

%postun -n lib%{name}-1_0-0 -p /sbin/ldconfig

%files -n lib%{name}-1_0-0
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/lib*.so.*
%{_datadir}/%{name}/phrases.txt
%{_datadir}/%{name}/db/create_index.sql
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/db

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files db-open-phrase
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/db
%{_datadir}/%{name}/db/open-phrase.db

%files db-android
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/db
%{_datadir}/%{name}/db/android.db

%changelog
