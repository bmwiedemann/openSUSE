#
# spec file for package pam_chroot (Version 0.9.2)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           pam_chroot
Url:            http://sourceforge.net/projects/pam-chroot/
BuildRequires:  pam-devel
License:        GPL-2.0+
Group:          System/Libraries
Requires:       pam
Provides:       pam-modules:/etc/security/chroot.conf
AutoReqProv:    on
Version:        0.9.2
Release:        42
Summary:        Linux-PAM Module that Allows a User to Be Chrooted
Source0:        pam_chroot-0.9.2.tar.bz2
Source1:        baselibs.conf
Source50:       dlopen.sh
Patch1:         pam_chroot-0.9.2.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

pam_chroot is a Linux-PAM module that allows a user to be chrooted in
auth, account, or session.



Authors:
--------
    Matthew Kirkwood (weejock@ferret.lmh.ox.ac.uk)
    Ed Schmollinger (schmolli@frozencrow.org)

%prep
%setup  
%patch1
cp options README

%build
EXTRA_CFLAGS=""
%ifnarch ia64
    EXTRA_CFLAGS="$EXTRA_CFLAGS -Wa,--noexecstack"
%endif
make CFLAGS="$RPM_OPT_FLAGS $EXTRA_CFLAGS -fPIC -DHAVE_SHADOW -DLINUX_PAM"

%install
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security
make DESTDIR=$RPM_BUILD_ROOT install
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

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,755)
%doc CREDITS LICENSE README TROUBLESHOOTING 
%attr(644,root,root) %config(noreplace) /etc/security/chroot.conf
%attr(755,root,root) /%{_lib}/security/pam_*.so

%changelog
