#
# spec file for package libdb_java-4_8
#
# Copyright (c) 2023 SUSE LLC
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


%define         generic_name db
%define         major 4
%define         minor 8
Name:           libdb_java-4_8
Version:        %{major}.%{minor}.30
Release:        0
Summary:        Java Bindings for the Berkeley DB
License:        BSD-3-Clause
Group:          Productivity/Databases/Servers
URL:            https://oracle.com/technetwork/products/berkeleydb/
Source:         http://download.oracle.com/berkeley-db/db-%{version}.tar.gz
Source1:        %{name}.changes
Patch0:         db-%{version}.patch
# PATCH-FIX-OPENSUSE Fix compilation with Java 10 (10-internal)
Patch1:         libdb_java-4_8-fix-java10-comp.patch
# PATCH-FIX-OPENSUSE Fix build with GCC8, conflict with reserved builtin name
Patch2:         libdb-fix-atomic.patch
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  java-sdk >= 1.8
BuildRequires:  unzip
Requires:       libdb-%{major}_%{minor} = %{version}
Conflicts:      libdb_java-4_5
Provides:       db-java = %{version}

%description
These are the Java bindings for the Berkeley DB. They are needed for
the Java support of db and dbxml.

%package        devel
Summary:        Java Bindings for the Berkeley DB
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}
Requires:       glibc-devel
Conflicts:      libdb_java-4_5-devel
Provides:       db-java-devel = %{version}

%description    devel
These are the Java bindings for the Berkeley DB. They are needed for
the Java support of db and dbxml.

These are the development files.

%prep
%setup -q -n %{generic_name}-%{version}
%patch0
%patch1 -p1
%patch2

%build
cd dist
# dist/RELEASE codes the build date into the binary.
# Use last change of changes file instead
LAST_MOD=`stat --format="%%Y" %{SOURCE1}`
DIST_DATE=`date '+%%B %%e, %%Y' --date="@$LAST_MOD"`
sed -i -e "s/^DB_RELEASE_DATE=.*$/DB_RELEASE_DATE=\"$DIST_DATE\"/" RELEASE
./s_config
CFLAGS="%{optflags} -fno-strict-aliasing"
CC=gcc
export CFLAGS CXXFLAGS CC
#
# Build now the NPTL version
#
mkdir ../build_nptl
cd ../build_nptl
%define _configure ../dist/configure
%configure \
        --enable-compat185 --disable-dump185 \
        --enable-shared --disable-static \
        --enable-cxx \
        --with-mutex="POSIX/pthreads/library" \
        --enable-java JAVACFLAGS="-source 1.8 -target 1.8" \
%ifarch %{arm}
        %{_target_cpu}-suse-linux-gnueabi
%else
        %{_target_cpu}-suse-linux
%endif
# Make sure O_DIRECT is really disabled (build host could have old kernel)
perl -pi -e 's/#define HAVE_O_DIRECT 1/#undef HAVE_O_DIRECT/' db_config.h
# Remove libtool predep_objects and postdep_objects wonkiness
perl -pi -e 's/^predep_objects=".*$/predep_objects=""/' libtool
perl -pi -e 's/^postdep_objects=".*$/postdep_objects=""/' libtool
perl -pi -e 's/-shared -nostdlib/-shared/' libtool

make %{?_smp_mflags} LIBSO_LIBS='$(LIBS)' LIBXSO_LIBS='$(LIBS)'" -L%{_libdir} -lstdc++"

%install
mkdir -p %{buildroot}%{_includedir}/db4
mkdir -p %{buildroot}%{_libdir}
cd build_nptl
%make_install STRIP=true
cd ..
# make ldd happy:
chmod 755 %{buildroot}%{_libdir}/libdb*.so
# Fix header file installation
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/db4
echo "#include <db4/db.h>" > %{buildroot}%{_includedir}/db.h
echo "#include <db4/db_185.h>" > %{buildroot}%{_includedir}/db_185.h
echo "#include <db4/db_cxx.h>" > %{buildroot}%{_includedir}/db_cxx.h
# remove dangling tags symlink from examples.
rm -f examples_cxx/tags
rm -f examples_c/tags
# Move documentation to the right directory
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_prefix}/docs/* %{buildroot}/%{_docdir}/%{name}
cp -a examples_cxx examples_c %{buildroot}/%{_docdir}/%{name}
cp -a LICENSE README %{buildroot}/%{_docdir}/%{name}
# Remove api documentation for C++, Java and TCL
rm -rf %{buildroot}/%{_docdir}/%{name}/csharp
rm -rf %{buildroot}/%{_docdir}/%{name}/java
rm -rf %{buildroot}/%{_docdir}/%{name}/api_reference/CXX
rm -rf %{buildroot}/%{_docdir}/%{name}/api_reference/STL
rm -rf %{buildroot}/%{_docdir}/%{name}/api_reference/TCL
rm -rf %{buildroot}/%{_docdir}/%{name}/gsg*/CXX
rm -rf %{buildroot}/%{_docdir}/%{name}/gsg*/JAVA
mv %{buildroot}/%{_docdir}/%{name}/collections/tutorial %{buildroot}/%{_docdir}/%{name}/
# Remove crappy *.la files
find %{buildroot} -type f -name "*.la" -delete -print
pushd %{buildroot}
for file in `find | grep -v "\(java\|jar\)"`
do
  rm $file || true
done
rm -rf %{buildroot}/%{_defaultdocdir}
mkdir -p %{buildroot}/%{_javadir}
mv %{buildroot}/%{_libdir}/*.jar %{buildroot}/%{_javadir}/db-%{version}.jar
ln -sf %{_javadir}/db-%{version}.jar %{buildroot}/%{_javadir}/db.jar

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_javadir}/*
%{_libdir}/libdb_java-%{major}.%{minor}.so

%files devel
%{_libdir}/*_g.so
%{_libdir}/libdb_java.so
%{_libdir}/libdb_java-%{major}.so

%changelog
