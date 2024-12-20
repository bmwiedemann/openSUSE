#
# spec file for package uisp
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files uisp_parport.conf

%define prefix /usr/avr

Name:           uisp
BuildRequires:  automake
BuildRequires:  gcc-c++
%define use_fastpoll		1
%define upstream_version	20050207
Version:        20050207suse
Release:        0
URL:            http://savannah.nongnu.org/projects/uisp
Summary:        An upload tool for AVR microcontrollers
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
Source:         http://savannah.nongnu.org/download/%{name}/%{name}-%{upstream_version}.tar.gz
Source1:        resmgr.uisp_parport.conf
Source2:        modprobe.uisp_parport
Provides:       avr-programmer
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         /bin/cat
PreReq:         /sbin/modprobe
Patch1:         uisp_fastpoll_3712.patch
Patch2:         uisp-20050207-2313+48.diff
Patch3:         uisp-20050207-err_msg.diff
Patch4:         uisp-20050207-warn-unused.diff
Patch5:         uisp-20050207suse.diff
Patch6:         uisp-20050207-m168-stk500-extendedFuseSupport.patch
Patch7:         stk500_pgzs_shift.diff
Patch8:         uisp-20050207-reproducible.patch

%description
Uisp is a tool for AVR microcontrollers and drives many hardware
in-system programmers. Uisp allows programming a microcontroller
through the parallel port.

%prep
%setup -n %{name}-%{upstream_version}
%if %{use_fastpoll}
%patch -P 1 -p1
%else
%patch -P 2 -p1
%endif
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1

%build
touch README
sed -i -e "s@\-Werror@@g" src/Makefile.am
autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%prefix --mandir=/usr/share/man
make

%install
%make_install
mkdir -p %{buildroot}/usr/share/doc/packages
mv %{buildroot}/%prefix/share/doc/%{name}-%{upstream_version} \
   %{buildroot}/usr/share/doc/packages/uisp
rmdir %{buildroot}/%prefix/share/doc
rmdir %{buildroot}/%prefix/share
mkdir -p       %{buildroot}/etc/resmgr.conf.d
# no longer works for 10.2 see bugzilla #235059
# install -m 644 %{SOURCE1} %{buildroot}/etc/resmgr.conf.d/99-uisp_parport.conf
mkdir -p       %{buildroot}%{_modprobedir}
install -m 644 %{SOURCE2} %{buildroot}%{_modprobedir}/uisp_parport.conf

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%post
%if %suse_version >= 1000
if [ "$1" -eq 1 ]; then
  # $1==0 is binary uninstall.
  # $1==1 is binary install.
  # $1==2 is during build
  if [  "$YAST_IS_RUNNING" = "yes" ]; then
    # make life trivial for yast users.
    test -x /usr/sbin/rcresmgr && /usr/sbin/rcresmgr restart
    /sbin/modprobe ppdev
  fi
fi
%endif

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%files
%defattr (-, root, root)
%doc AUTHORS CHANGES COPYING ChangeLog* CHANGES.old INSTALL NEWS TODO
%doc /usr/share/man/man?/*.*
%dir %prefix
%prefix/*
%config /etc/*
%dir %{_modprobedir}
%{_modprobedir}/uisp_parport.conf

%changelog
