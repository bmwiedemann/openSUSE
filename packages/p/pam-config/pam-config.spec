#
# spec file for package pam-config
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pam-config
Version:        1.9
Release:        0
Summary:        Utility to modify common PAM configuration files
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/SUSE/pam-config
Source:         %{name}-%{version}.tar.xz
# Do not show some rpmlint errors.
Source1:        pam-config-rpmlintrc
PreReq:         pam >= 1.3.0
Recommends:     pam_pwquality

%description
pam-config is a command line utility to maintain the common PAM
configuration files included by most PAM application configuration
files. It can be used to configure a system for different network or
hardware based authentication schemes. pam-config can also
add/adjust/remove other PAM modules and their options.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/%{_sysconfdir}/pam.d
for i in account auth password session ; do
  touch %{buildroot}/%{_sysconfdir}/pam.d/common-$i-pc
done
%find_lang pam-config

%post
if [ ! -f %{_sysconfdir}/pam.d/common-auth-pc ] ; then
  pam-config --debug --create --force
else
  pam-config --debug --update ||:
fi

%postun
if [ $1 = 0 ]; then
  # Deinstall
  dir=%{_sysconfdir}/security
  for conf in pam_unix2.conf pam_pwcheck.conf ; do
    if [ -f $dir/$conf.pam-config-backup -a ! -f $dir/$conf ]; then
      mv -v $dir/$conf.pam-config-backup $dir/$conf
    fi
  done
  dir=%{_sysconfdir}/pam.d
  for pamd in common-account common-auth common-password common-session ; do
    if [ -f $dir/$pamd.pam-config-backup -a -L $dir/$pamd ]; then
      rm -v $dir/$pamd && mv -v $dir/$pamd.pam-config-backup $dir/$pamd
    fi
    # common-*-pc are ghost, so we have to move them away...
    if [ -f $dir/$pamd-pc ]; then
      mv -v $dir/$pamd-pc $dir/$pamd-pc.bak
    fi
  done
fi

%triggerpostun -- pam-modules
[ $2 = 0 ] || exit 0
pam-config --debug --update ||:

%files -f pam-config.lang
%license COPYING
%{_sbindir}/pam-config
%{_mandir}/man8/pam-config.8*
%ghost %config %{_sysconfdir}/pam.d/common-account-pc
%ghost %config %{_sysconfdir}/pam.d/common-auth-pc
%ghost %config %{_sysconfdir}/pam.d/common-password-pc
%ghost %config %{_sysconfdir}/pam.d/common-session-pc

%changelog
