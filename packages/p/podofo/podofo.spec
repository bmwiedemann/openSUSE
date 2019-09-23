#
# spec file for package podofo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libver 0_9_6
Name:           podofo
Version:        0.9.6
Release:        0
Summary:        Tools to work with PDF files
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PDF
URL:            http://podofo.sourceforge.net/
Source0:        http://downloads.sourceforge.net/podofo/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         r1933-Really-fix-CVE-2017-7381.patch
# PATCH-FIX-UPSTREAM
Patch1:         r1936-Really-fix-CVE-2017-7382.patch
# PATCH-FIX-UPSTREAM
Patch2:         r1937-Really-fix-CVE-2017-7383.patch
# PATCH-FIX-UPSTREAM
Patch3:         r1938-Fix-CVE-2018-11256-PdfError-info-gives-not-found-page-0-based.patch
# PATCH-FIX-UPSTREAM
Patch4:         r1941-Fix-CVE-2017-8054-and-other-issues-keeping-binary-compat.patch
# PATCH-FIX-UPSTREAM
Patch5:         r1942-Fix-build-with-cmake-ge-3.12.patch
# PATCH-FIX-UPSTREAM
Patch6:         r1945-Fix-possible-incompatibility-of-PdfAESStream-with-OpenSSL-1.1.0g.patch
# PATCH-FIX-UPSTREAM
Patch7:         r1948-Fix-CVE-2018-12982-implementing-inline-PdfDictionary-MustGetKey.patch
# PATCH-FIX-UPSTREAM
Patch8:         r1949-Fix-CVE-2018-5783-by-introducing-singleton-limit-for-indirect-objects-keeping-binary-compat.patch
# PATCH-FIX-UPSTREAM
Patch9:         r1950-Fix-null-pointer-dereference-in-PdfTranslator-setTarget.patch
# PATCH-FIX-UPSTREAM
Patch10:        r1952-Fix-CVE-2018-11255-Null-pointer-dereference-in-PdfPage-GetPageNumber.patch
# PATCH-FIX-UPSTREAM
Patch11:        r1953-Fix-CVE-2018-14320-Possible-undefined-behaviour-in-PdfEncoding-ParseToUnicode.patch
# PATCH-FIX-UPSTREAM
Patch12:        r1954-Fix-CVE-2018-20751-null-pointer-dereference-in-crop_page-of-tools-podofocrop.patch
# PATCH-FIX-UPSTREAM
Patch13:        r1961-EncryptTest-Fix-buffer-overflow-in-decrypted-out-buffer-in-TestEncrypt.patch
# PATCH-FIX-UPSTREAM
Patch14:        r1963-Fix-heap-based-buffer-overflow-vulnerability-in-PoDoFo-PdfVariant-DelayedLoad.patch
# PATCH-FIX-UPSTREAM
Patch15:        r1969-Fix-CVE-2019-9687-heap-based-buffer-overflow.patch
BuildRequires:  cmake >= 2.5
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
#BuildRequires:  libcppunit-devel
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
Command line tools for working with PDF files.

%package -n libpodofo%{libver}
Summary:        PDF parsing and creation library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libpodofo%{libver}
A cross platform PDF parsing and creation library.

%package -n libpodofo-devel
Summary:        Development files for podofo
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       libpodofo%{libver} = %{version}

%description -n libpodofo-devel
This package contains development files for podofo library.

%prep
%setup -q
%autopatch -p0 

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> Doxyfile

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPODOFO_BUILD_STATIC=FALSE -DPODOFO_USE_VISIBILITY=1 \
%if "%{_lib}" == "lib64"
-DWANT_LIB64=1 \
%endif
../

make %{?_smp_mflags} VERBOSE=1
cd ..

# Build devel docs
doxygen

%install
pushd build
%make_install DESTDIR=%{buildroot}
popd

# Install devel docs (do it manually to fix also rpmlint warning "files-duplicate" with %%fdupes)
mkdir -p %{buildroot}%{_docdir}/libpodofo-devel
install -pm 0644 AUTHORS COPYING.LIB ChangeLog FAQ.html README.html TODO %{buildroot}%{_docdir}/libpodofo-devel/
cp -a doc/html/ %{buildroot}%{_docdir}/libpodofo-devel/

%fdupes -s %{buildroot}

%post -n libpodofo%{libver} -p /sbin/ldconfig
%postun -n libpodofo%{libver} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.html
%{_bindir}/*
%{_mandir}/man1/podofo*.1%{?ext_man}

%files -n libpodofo%{libver}
%license COPYING
%{_libdir}/libpodofo.so.%{version}

%files -n libpodofo-devel
%license COPYING
%doc %{_docdir}/libpodofo-devel/
%{_includedir}/podofo/
%{_libdir}/libpodofo.so
%{_libdir}/pkgconfig/libpodofo-0.pc

%changelog
