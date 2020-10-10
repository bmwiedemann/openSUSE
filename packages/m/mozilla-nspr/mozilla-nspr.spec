#
# spec file for package mozilla-nspr
#
# Copyright (c) 2020 SUSE LLC
#               2006-2020 Wolfgang Rosenauer
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


Name:           mozilla-nspr
Version:        4.29
Release:        0
Summary:        Netscape Portable Runtime
License:        MPL-2.0
Group:          System/Libraries
URL:            http://www.mozilla.org/projects/nspr/
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
# bug437293
%ifarch ppc64
Obsoletes:      mozilla-nspr-64bit
%endif
#
Source:         https://ftp.mozilla.org/pub/nspr/releases/v%{version}/src/nspr-%{version}.tar.gz
Source1:        baselibs.conf
Source99:       %{name}.changes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NSPR provides platform independence for non-GUI operating system
facilities. These facilities include threads, thread synchronization,
normal file and network I/O, interval timing and calendar time, basic
memory management (malloc and free), and shared library linking.


%package devel
Summary:        Netscape Portable Runtime development files
Group:          Development/Libraries/Other
Requires:       mozilla-nspr = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      mozilla-nspr-devel-64bit
%endif
#

%description devel
NSPR provides platform independence for non-GUI operating system
facilities. These facilities include threads, thread synchronization,
normal file and network I/O, interval timing and calendar time, basic
memory management (malloc and free), and shared library linking.


%prep
%setup -n nspr-%{version} -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
pushd nspr
# set buildtime to "last-modification-time"
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{S:99}")"
BUILD_STRING="$(date -u -d "${modified}" "+%%F %%T")"
BUILD_TIME="$(date -u -d "${modified}" "+%%s000000")"
#
export CFLAGS="%{optflags}"
./configure --enable-optimize="$CFLAGS" \
            --disable-debug \
%ifarch x86_64
	    --enable-64bit \
%endif
	    --libdir=%{_libdir} \
	    --includedir=%{_includedir}/nspr4 \
	    --prefix=%{_prefix}
make SH_DATE="$BUILD_STRING" SH_NOW="$BUILD_TIME" %{?_smp_mflags}
popd

%install
pushd nspr
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/nspr
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_includedir}/nspr4
cp config/nspr-config %{buildroot}%{_bindir}/
cp config/nspr.pc %{buildroot}%{_libdir}/pkgconfig
cp -L dist/lib/*.so %{buildroot}%{_libdir}
cp -L dist/lib/*.a  %{buildroot}%{_libdir}/nspr/
cp -rL dist/include/nspr/* %{buildroot}%{_includedir}/nspr4/
# #31667
chmod -x %{buildroot}%{_includedir}/nspr4/prvrsion.h
popd

%check
cd nspr
# Run test suite
perl ./pr/tests/runtests.pl 2>&1 | tee output.log
TEST_FAILURES=`grep -c FAILED ./output.log` || :
if [ $TEST_FAILURES -ne 0 ]; then
  echo "error: test suite returned failure(s)"
  exit 1
fi
echo "test suite completed"

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_libdir}/*.so

%files devel
%defattr(-, root, root)
%{_bindir}/nspr-config
%{_libdir}/pkgconfig/nspr.pc
%{_includedir}/nspr4/
%exclude %{_includedir}/nspr4/md/*
%{_libdir}/nspr/

%changelog
