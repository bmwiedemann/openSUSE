#
# spec file for package pam_userpass
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pam_userpass
Version:        1.0.2
Release:        0
Summary:        Uses PAM Binary Prompts to Ask Applications for Username/Password
License:        ISC
URL:            https://www.openwall.com/pam/
Source0:        https://www.openwall.com/pam/modules/pam_userpass/pam_userpass-%{version}.tar.gz
Source1:        baselibs.conf
Source50:       dlopen.sh
Patch0:         pam_userpass-1.0.diff
BuildRequires:  pam-devel
Requires:       pam
Provides:       pam-modules:/%{_lib}/security/pam_userpass.so

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

pam_userpass uses PAM binary prompts to ask the application for the
username and password.

%prep
%autosetup

%build
EXTRA_CFLAGS="-fno-strict-aliasing -Iinclude"
make %{?_smp_mflags} CFLAGS="%{optflags} $EXTRA_CFLAGS -fPIC -DHAVE_SHADOW -DLINUX_PAM"

%install
mkdir -p %{buildroot}/%{_lib}/security
%make_install
#
# Remove stuff we don't wish to have now:
#
rm -rf %{buildroot}%{_prefix}/{include,lib}
find %{buildroot} -type f -name "*.la" -delete -print
#
# On 64bit archs, we need to move same libraries ourself:
#
if [ %{_lib} = lib64 ]; then
  mv %{buildroot}/lib/security/* %{buildroot}/%{_lib}/security/
fi
# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
for module in %{buildroot}/%{_lib}/security/pam*.so ; do
   if ! sh $RPM_SOURCE_DIR/dlopen.sh -lpam -ldl ${module} ; then
      exit 1
   fi
done

%files
%defattr(-,root,root,755)
%license LICENSE
%doc README conf/*
%attr(755,root,root) /%{_lib}/security/pam_*.so

%changelog
