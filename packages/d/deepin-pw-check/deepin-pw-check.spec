#
# spec file for package deepin-pw-check
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Hillwood Yang <hillwood@opensuse.org>
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


%define   with_pam        0
%define   sover           1
%define   provider        github
%define   provider_tld    com
%define   project         linuxdeepin
%define   repo            deepin-pw-check
# https://github.com/linuxdeepin/deepin-pw-check
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     %{provider_prefix}

Name:           deepin-pw-check
Version:        5.1.16
Release:        0
License:        GPL-3.0-or-later
Summary:        Deepin Password Check tool
URL:            https://github.com/linuxdeepin/deepin-pw-check
Group:          Productivity/Security
Source0:        https://github.com/linuxdeepin/deepin-pw-check/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE disable-gobuild-in-makefile.patch hillwood@opensuse.org - Use go macro instead of make
Patch0:         disable-gobuild-in-makefile.patch
# PATCH-FIX-UPSTREAM fix-missing-header.patch hillwood@opensuse.org - Missing include stdlib.h
Patch1:         fix-missing-header.patch
BuildRequires:  gcc
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150300
BuildRequires:  golang(github.com/stretchr/testify/mock)
%endif
BuildRequires:  cracklib-devel
BuildRequires:  deepin-gettext-tools
BuildRequires:  golang-github-linuxdeepin-go-dbus-factory
BuildRequires:  golang-github-linuxdeepin-go-lib
BuildRequires:  golang-packaging
BuildRequires:  libiniparser-devel
BuildRequires:  pam
BuildRequires:  pam-devel
BuildRequires:  polkit
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-2.0)
AutoReqProv:    Off

%description
deepin-pw-check is a tool to verify the validity of the password

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        Deepin-pw-check source
Group:          Development/Languages/Golang
Requires:       golang-github-linuxdeepin-go-dbus-factory
AutoReq:        Off
BuildArch:      noarch

%description -n golang-%{provider}-%{project}-%{repo}
This package contains source of deepin-pw-check
libraries that are developed by the Go team but outside of the main source tree.

%package -n libdeepin_pw_check%{sover}
Summary:        Deepin-pw-check libraries
Group:          System/Libraries

%description -n libdeepin_pw_check%{sover}
This package contains the libraries for IBus

%package devel
Summary:        Development tools for deepin-pw-check
Group:          Development/Libraries/Other
Requires:       libdeepin_pw_check%{sover} = %{version}

%description devel
The deepin-pw-check-devel package contains the header files and developer
docs for deepin-pw-check.

%lang_package

%prep
%autosetup -p1 -a1 -n %{name}-%{version}
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150300
rm -rf vendor/github.com/stretchr/testify/
%endif
%if 0%{?suse_version} > 1500
mkdir -p $HOME/rpmbuild/BUILD/%{name}-%{version}-build/go/src/
cp vendor/* $HOME/rpmbuild/BUILD/%{name}-%{version}-build/go/src/ -r
%else
mkdir -p $HOME/rpmbuild/BUILD/go/src/
cp vendor/* $HOME/rpmbuild/BUILD/go/src/ -r
%endif
rm -rf vendor
sed -i 's|<iniparser/|<|g' tool/pwd_conf_update.c lib/deepin_pw_check.c
sed -i '/<allow_any>/s|no|auth_admin|g' misc/polkit-action/*

%build
export GO111MODULE=off
%goprep %{import_path}
%gobuild ...
%make_build

%install
%if 0%{?suse_version} > 1500
rm -rf $HOME/rpmbuild/BUILD/%{name}-%{version}-build/go/src/github.com \
       $HOME/rpmbuild/BUILD/%{name}-%{version}-build/go/src/golang.org \
       $HOME/rpmbuild/BUILD/%{name}-%{version}-build/go/src/gopkg.in
%else
rm -rf $HOME/rpmbuild/BUILD/go/src/github.com \
       $HOME/rpmbuild/BUILD/go/src/golang.org \
       $HOME/rpmbuild/BUILD/go/src/gopkg.in
%endif
%goinstall
%gosrc
cp %{buildroot}%{_bindir}/* out/bin/deepin-pw-check
rm %{buildroot}%{_bindir}/*
%make_install LIBDIR=%{_libdir} \
              PKG_FILE_DIR=%{_libdir}/pkgconfig \
              PAM_MODULE_DIR=/%{_lib}/security
%gofilelist

%if %{with_pam}
%else
rm %{buildroot}/%{_lib}/security/pam_deepin_pw_check.so
%endif
rm %{buildroot}%{_datadir}/dbus-1/system-services/com.deepin.daemon.PasswdConf.service \
   %{buildroot}%{_datadir}/dbus-1/system.d/com.deepin.daemon.PasswdConf.conf \
   %{buildroot}%{_datadir}/polkit-1/actions/com.deepin.daemon.passwdconf.policy

find %{buildroot} -type f -name "*.a" -delete -print

%find_lang %{name}

%post -n libdeepin_pw_check%{sover} -p /sbin/ldconfig
%postun -n libdeepin_pw_check%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/pwd-conf-update
%{_prefix}/lib/deepin-pw-check
%if %{with_pam}
/%{_lib}/security/pam_deepin_pw_check.so
%endif
# %{_datadir}/dbus-1/system-services/com.deepin.daemon.PasswdConf.service
# %{_datadir}/dbus-1/system.d/com.deepin.daemon.PasswdConf.conf
# %{_datadir}/polkit-1/actions/com.deepin.daemon.passwdconf.policy

%files -n libdeepin_pw_check%{sover}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%doc README.md
%license LICENSE
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdeepin_pw_check.pc
%{_includedir}/*.h

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%doc README.md
%license LICENSE

%files lang -f %{name}.lang

%changelog
