#
# spec file for package pyzy
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pyzy
Version:        1.1
Release:        0
Summary:        The Chinese PinYin and Bopomofo conversion library
License:        LGPL-2.1-only
Group:          System/I18n/Chinese
URL:            https://github.com/openSUSE/pyzy
Source0:        https://github.com/openSUSE/pyzy/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/pyzy/pyzy-database-1.0.0.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  gnome-common
BuildRequires:  googletest-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(uuid) 
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  sqlite3
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  wget
Requires:       opencc

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
cp %{SOURCE1} data/db/open-phrase

%build
export PYTHON=python3
autoreconf -fi
%configure --disable-static \
           --enable-db-open-phrase \
           --enable-opencc
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n lib%{name}-1_0-0 -p /sbin/ldconfig

%postun -n lib%{name}-1_0-0 -p /sbin/ldconfig

%files -n lib%{name}-1_0-0
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
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
