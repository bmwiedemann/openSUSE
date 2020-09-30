#
# spec file for package sysdig
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sysdig
Version:        0.27.0
Release:        0
Summary:        System-level exploration
License:        Apache-2.0
Group:          System/Monitoring
URL:            http://www.sysdig.org/
Source0:        https://github.com/draios/%{name}/archive/%{version}/sysdig-%{version}.tar.gz
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libb64-devel
BuildRequires:  libjq-devel
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    %{arm} aarch64
%kernel_module_package

%description
Sysdig is open source, system-level exploration: capture system state and
activity from a running Linux instance, then save, filter and analyze.
Think of it as strace + tcpdump + lsof + awesome sauce. With a little Lua
cherry on top.

%prep
%autosetup

%build
export SYSDIG_CHISEL_DIR=%{_datadir}%{name}/chisels
%cmake \
  -DUSE_BUNDLED_JSONCPP=OFF \
  -DUSE_BUNDLED_LUAJIT=OFF \
  -DUSE_BUNDLED_ZLIB=OFF \
  -DUSE_BUNDLED_TBB=OFF \
  -DUSE_BUNDLED_NCURSES=OFF \
  -DUSE_BUNDLED_OPENSSL=OFF \
  -DUSE_BUNDLED_CURL=OFF \
  -DUSE_BUNDLED_B64=OFF \
  -DUSE_BUNDLED_JQ=OFF \
  -DUSE_BUNDLED_CARES=OFF \
  -DUSE_BUNDLED_PROTOBUF=OFF \
  -DUSE_BUNDLED_GRPC=OFF \
  -DCREATE_TEST_TARGETS=OFF \
  -DDIR_ETC=%{_sysconfdir} \
  -DBUILD_DRIVER=OFF \
  -Wno-dev
%cmake_build

%install
export INSTALL_MOD_PATH=%{buildroot}
%cmake_install
cd build
for flavor in %{flavors_to_build} ; do
	make KERNELDIR="%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor" \
	 clean install_driver DESTDIR=%{buildroot}
done
rm -rf %{buildroot}%{_prefix}/src/*
%fdupes -s %{buildroot}/%{_datadir}

%files
%license COPYING
%doc README.md
%config %{_sysconfdir}/bash_completion.d/sysdig
%{_bindir}/sysdig
%{_bindir}/csysdig
%{_bindir}/sysdig-probe-loader
%{_mandir}/man8/sysdig.8%{?ext_man}
%{_mandir}/man8/csysdig.8%{?ext_man}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/site-functions/_sysdig
%{_datadir}/zsh/vendor-completions/_sysdig
%{_datadir}/sysdig

%changelog
