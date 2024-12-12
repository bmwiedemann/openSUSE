#
# spec file for package btop
#
# Copyright (c) 2024 SUSE LLC
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

%define ROCm_version 6.3.0
Name:           btop
Version:        1.4.0+git20241108.e17bc6b
Release:        0
Summary:        Usage and stats for processor, memory, disks, network and processes
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/aristocratos/btop
Source0:        %{name}-%{version}.tar.gz
### osc service runall download_files
Source1:        https://github.com/ROCm/rocm_smi_lib/archive/refs/tags/rocm-%{ROCm_version}.tar.gz#/rocm_smi_lib-rocm-%{ROCm_version}.tar.gz
#####
Source99:       btop-rpmlintrc
Patch0:         Makefile.diff
BuildRequires:  coreutils
BuildRequires:  cmake
%if 0%{?suse_version} < 1550
BuildRequires:  gcc13-c++
%define cxxflags CXXFLAGS="%{optflags} -fPIE"
%define cxxopt CXX="g++-13"
### Throws:
# ... relocation R_X86_64_32S against hidden symbol `_ZTVN3fmt3v1012format_errorE' can not be used when
#   making a PIE object ..." error when '-pie' is used
#%%define lddopt LDCXXFLAGS="-ldl -lpthread -pie -DFMT_HEADER_ONLY"
#####
%define lddopt LDCXXFLAGS="-ldl -lpthread -DFMT_HEADER_ONLY"
%else
BuildRequires:  gcc-c++ >= 11
BuildRequires:  lowdown
%define cxxflags %{nil}
%define cxxopt %{nil}
%define lddopt %{nil}
%endif
BuildRequires:  sed

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes. C++ version and continuation of bashtop and bpytop.

%prep
%autosetup -p0
cd %{_builddir}/%{name}-%{version}
mkdir -vp %{_builddir}/%{name}-%{version}/lib/rocm_smi_lib
tar zxf %{SOURCE1} -C %{_builddir}/%{name}-%{version}/lib/rocm_smi_lib --strip-components=1

%build
###
### RSMI_STATIC will break with gcc-14, as of <= v6.1.2 (20240606)
###
%make_build %{cxxflags} %{cxxopt} %{lddopt} RSMI_STATIC=true

%install
%make_install %{cxxopt} %{lddopt} PREFIX=%{_prefix}
chmod -c 644 %{buildroot}%{_datadir}/%{name}/themes/*.theme

%files
%doc CHANGELOG.md README.md
%{_bindir}/btop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/%{name}/themes/*.theme
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%if 0%{?suse_version} > 1550
%{_mandir}/man1/%{name}.1.gz
%endif
%license LICENSE

%changelog
