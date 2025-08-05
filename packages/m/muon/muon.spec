#
# spec file for package muon
#
# Copyright (c) 2025 Eyad Issa
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


%if %{suse_version} >= 1600
  %bcond_without docs
%else
  %bcond_with docs
%endif

Name:           muon
Version:        0.5.0
Release:        0
Summary:        An implementation of the meson build system in c99
License:        Apache-2.0 AND GPL-3.0-only
URL:            https://muon.build/
Source0:        https://muon.build/releases/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpkgconf)
%if 0%{with docs}
BuildRequires:  scdoc
%endif

%description
muon is an implementation of the meson build system in c99 with
minimal dependencies.

%prep
%autosetup -n %{name}-v%{version}

%build
%global _builddir         %{_target_platform}
%global _builddir_stage0  %{_builddir}/muon-stage0
%global _builddir_stage1  %{_builddir}/muon-stage1
%global _builddir_stage2  %{_builddir}/muon-stage2

%{set_build_flags}
export CC="gcc"

# there are two way to build muon, either using meson or bootstrapping
# from scratch
# we will use the bootstrap method here

# stage 0: build from amalgam source
./bootstrap.sh %{_builddir_stage0}

# stage 1: build using muon
%{_builddir_stage0}/muon-bootstrap setup %{_builddir_stage1}
%{_builddir_stage0}/muon-bootstrap -C %{_builddir_stage1} samu -v %{?_smp_mflags}

# stage 2: build again using the new muon
%{_builddir_stage1}/muon setup \
  -Dprefix=%{_prefix} \
%if 0%{with docs}
  -Dman-pages=enabled \
%endif
  -Dlibpkgconf=enabled \
  -Dlibcurl=enabled \
  -Dlibarchive=enabled \
  -Dsamurai=enabled \
  %{_builddir_stage2}

%{_builddir_stage1}/muon -C %{_builddir_stage2} samu -v %{?_smp_mflags}

%install
export DESTDIR=%{buildroot}
%{_builddir_stage1}/muon -C %{_builddir_stage2} install

%files
%license LICENSES/*
%doc README.md
%{_bindir}/muon
%if 0%{with docs}
%{_mandir}/man1/muon.1%{?ext_man}
%{_mandir}/man5/meson.build.5%{?ext_man}
%endif

%changelog
