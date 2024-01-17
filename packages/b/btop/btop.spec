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


Name:           btop
Version:        1.3.0+git20240107.36842a3
Release:        0
Summary:        Usage and stats for processor, memory, disks, network and processes
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/aristocratos/btop
Source:         %{name}-%{version}.tar.gz
Patch0:         Makefile.diff
BuildRequires:  coreutils
%if 0%{?suse_version} < 1550
BuildRequires:  gcc13-c++
%define cxxflags CXXFLAGS="%{optflags} -fPIE"
%define cxxopt CXX="g++-13"
%define lddopt LDCXXFLAGS="-ldl -lpthread -pie"
%else
BuildRequires:  gcc-c++ >= 11
%define cxxflags %{nil}
%define cxxopt %{nil}
%define lddopt %{nil}
%endif
BuildRequires:  sed

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes. C++ version and continuation of bashtop and bpytop.

%prep
%setup -q
%patch0

%build
%make_build %{cxxflags} %{cxxopt} %{lddopt}

%install
%make_install %{cxxopt} %{lddopt} PREFIX=%{_prefix}

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
%license LICENSE

%changelog
