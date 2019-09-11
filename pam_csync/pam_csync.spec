#
# spec file for package pam_csync
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


Name:           pam_csync
BuildRequires:  cmake
BuildRequires:  libcsync-devel
BuildRequires:  libiniparser-devel
BuildRequires:  pam-devel
Version:        0.42.0
Release:        0
Summary:        A PAM module for roaming home directories
License:        GPL-2.0+
Group:          System/Libraries
Url:            http://www.csync.org/
Source0:        %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM 0001-Remove-backward-compatibility-option-for-newer-cmake.patch
Patch1:         0001-Remove-backward-compatibility-option-for-newer-cmake.patch
# PATCH-FIX-UPSTREAM 0002-Update-FSF-address.patch
Patch2:         0002-Update-FSF-address.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a PAM module to provide roaming home directories for a user
session. The authentication module verifies the identity of a user and
triggers a synchronization with the server on the first login and the
last logout.



Authors:
--------
    Andreas Schneider


%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
if test ! -d "build"; then
  mkdir build
fi
pushd build
cmake \
  -DCMAKE_C_FLAGS:STRING="%{optflags}" \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
%if %{_lib} == lib64
  -DLIB_SUFFIX=64 \
%endif
  %{_builddir}/%{name}-%{version}

%__make %{?jobs:-j%jobs} VERBOSE=1
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING FAQ README
/%{_lib}/security/pam_csync.so
%dir %{_sysconfdir}/security
%config(noreplace) %{_sysconfdir}/security/pam_csync.conf
%{_mandir}/man?/pam_csync.*

%changelog
