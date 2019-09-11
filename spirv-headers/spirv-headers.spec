#
# spec file for package spirv-headers
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


%define version_unconverted 1.4.1.g36

Name:           spirv-headers
Version:        1.4.1.g36
Release:        0
Summary:        Machine-readable files from the SPIR-V registry
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/KhronosGroup/SPIRV-Headers

Source:         %name-%version.tar.xz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++

%description
This repository contains machine-readable files from the SPIR-V
registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file.

%prep
%setup -q

%build
# Because Khronos does not know what DESTDIR is.
%cmake -DCMAKE_INSTALL_PREFIX="%buildroot/%_prefix"
make %{?_smp_mflags}

%install
pushd build/
make install-headers
popd
%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%_includedir/spirv/
%doc LICENSE

%changelog
