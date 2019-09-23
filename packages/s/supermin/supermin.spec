#
# spec file for package supermin
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


Name:           supermin
Version:        5.1.18
Release:        0
%{ocaml_preserve_bytecode}
Url:            http://libguestfs.org/
Summary:        Bootstrapping tool for creating supermin appliances
License:        GPL-3.0-or-later
Group:          System/Filesystems
Provides:       febootstrap
Requires:       distribution-release
Requires:       sysconfig-netconfig
Requires:       tar
Requires:       xmlstarlet
Requires:       zypper
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        supermin-%{version}.tar.xz
# Pending upstream review
Patch0:         suse_release.patch
%if "%{?_ignore_exclusive_arch}" == ""
ExclusiveArch:  x86_64 ppc64 ppc64le s390x aarch64
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs
BuildRequires:  glibc-devel-static
BuildRequires:  gzip
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(rpm)

%description
supermin is a tool for building supermin appliances. These are tiny
appliances (similar to virtual machines), usually around 100KB in size,
which get fully instantiated on-the-fly in a fraction of a second when
you need to boot one of them.

%prep
%setup -q
%patch0 -p1

%build
export ZYPPER=zypper
export ZYPPER=/usr/bin/zypper
touch INSTALL NEWS AUTHORS ChangeLog
autoreconf -fi
%configure --help
%configure
make \
	%{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -ls

%files
%defattr (-,root,root)
%doc README
%doc TODO
/usr/bin/*
%{_mandir}/*/*

%changelog
