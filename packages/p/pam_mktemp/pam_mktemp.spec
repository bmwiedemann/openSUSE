#
# spec file for package pam_mktemp
#
# Copyright (c) 2021 SUSE LLC
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


Name:           pam_mktemp
URL:            http://www.openwall.com/pam/
BuildRequires:  e2fsprogs-devel
BuildRequires:  pam-devel
Requires:       pam
Provides:       pam-modules:%{_pam_moduledir}/pam_mktemp.so
Version:        1.1.1
Release:        0
Summary:        PAM Module to Provide Per-User Private Directories Under /tmp
License:        SUSE-Permissive
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source50:       dlopen.sh
Patch0:         pam_mktemp-1.1.1-Makefile.patch
Patch1:         pam_mktemp-1.1.1-ppc64.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

pam_mktemp is a PAM module which may be used with a PAM-aware login
service to provide per-user private directories under /tmp as a part of
PAM session or account management.

%prep
%autosetup -p1

%build
EXTRA_CFLAGS="-fno-strict-aliasing"
%ifnarch ia64
    EXTRA_CFLAGS="$EXTRA_CFLAGS -Wa,--noexecstack"
%endif
make CFLAGS="$RPM_OPT_FLAGS $EXTRA_CFLAGS -fPIC -DHAVE_SHADOW -DLINUX_PAM" \
	%{?_smp_mflags}

%install
make DESTDIR=%{buildroot} SHARED_LIBDIR=/"%{_lib}" DEVEL_LIBDIR="%{_libdir}" SECUREDIR="%{_pam_moduledir}" install
# Remove stuff we don't wish to have now. Note that "make" seems to install library files in /usr/lib!
rm -rf %{buildroot}%{_prefix}/include/security/*.h %{buildroot}/usr/lib/lib*

%check
# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
export LD_LIBRARY_PATH="%{buildroot}/%{_lib}/"
for module in %{buildroot}%{_pam_moduledir}/pam*.so ; do
   if ! sh $RPM_SOURCE_DIR/dlopen.sh -lpam -ldl ${module} ; then
      exit 1
   fi
done

%files 
%defattr(-,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_pam_moduledir}/pam_*.so

%changelog
