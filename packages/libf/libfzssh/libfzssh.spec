#
# spec file for package libfzssh
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover		13
%define soname		%{sover}_0_0
%define libname		%{name}%{soname}
%define develname	%{name}-devel

%define libfilezillaversion 0.55.3

Name:           libfzssh
Version:        1.3.0
Release:        0
Summary:        A C++ SSH/SFTP library based on libfilezilla
License:        AGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://fzssh.filezilla-project.org/
#Source0:        https://download.filezilla-project.org/fzssh/%%{name}-%%{version}.tar.xz
Source0:        fzssh-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libfilezilla) >= %{libfilezillaversion}
BuildRequires:  pkgconfig(libargon2)

%description
fzssh is a SSH/SFTP library based on libfilezilla.

%package -n	%{libname}
Summary:        A C++ SSH/SFTP library based on libfilezilla
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n	%{libname}
fzssh is a SSH/SFTP library based on libfilezilla

%package -n	%{develname}
Summary:        Development package for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description -n	%{develname}
Files needed for development with %{name}.

%prep
%autosetup -p1 -n fzssh-%{version}

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{libname}

%files
%license agpl3.txt
%doc README

%files -n %{libname}
%license agpl3.txt
%doc README
%{_libdir}/%{name}.so.%{sover}.0.0
%{_libdir}/%{name}-client.so.%{sover}.0.0
%{_libdir}/%{name}-crypt.so.%{sover}.0.0

%files -n %{develname}
%{_includedir}/fzssh/
%{_libdir}/%{name}.so
%{_libdir}/%{name}-client.so
%{_libdir}/%{name}-crypt.so
%{_libdir}/pkgconfig/%{name}-client.pc

%changelog
