#
# spec file for package libmp4tag
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 2_0_0
Name:           libmp4tag
Version:        2.0.0
Release:        0
Summary:        MP4 tagging library
License:        Zlib
URL:            https://libmp4tag.sourceforge.io/
Source:         https://sourceforge.net/projects/libmp4tag/files/%{name}-src-%{version}.tar.gz
Patch0:         libmp4tag-2.0.0-remove-rpath.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.18

%description
An MP4 tagging library where all tags can be accessed and modified. Any tags,
unknown tags or custom tags are never lost when the audio file is updated. A
list of known tags is only used when new tags are added.

%package -n %{name}%{sover}
Summary:        MP4 tagging library

%description -n %{name}%{sover}
An MP4 tagging library where all tags can be accessed and modified. Any tags,
unknown tags or custom tags are never lost when the audio file is updated. A
list of known tags is only used when new tags are added.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
An MP4 tagging library where all tags can be accessed and modified. Any tags,
unknown tags or custom tags are never lost when the audio file is updated. A
list of known tags is only used when new tags are added.

This package contains files requires for development using %{name}.

%package tools
Summary:        Development files for %{name}

%description tools
An MP4 tagging library where all tags can be accessed and modified. Any tags,
unknown tags or custom tags are never lost when the audio file is updated. A
list of known tags is only used when new tags are added.

This package contains the CLI tools built from %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DCMAKE_PROJECT_VERSION="%{version}" \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{name}%{sover}

%files tools
%license LICENSE.txt
%doc README.txt
%{_bindir}/mp4tagcli
%{_mandir}/man1/mp4tagcli.1%{?ext_man}

%files -n %{name}%{sover}
%license LICENSE.txt
%{_libdir}/libmp4tag.so.*

%files devel
%license LICENSE.txt
%{_includedir}/*.h
%{_libdir}/libmp4tag.so
%{_libdir}/pkgconfig/libmp4tag.pc
%{_mandir}/man3/libmp4tag.3%{?ext_man}

%changelog
