#
# spec file for package csync
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


Name:           csync
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  pkg-config
%if 0%{?suse_version}
BuildRequires:  sqlite3-devel
%else
BuildRequires:  sqlite-devel
%endif
Version:        0.50.0
Release:        0
Summary:        A user level bidirectional client only file synchronizer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.csync.org/
Source0:        %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE fix-cmake-on-pre-12.patch
Patch0:         fix-cmake-on-pre-12.patch
Patch1:         csync_log.h.patch
# PATCH-FIX-OPENSUSE fix-missing-const.patch
Patch2:         fix-missing-const.patch
# PATCH-FIX-OPENSUSE csync-libssh.patch -- Detect newer libssh versions; hacked patch
Patch3:         csync-libssh.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
csync is an implementation of a file synchronizer which provides the
feature of roaming home directories for Linux clients. csync makes use
of libsmbclient in Samba/Windows environments.

%package -n libcsync0
Summary:        A user level bidirectional client only file synchronizer
License:        LGPL-2.1-or-later
Group:          System/Libraries
%if 0%{?suse_version} > 1030
Recommends:     libcsync-plugin-smb
Recommends:     libcsync-plugin-sftp
%endif

%description -n libcsync0
csync is an implementation of a file synchronizer which provides the
feature of roaming home directories for Linux clients. csync makes use
of libsmbclient in Samba/Windows environments.

%package -n libcsync-plugin-smb
Summary:        SMB plugin for csync
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       libcsync0 = %{version}

%description -n libcsync-plugin-smb
This plug-in allows applications using csync to synchronize with a
Samba or Windows server.

%package -n libcsync-plugin-sftp
Summary:        A user level bidirectional client only file synchronizer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Requires:       libcsync0 = %{version}

%description -n libcsync-plugin-sftp
csync is an implementation of a file synchronizer which provides the
feature of roaming home directories for Linux clients. csync makes use
of libsmbclient in Samba/Windows environments.

%if 0%{?suse_version} >= 1200
%package -n libcsync-plugin-owncloud
Summary:        Owncloud plugin for csync
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       libcsync0 = %{version}
BuildRequires:  libneon-devel

%description -n libcsync-plugin-owncloud
This plug-in allows applications using csync to synchronize with Owncloud.
%endif

%package -n libcsync-devel
Summary:        Development files for csync
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libcsync0 = %{version}

%description -n libcsync-devel
The libcsync-devel package contains the static libraries and header
files needed for development with csync.

%package -n libcsync-devel-doc
Summary:        Developer documentation for csync
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++

%description -n libcsync-devel-doc
The libcsync-devel-doc package provides documentation for csync
development.

%package -n libcsync-doc
Summary:        User documentation for csync
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++

%description -n libcsync-doc
The libcsync-doc package provides user documentation for csync.

%prep
%setup -q
%if 0%{?suse_version} < 1200
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1
if [ -f %{_includedir}/libssh/libssh_version.h ]; then
%patch3 -p1
fi

%build
if test ! -e "build"; then
  %{__mkdir} build
fi
pushd build
cmake \
  -DCMAKE_C_FLAGS:STRING="%{optflags}" \
  -DCMAKE_CXX_FLAGS:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if %{_lib} == lib64
  -DLIB_SUFFIX=64 \
%endif
  %{_builddir}/%{name}-%{version}
%__make %{?jobs:-j%jobs} VERBOSE=1
%__make doc
popd

%install
pushd build
%if 0%{?suse_version}
%makeinstall
%else
make DESTDIR=%{buildroot} install
%endif
popd

%post -n libcsync0 -p /sbin/ldconfig

%postun -n libcsync0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/csync
%{_mandir}/man?/csync.*

%files -n libcsync0
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README
%dir %{_sysconfdir}/csync
%config(noreplace) %{_sysconfdir}/csync/csync.conf
%config(noreplace) %{_sysconfdir}/csync/csync_exclude.conf
%{_libdir}/libcsync.so.*
%dir %{_libdir}/csync-0

%files -n libcsync-plugin-smb
%defattr(-,root,root)
%{_libdir}/csync-0/csync_smb.so

%files -n libcsync-plugin-sftp
%defattr(-,root,root)
%{_libdir}/csync-0/csync_sftp.so

%if 0%{?suse_version} >= 1200
%files -n libcsync-plugin-owncloud
%defattr(-,root,root)
%{_libdir}/csync-0/csync_owncloud.so
%endif

%files -n libcsync-devel
%defattr(-,root,root)
%{_includedir}/csync
%{_libdir}/libcsync.so

%files -n libcsync-devel-doc
%defattr(-,root,root)
%doc build/doc/html

%files -n libcsync-doc
%defattr(-,root,root)
%{_datadir}/doc/csync

%changelog
