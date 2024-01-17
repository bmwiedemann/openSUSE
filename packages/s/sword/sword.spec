#
# spec file for package sword
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         major 1.8
%define         libver 1_8_1
%define         libinstver 1.8.1
Name:           sword
Version:        1.8.1
Release:        0
Summary:        Framework for manipulating Bible texts
License:        GPL-2.0-only AND Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://www.crosswire.org/sword
Source0:        http://crosswire.org/ftpmirror/pub/sword/source/v%{major}/sword-%{version}.tar.gz 
Source1:        sword-rpmlintrc
Patch1:         sword-1.7.1-curl.patch
Patch2:         sword_sysdata_changes.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)
Recommends:     sword-bible
Recommends:     sword-commentary
Recommends:     sword-frontend

%description
The SWORD Project is an effort to create an ever expanding software package for
research and study of God and His Word.

The SWORD Bible Framework allows easy manipulation of Bible texts, commentaries,
lexicons, dictionaries, etc.  Many frontends are build using this framework.
An installed module set may be shared between any frontend using the framework.

%package -n libsword-%{libver}
Summary:        Shared library for sword
Group:          Development/Libraries/Other

%description -n libsword-%{libver}
This package contains the shared library for applications using sword.

%package devel
Summary:        Include files and static libraries for developing sword applications
Group:          Development/Libraries/Other
Requires:       libsword-%{libver} = %{version}
Requires:       pkgconfig(libcurl)

%description devel
Include files and static libraries for developing sword applications. This package
is required to compile Sword frontends, too.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export CXXFLAGS="%{optflags} -DU_USING_ICU_NAMESPACE=1"
autoreconf -fiv
%configure \
  --disable-static \
  --with-icu \
  --enable-tests \
  --enable-examples
make %{?_smp_mflags}

%check
cd tests/testsuite
# && ./runall.sh
TESTSUITE=$(for i in *.good; do basename $i .good; done)
for i in $TESTSUITE; do
	case $i in
		osis*)
			continue
		;;
		*)
			echo -n "$i: "
			./runtest.sh $i -q
		    if [ $? -ne 0 ]; then
		        echo FAILED
		        echo ""
		        echo To see problems, try running:
		        echo ./runtest.sh $i
		        echo ""
		        exit 1
		    else
		        echo PASSED.
		    fi
		;;
	esac
done

%install
%make_install install_config
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libsword-%{libver} -p /sbin/ldconfig
%postun -n libsword-%{libver} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog LICENSE NEWS README doc/translation-template.conf
%config(noreplace) %{_sysconfdir}/sword.conf
%{_bindir}/*
%dir %{_datadir}/sword
%dir %{_datadir}/sword/locales.d
%dir %{_datadir}/sword/mods.d
%{_datadir}/sword/locales.d/*
%{_datadir}/sword/mods.d/globals.conf

%files -n libsword-%{libver}
%{_libdir}/libsword-%{libinstver}.so

%files devel
%doc CODINGSTYLE
%{_includedir}/*
%{_libdir}/pkgconfig/sword.pc
%{_libdir}/*.so
%exclude %{_libdir}/libsword-%{libinstver}.so

%changelog
