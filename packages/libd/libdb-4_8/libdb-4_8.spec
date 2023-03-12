#
# spec file for package libdb-4_8
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


%define util_list archive checkpoint deadlock dump hotbackup load printlog recover sql stat upgrade verify
%define         generic_name db
%define         major 4
%define         minor 8
Name:           libdb-4_8
Version:        %{major}.%{minor}.30
Release:        0
Summary:        Berkeley DB Database Library Version 4.8
License:        Sleepycat
Group:          System/Libraries
URL:            https://oracle.com/technetwork/products/berkeleydb/
Source:         http://download.oracle.com/berkeley-db/db-%{version}.tar.gz
Source1:        %{name}.changes
Source2:        baselibs.conf
Patch0:         db-%{version}.patch
# PATCH-FIX-OPENSUSE Fix build with GCC8, conflict with reserved builtin name
Patch1:         libdb-fix-atomic.patch
Patch2:         0001-OPD-deadlock-RH-BZ-1349779.patch
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Provides:       db = %{version}
%{?suse_build_hwcaps_libs}

%description
The Berkeley DB Database is a programmatic toolkit that provides
database support for applications.

This package contains the necessary runtime libraries.

%package -n db48-utils
Summary:        Command Line tools for Managing Berkeley DB Databases
Group:          Productivity/Databases/Tools
Requires(post): update-alternatives
Provides:       db-utils = %{version}
Obsoletes:      db-utils < %{version}

%description -n db48-utils
The Berkeley DB Database is a programmatic toolkit that provides
database support for applications.

This package contains the command line tools for managing Berkeley DB
databases.

%package -n     db48-doc
Summary:        Documentation for Berkeley DB
Group:          Development/Libraries/C and C++
Provides:       db-doc = %{version}
Provides:       db-utils-doc = %{version}
Obsoletes:      db-doc < %{version}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n db48-doc
The Berkeley DB Database is a programmatic toolkit that provides
database support for applications.

This package contains the documentation.

%package        devel
Summary:        Development Files and Libraries for the Berkeley DB library Version 4.8
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Conflicts:      libdb-4_5-devel
Provides:       db-devel = %{version}

%description    devel
The Berkeley DB Database is a programmatic toolkit that provides
database support for applications.

This package contains the header files and libraries.

%prep
%setup -q -n %{generic_name}-%{version}
%patch0
%patch1
%patch2 -p1

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

mkdir -p %{buildroot}%{_sysconfdir}/alternatives

for i in %{util_list}; do
    # dummy
    mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
    touch "%{buildroot}%{_sysconfdir}/alternatives/db_$i"
    mv "%{buildroot}/%{_bindir}/db_$i" "%{buildroot}/%{_bindir}/db48_$i"
    ln -s "%{_sysconfdir}/alternatives/db_$i" "%{buildroot}%{_bindir}/db_$i"
done

%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n db48-utils
for i in %{util_list}; do
	update-alternatives --install "%{_bindir}/db_$i" \
		"db_$i" "%{_bindir}/db48_$i" 48
done

%postun -n db48-utils
for i in %{util_list}; do
	update-alternatives --remove "db_$i" "%{_bindir}/db_$i"
done

%files
%{_libdir}/libdb-%{major}.%{minor}.so
%{_libdir}/libdb_cxx-%{major}.%{minor}.so

%files -n db48-doc
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/index.html
%license %{_docdir}/%{name}/license
%doc %{_docdir}/%{name}/articles
%doc %{_docdir}/%{name}/api_reference
%doc %{_docdir}/%{name}/examples_c
%doc %{_docdir}/%{name}/examples_cxx
%doc %{_docdir}/%{name}/gsg*
%doc %{_docdir}/%{name}/porting
%doc %{_docdir}/%{name}/programmer_reference
%doc %{_docdir}/%{name}/tutorial

%files -n db48-utils
%{_bindir}/db48_*
%ghost %{_sysconfdir}/alternatives/db_archive
%ghost %{_sysconfdir}/alternatives/db_checkpoint
%ghost %{_sysconfdir}/alternatives/db_deadlock
%ghost %{_sysconfdir}/alternatives/db_dump
%ghost %{_sysconfdir}/alternatives/db_hotbackup
%ghost %{_sysconfdir}/alternatives/db_load
%ghost %{_sysconfdir}/alternatives/db_printlog
%ghost %{_sysconfdir}/alternatives/db_recover
%ghost %{_sysconfdir}/alternatives/db_sql
%ghost %{_sysconfdir}/alternatives/db_stat
%ghost %{_sysconfdir}/alternatives/db_upgrade
%ghost %{_sysconfdir}/alternatives/db_verify
%{_bindir}/db_*

%files devel
%dir %{_includedir}/db4
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_includedir}/db_cxx.h
%{_includedir}/db4/db.h
%{_includedir}/db4/db_185.h
%{_includedir}/db4/db_cxx.h
%{_libdir}/libdb.so
%{_libdir}/libdb-%{major}.so
%{_libdir}/libdb_cxx.so
%{_libdir}/libdb_cxx-%{major}.so

%changelog
