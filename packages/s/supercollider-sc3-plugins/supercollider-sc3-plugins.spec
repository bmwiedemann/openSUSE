#
# spec file for package supercollider-sc3-plugins
#
# Copyright (c) 2023 SUSE LLC
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


%define build_supernova 1
# what extra options to compile with
%define cmakearch -DSSE=OFF
%ifarch x86_64
%define cmakearch -DSSE=ON -DX86_64=ON
%endif
%ifarch %{ix86}
%define cmakearch -DSSE=ON -DI686=ON
%endif
# options to build supernova
%if 0%{?build_supernova}
%define cmakesupernova -DSUPERNOVA=ON
%else
%define cmakesupernova -DSUPERNOVA=OFF
%endif
Name:           supercollider-sc3-plugins
Version:        3.13.0
Release:        0
Summary:        Collection of SuperCollider plugins
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://supercollider.github.io/sc3-plugins/
Source0:        https://github.com/supercollider/sc3-plugins/releases/download/Version-%{version}/sc3-plugins-%{version}-Source.tar.bz2
Source1:        https://github.com/supercollider/sc3-plugins/releases/download/Version-%{version}/sc3-plugins-%{version}-Source.tar.bz2.asc
Source9:        supercollider-sc3-plugins.keyring
Source99:       supercollider-sc3-plugins-rpmlintrc
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  supercollider-devel
Requires:       supercollider >= 3.5

%description
Collection of free and usefull SuperCollider plugins

%prep
%setup -q -n sc3-plugins-%{version}-Source

%build
%ifarch ppc ppc64 ppc64le
export CFLAGS='%{optflags} -mno-altivec'
export CXXFLAGS='%{optflags} -mno-altivec'
%endif
%cmake \
	-DSC_PATH=%{_includedir}/SuperCollider \
	%{cmakearch} \
	-DQUARKS=ON \
	%{?cmakesupernova}
%make_build clean
%make_build

%install
cd build
%make_install
%fdupes %{buildroot}%{_prefix}

%files
%license license.txt
%doc README.md
%dir %{_datadir}/SuperCollider
%dir %{_datadir}/SuperCollider/SC3plugins
%{_datadir}/SuperCollider/SC3plugins
%dir %{_libdir}/SuperCollider
%dir %{_libdir}/SuperCollider/plugins
%{_libdir}/SuperCollider/plugins

%changelog
