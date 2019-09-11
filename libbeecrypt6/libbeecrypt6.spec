#
# spec file for package libbeecrypt6
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libbeecrypt6
Summary:        An open source cryptography library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Version:        4.1.2
Release:        0
BuildRequires:  libtool
Source:         beecrypt-%{version}.tar.bz2
Patch0:         beecrypt-4.1.2.diff
Patch1:         beecrypt-4.1.2-build.diff
Patch2:         beecrypt-4.1.2-fix_headers.diff
Patch3:         beecrypt-libdir.diff
Url:            http://sourceforge.net/projects/beecrypt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BeeCrypt is an ongoing project to provide a strong and fast
cryptography toolkit. Includes entropy sources, random generators,
block ciphers, hash functions, message authentication codes,
multiprecision integer routines, and public key primitives.

%package -n libbeecrypt-devel
Summary:        An open source cryptography library
Group:          Development/Libraries/C and C++
Requires:       libbeecrypt6 = %{version}

%description -n libbeecrypt-devel
BeeCrypt is an ongoing project to provide a strong and fast
cryptography toolkit. Includes entropy sources, random generators,
block ciphers, hash functions, message authentication codes,
multiprecision integer routines, and public key primitives.

%prep
%setup -q -n beecrypt-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch -P 3 -p1

%build
./autogen.sh
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -ffunction-sections"
export LDFLAGS="-Wl,-Bsymbolic-functions -ffunction-sections"
%configure --without-cplusplus --without-java --without-python
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install
rm -f $RPM_BUILD_ROOT%{_libdir}/libbeecrypt.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS BUGS CONTRIBUTORS ChangeLog COPYING COPYING.LIB NEWS README
%{_libdir}/libbeecrypt.so.6*

%files -n libbeecrypt-devel
%defattr(644,root,root,755)
/usr/include/beecrypt
%{_libdir}/libbeecrypt.a
%{_libdir}/libbeecrypt.so

%changelog
