#
# spec file for package pam_passwdqc
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           pam_passwdqc
Url:            http://www.openwall.com/passwdqc/
BuildRequires:  pam-devel
Requires:       pam
Recommends:     passwdqc
Provides:       pam-modules:/%_lib/security/pam_passwdqc.so
Version:        1.3.1
Release:        0
Summary:        Simple Password Strength Checking Module
License:        BSD-3-Clause
Group:          System/Libraries
Source0:        www.openwall.com/passwdqc/passwdqc-%{version}.tar.gz
Source1:        baselibs.conf
Source50:       dlopen.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

pam_passwdqc is a simple password strength checking module forPAM-aware
password changing programs. In addition to checking regular passwords,
it offers support for passphrases and can provide randomly generated
ones.

%package -n libpasswdqc0
Summary:        A Simple Password Strength Checking Library
Group:          System/Libraries

%description -n libpasswdqc0
libpasswdqc is a simple password strength checking library. 
In addition to checking regular passwords, it offers support for passphrases 
and can provide randomly generated ones.

%package -n passwdqc-devel
Summary:        Useful collection of routines for C and C++ programming
Group:          Development/Libraries/C and C++
Requires:       libpasswdqc0 = %{version}

%description -n passwdqc-devel
libpasswdqc is a simple password strength checking library.
In addition to checking regular passwords, it offers support for passphrases
and can provide randomly generated ones.


%package -n passwdqc
Summary:        Tools for Password Checking and Generation
Group:          Productivity/Networking/Diagnostic

%description -n passwdqc
The pwqcheck program checks passphrase quality using the libpasswdqc library.
The pwqgen program generates a random passphrase using the libpasswdqc library.


%prep
%setup -n passwdqc-%{version}

%build
EXTRA_CFLAGS="-fno-strict-aliasing"
# ia64 is noexecstack by default
%ifnarch ia64
    EXTRA_CFLAGS="$EXTRA_CFLAGS -Wa,--noexecstack"
%endif
make CFLAGS="$RPM_OPT_FLAGS $EXTRA_CFLAGS -fPIC -DHAVE_SHADOW -DLINUX_PAM" \
     SHARED_LIBDIR="/%{_lib}" \
     DEVEL_LIBDIR="/usr/%{_lib}" \
     SECUREDIR="/%{_lib}/security"

%install
make DESTDIR=$RPM_BUILD_ROOT SHARED_LIBDIR="/%{_lib}" DEVEL_LIBDIR="/%{_libdir}" SECUREDIR="/%{_lib}/security" install

%check
# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
export LD_LIBRARY_PATH="$RPM_BUILD_ROOT/%{_lib}/"
for module in $RPM_BUILD_ROOT/%{_lib}/security/pam*.so ; do
   if ! sh $RPM_SOURCE_DIR/dlopen.sh -lpam -ldl ${module} ; then
      exit 1
   fi
done

%post -n libpasswdqc0 -p /sbin/ldconfig

%postun -n libpasswdqc0 -p /sbin/ldconfig

%files 
%defattr(-,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_*.so
%attr(644,root,root) %doc %{_mandir}/man8/pam_*.8.*

%files -n libpasswdqc0
%defattr(-,root,root)
/%{_lib}/libpasswdqc*.so.*

%files -n passwdqc-devel
%defattr(-,root,root)
%{_libdir}/libpasswdqc*.so
%{_includedir}/*

%files -n passwdqc
%defattr(-,root,root)
%attr(644,root,root) %doc %{_mandir}/man1/*
%attr(644,root,root) %doc %{_mandir}/man5/*
%license INTERNALS LICENSE PLATFORMS README 
%config(noreplace) %{_sysconfdir}/*.conf
%{_bindir}/*

%changelog
