#
# spec file for package linux-enable-ir-emitter
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} < 1600
# c++20 support incl. <format> required
%define gcc_ver 13
%endif
Name:           linux-enable-ir-emitter
Version:        6.1.2
Release:        0
Summary:        Support for infrared cameras that are not directly enabled out-of-the box
License:        MIT
URL:            https://github.com/EmixamPP/linux-enable-ir-emitter
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(argparse)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(yaml-cpp)

%description
linux-enable-ir-emitter provides support for infrared cameras that are not
directly enabled out-of-the box (at the very least, the kernel must recognize
your infrared camera). It can automatically configure almost any (UVC) infrared
emitter.

%prep
%autosetup -p1

%build
%if 0%{?gcc_ver}
export CXX=g++-%{gcc_ver}
%endif
%meson \
  -Dcreate_config_dir=true \
  -Dcreate_log_dir=true \
  -Dtests=true \
  %{nil}
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_sysconfdir}/systemd/system/%{name}.service \
   %{buildroot}%{_unitdir}/%{name}.service

sed -Ei "1{\@/bin/bash@d}" %{buildroot}%{_datadir}/bash-completion/completions/%{name}

rm -fr %{buildroot}%{_datadir}/doc/*

%check
%meson_test linux-enable-ir-emitter

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/
%{_datadir}/zsh/
%{_unitdir}/*.service
%dir %{_sysconfdir}/%{name}
%dir %{_localstatedir}/log/%{name}

%changelog
