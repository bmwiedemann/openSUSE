#
# spec file for package cmake-fedora
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


Name:           cmake-fedora
Version:        2.9.2
Release:        0
Summary:        CMake modules and scripts
License:        BSD-3-Clause
URL:            https://pagure.io/cmake-fedora
Source0:        https://releases.pagure.org/cmake-fedora/%{name}-%{version}-Source.tar.gz
BuildRequires:  cmake >= 2.6.2
Recommends:     %{name}-modules = %{version}-%{release}
BuildArch:      noarch

%description
cmake-fedora consists a set of scripts and cmake modules that simply the
release process of a *nix software package,  especially for
Fedora and EPEL.

%package modules
Summary:        CMake modules
Requires:       cmake >= 2.6.2

%description modules
cmake-fedora consists a set of scripts and cmake modules that simply the
release process of a *nix software package,  especially for
Fedora and EPEL.

%prep
%setup -q -n %{name}-%{version}-Source

%build
%cmake \
  -DCMAKE_FEDORA_ENABLE_FEDORA_BUILD=0 \
  -Wno-dev
%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc/

%files
%doc AUTHORS ChangeLog README.md RELEASE-NOTES.txt TODO.md
%license COPYING
%config %{_sysconfdir}/cmake-fedora.conf
%{_bindir}/cmake-fedora-fedpkg
%{_bindir}/cmake-fedora-koji
%{_bindir}/cmake-fedora-newprj
%{_bindir}/cmake-fedora-pkgdb
%{_bindir}/cmake-fedora-zanata
%{_bindir}/cmake-fedora-reset
%{_bindir}/koji-build-scratch
%{_datadir}/cmake/Templates/fedora

%files modules
%{_datadir}/cmake/Modules/CmakeFedoraScript.cmake
%{_datadir}/cmake/Modules/DateTimeFormat.cmake
%{_datadir}/cmake/Modules/ManageAPIDoc.cmake
%{_datadir}/cmake/Modules/ManageArchive.cmake
%{_datadir}/cmake/Modules/ManageChangeLogScript.cmake
%{_datadir}/cmake/Modules/ManageDependency.cmake
%{_datadir}/cmake/Modules/ManageEnvironment.cmake
%{_datadir}/cmake/Modules/ManageEnvironmentCommon.cmake
%{_datadir}/cmake/Modules/ManageFile.cmake
%{_datadir}/cmake/Modules/ManageGConf.cmake
%{_datadir}/cmake/Modules/ManageGettextScript.cmake
%{_datadir}/cmake/Modules/ManageGitScript.cmake
%{_datadir}/cmake/Modules/ManageMessage.cmake
%{_datadir}/cmake/Modules/ManageRPM.cmake
%{_datadir}/cmake/Modules/ManageRPMScript.cmake
%{_datadir}/cmake/Modules/ManageRelease.cmake
%{_datadir}/cmake/Modules/ManageReleaseFedora.cmake
%{_datadir}/cmake/Modules/ManageSourceVersionControl.cmake
%{_datadir}/cmake/Modules/ManageString.cmake
%{_datadir}/cmake/Modules/ManageTarget.cmake
%{_datadir}/cmake/Modules/ManageTranslation.cmake
%{_datadir}/cmake/Modules/ManageUninstall.cmake
%{_datadir}/cmake/Modules/ManageUpload.cmake
%{_datadir}/cmake/Modules/ManageVariable.cmake
%{_datadir}/cmake/Modules/ManageVersion.cmake
%{_datadir}/cmake/Modules/ManageZanata.cmake
%{_datadir}/cmake/Modules/ManageZanataDefinition.cmake
%{_datadir}/cmake/Modules/ManageZanataScript.cmake
%{_datadir}/cmake/Modules/ManageZanataSuggest.cmake
%{_datadir}/cmake/Modules/cmake_uninstall.cmake.in

%changelog
