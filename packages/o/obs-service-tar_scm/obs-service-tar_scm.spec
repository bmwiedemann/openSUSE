#
# spec file for package obs-service-tar_scm
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


%if 0%{?fedora_version}%{?rhel}
%define _pkg_base %nil
%else
%define _pkg_base -base
%endif

%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == ""
%define nsuffix %nil
%else
%define nsuffix -test
%endif

%if 0%{?suse_version} && 0%{?suse_version} >= 1220 && "%{flavor}" == "test"
%bcond_without obs_scm_testsuite
%else
%bcond_with    obs_scm_testsuite
%endif

# special guard for flavor test, yet --without test being specified
%if "%{flavor}" == "test" && %{without obs_scm_testsuite}
ExclusiveArch:  skip-build
%endif

%if 0%{?suse_version} >= 1315 || 0%{?fedora_version} >= 29 || 0%{?rhel} >= 8
%bcond_without python3
%else
%bcond_with    python3
%endif

# This list probably needs to be extended
# logic seems to be if python < 2.7 ; then needs_external_argparse ; fi
%if (0%{?centos_version} == 6) || (0%{?suse_version} && 0%{?suse_version} < 1315) || (0%{?fedora_version} && 0%{?fedora_version} < 26)
%bcond_without needs_external_argparse
%else
%bcond_with    needs_external_argparse
%endif

%if %{with python3}
%define use_python python3
%define use_test   test3
%else
%define use_python python
%define use_test   test
%endif

%if 0%{?suse_version}
%define pyyaml_package %{use_python}-PyYAML
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
%define locale_package glibc-locale-base
%else
%define locale_package glibc-locale
%endif
%endif

%if 0%{?fedora_version} || 0%{?rhel}
%if 0%{?fedora_version} >= 29 || 0%{?rhel} >= 8
%define pyyaml_package %{use_python}-PyYAML
%else
%define pyyaml_package PyYAML
%endif

%if 0%{?fedora_version} >= 24 || 0%{?rhel} >= 8
%define locale_package glibc-langpack-en
%else
%define locale_package glibc-common
%endif
%endif

%if 0%{?mageia} || 0%{?mandriva_version}
%define pyyaml_package python-yaml
%define locale_package locales
%endif

# Mageia 8 has package names python-*
# but requires python3 in shebang
%if 0%{?mageia} >= 8 || 0%{?rhel} >= 8
%define python_path %{_bindir}/python3
%else
%define python_path %{_bindir}/%{use_python}
%endif

# avoid code duplication
%define scm_common_dep                                          \
Requires:       obs-service-obs_scm-common = %version-%release  \
%{nil}

%define scm_dependencies                                        \
Requires:       git-core                                        \
%if 0%{?suse_version} >= 1315                                   \
Recommends:     bzr                                             \
Recommends:     mercurial                                       \
Recommends:     subversion                                      \
Recommends:     obs-service-download_files                      \
Recommends:     %{use_python}-keyring                           \
Recommends:     %{use_python}-keyrings.alt                      \
%endif                                                          \
%{nil}

######## END OF MACROS AND FUN ###################################

%define pkg_name obs-service-tar_scm
Name:           %{pkg_name}%{nsuffix}
%define version_unconverted 0.10.43
Version:        0.10.43
Release:        0
Summary:        An OBS source service: create tar ball from svn/git/hg
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-tar_scm
Source:         %{pkg_name}-%{version}.tar.gz

# Fix build on Ubuntu by disabling mercurial tests, not applied in rpm
# based distributions
#Patch0:         0001-Debianization-disable-running-mercurial-tests.patch

%if %{with obs_scm_testsuite}
BuildRequires:  %{locale_package}
BuildRequires:  %{pkg_name} = %{version}
BuildRequires:  %{use_python}-keyring
BuildRequires:  %{use_python}-keyrings.alt
BuildRequires:  %{use_python}-six
BuildRequires:  bzr
BuildRequires:  git-core
BuildRequires:  gpg
BuildRequires:  mercurial
BuildRequires:  subversion
%if !%{with python3}
BuildRequires:  %{use_python}-mock
%endif
%endif

BuildRequires:  %{locale_package}
BuildRequires:  %{pyyaml_package}
%if %{with needs_external_argparse}
BuildRequires:  %{use_python}-argparse
%endif
BuildRequires:  %{use_python}-dateutil
# Why do we need this? we dont use it as runtime requires later
BuildRequires:  %{use_python}-lxml

%if %{with python3}
BuildRequires:  %{use_python}%{_pkg_base}
# Fix missing Requires in python3-pbr in Leap42.3
BuildRequires:  %{use_python}-setuptools
%else
BuildRequires:  python >= 2.6
%endif
%scm_common_dep
%scm_dependencies
#
#
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       %{python_path}

%description
This is a source service for openSUSE Build Service.

It supports downloading from svn, git, hg and bzr repositories.

%package -n     obs-service-obs_scm-common
Summary:        Common parts of SCM handling services
Group:          Development/Tools/Building
Requires:       %{locale_package}
Requires:       %{pyyaml_package}
Requires:       %{use_python}-dateutil
%if %{with needs_external_argparse}
Requires:       %{use_python}-argparse
%endif

%description -n obs-service-obs_scm-common
This is a source service for openSUSE Build Service.

It supports downloading from svn, git, hg and bzr repositories.

This package holds the shared files for different services.

%package -n     obs-service-tar
Summary:        Creates a tar archive from local directory
Group:          Development/Tools/Building
Provides:       obs-service-tar_scm:/usr/lib/obs/service/tar.service
%scm_common_dep

%description -n obs-service-tar
Creates a tar archive from local directory

%package -n     obs-service-obs_scm
Summary:        Creates a OBS cpio from a remote SCM resource
Group:          Development/Tools/Building
Provides:       obs-service-tar_scm:/usr/lib/obs/service/obs_scm.service
%scm_common_dep
%scm_dependencies

%description -n obs-service-obs_scm
Creates a OBS cpio from a remote SCM resource.

This can be used to work directly in local git checkout and can be packaged
into a tar ball during build time.

%package -n     obs-service-appimage
Summary:        Handles source downloads defined in appimage.yml files
Group:          Development/Tools/Building
%scm_common_dep
%scm_dependencies

%description -n obs-service-appimage
Experimental appimage support: This parses appimage.yml files for SCM
resources and packages them.

%package -n     obs-service-snapcraft
Summary:        Handles source downloads defined in snapcraft.yaml files
Group:          Development/Tools/Building
Provides:       obs-service-tar_scm:/usr/lib/obs/service/snapcraft.service
%scm_common_dep
%scm_dependencies

%description -n obs-service-snapcraft
Experimental snapcraft support: This parses snapcraft.yaml files for SCM
resources and packages them.

%if 0%{?enable_gbp}
%package -n     obs-service-gbp
Summary:        Creates Debian source artefacts from a Git repository
Group:          Development/Tools/Building
Requires:       git-buildpackage >= 0.6.0
Requires:       obs-service-obs_scm-common = %version-%release
%if 0%{?enable_gbp}
Provides:       obs-service-tar_scm:/usr/lib/obs/service/obs_gbp.service
%endif

%description -n obs-service-gbp
Debian git-buildpackage workflow support: uses gbp to create Debian
source artefacts (.dsc, .origin.tar.gz and .debian.tar.gz if non-native).
%endif

%prep
%setup -q -n obs-service-tar_scm-%version

%build

%install
%if %{without obs_scm_testsuite}
make install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" SYSCFG="%{_sysconfdir}" PYTHON="%{python_path}" WITH_GBP="%{enable_gbp}"
# Doing %%python3_fix_shebang_path old fashioned way for the backward compatibility
sed -i "1s@#\\!.*python\S*@#\\!$(realpath %__python3)@" \
    %{buildroot}%{_prefix}/lib/obs/service/tar_scm

%else

# moved conditional to the top as it helps to have it all in one place and only rely on the bcond_with here.
%check
# No need to run PEP8 tests here; that would require a potentially
# brittle BuildRequires: python-pep8, and any style issues are already
# caught by Travis CI.
make %{use_test}
%endif

%if %{without obs_scm_testsuite}
%files
%defattr(-,root,root)
%{_prefix}/lib/obs/service/tar_scm.service

%files -n obs-service-obs_scm-common
%defattr(-,root,root)
%license COPYING
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/TarSCM
%{_prefix}/lib/obs/service/tar_scm
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%verify (not user group) %dir %{_sysconfdir}/obs/services/tar_scm.d
%config(noreplace) %{_sysconfdir}/obs/services/*
%ghost %dir %{_sysconfdir}/obs/services/tar_scm.d/python_keyring

%files -n obs-service-tar
%defattr(-,root,root)
%{_prefix}/lib/obs/service/tar
%{_prefix}/lib/obs/service/tar.service

%files -n obs-service-obs_scm
%defattr(-,root,root)
%{_prefix}/lib/obs/service/obs_scm
%{_prefix}/lib/obs/service/obs_scm.service

%files -n obs-service-appimage
%defattr(-,root,root)
%{_prefix}/lib/obs/service/appimage*

%files -n obs-service-snapcraft
%defattr(-,root,root)
%{_prefix}/lib/obs/service/snapcraft*

%if 0%{?enable_gbp}
%files -n obs-service-gbp
%defattr(-,root,root)
%{_prefix}/lib/obs/service/obs_gbp*
%endif
%endif

%changelog
