#
# spec file for package shlomif-cmake-modules
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


Name:           shlomif-cmake-modules
Version:        8f5acb6450c1
Release:        0
Summary:        Shlomi Fish's CMake Modules
License:        MIT
Group:          Development/Tools/Other
URL:            https://bitbucket.org/shlomif/shlomif-cmake-modules/src/default/
Source0:        https://bitbucket.org/shlomif/shlomif-cmake-modules/get/%{version}.tar.gz#/shlomif-cmake-modules.tar.gz
BuildRequires:  cmake
Requires:       cmake
Requires:       perl
BuildArch:      noarch

%description
Shlomi Fish's CMake Modules

%prep
%setup -n shlomif-%{name}-%{version}

%build
:

%install
install -Dm 0644 %{name}/Shlomif_Common.cmake %{buildroot}%{_datadir}/cmake/Modules/Shlomif_Common.cmake

%files
%doc README.md
%license LICENSE
%{_datadir}/cmake/Modules/Shlomif_Common.cmake

%changelog
