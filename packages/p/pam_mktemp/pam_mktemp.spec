#
# spec file for package pam_mktemp
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           pam_mktemp
Url:            http://www.openwall.com/pam/
BuildRequires:  e2fsprogs-devel
BuildRequires:  pam-devel
Requires:       pam
Provides:       pam-modules:/%_lib/security/pam_mktemp.so
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
%setup
%patch0 -p1
%patch1 -p1

%build
EXTRA_CFLAGS="-fno-strict-aliasing"
%ifnarch ia64
    EXTRA_CFLAGS="$EXTRA_CFLAGS -Wa,--noexecstack"
%endif
make CFLAGS="$RPM_OPT_FLAGS $EXTRA_CFLAGS -fPIC -DHAVE_SHADOW -DLINUX_PAM" \
	%{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security
make DESTDIR=$RPM_BUILD_ROOT install
#
# Remove stuff we don't wish to have now:
#
rm -rf $RPM_BUILD_ROOT/usr/{include,lib}
rm -rf $RPM_BUILD_ROOT/%{_lib}/security/*.la
#
# On 64bit archs, we need to move same libraries ourself:
#
if [ %_lib = lib64 ]; then
  mv $RPM_BUILD_ROOT/lib/security/* $RPM_BUILD_ROOT/%{_lib}/security/
fi
# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
for module in $RPM_BUILD_ROOT/%{_lib}/security/pam*.so ; do
   if ! sh $RPM_SOURCE_DIR/dlopen.sh -lpam -ldl ${module} ; then
      exit 1
   fi
done

%files 
%defattr(-,root,root,755)
%doc LICENSE README
%attr(755,root,root) /%{_lib}/security/pam_*.so

%changelog
