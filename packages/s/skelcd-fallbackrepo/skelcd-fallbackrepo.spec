#
# spec file for package skelcd-fallbackrepo
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# needsbinariesforbuild


%if "@BUILD_FLAVOR@" == ""
ExclusiveArch:  do_not_build
%endif

%global flavor @BUILD_FLAVOR@%nil

# SLE but not Leap
%if 0%{?sle_version} && !0%{?is_opensuse}
%define sle_only 1
%else
%define sle_only 0
%endif

# ===  sort out which flavor to build  ===

%if "%flavor" == "openSUSE"
%if 0%{?is_opensuse}
%define theme openSUSE
%endif
%endif

%if "%flavor" == "SLED"
# build SLED only on x86_64
%if %sle_only && "%{_target_cpu}" == "x86_64"
%define theme SLED
%endif
%endif

%if "%flavor" == "SLES"
%if %sle_only
%ifnarch %ix86
%define theme SLES
%endif
%endif
%endif

%if "%flavor" == "SLES_SAP"
%if %sle_only && ( "%{_target_cpu}" == "x86_64" || "%{_target_cpu}" == "ppc64le" )
%define theme SLES_SAP
%endif
%endif

%if "%flavor" == "SLE_HPC"
%if %sle_only && ( "%{_target_cpu}" == "x86_64" || "%{_target_cpu}" == "aarch64" )
%define theme SLE_HPC
%endif
%endif

%if "%flavor" == "SLE_RT"
%if %sle_only && ( "%{_target_cpu}" == "x86_64" )
%define theme SLE_RT
%endif
%endif

%if "%flavor" == "CAASP"
%if 0%{?is_susecaasp}
%ifnarch %ix86
%define theme CAASP
%endif
%endif
%endif

# ===  define each theme  ===

%if "%{?theme}" == ""
ExclusiveArch:  do_not_build
%endif

%if "%theme" == "openSUSE"
%define skelcd_control openSUSE
%define prod_release   openSUSE
%endif

%if "%theme" == "SLED"
%define skelcd_control SLED
%define prod_release   sled
%endif

%if "%theme" == "SLES"
%define skelcd_control SLES
%define prod_release   sles
%endif

%if "%theme" == "SLES_SAP"
%define skelcd_control SLES4SAP
%define prod_release   SLES_SAP
%endif

%if "%theme" == "SLE_HPC"
%define skelcd_control SLE_HPC
%define prod_release   SLE_HPC
%endif

%if "%theme" == "SLE_RT"
%define skelcd_control SLE_RT
%define prod_release   SLE_RT
%endif

%if "%theme" == "CAASP"
%define skelcd_control CAASP
%define prod_release   caasp
%endif

BuildRequires:  %{prod_release}-release
BuildRequires:  skelcd-control-%{skelcd_control}

%if "@BUILD_FLAVOR@" == ""
# This package is never built - but it helps the bots seeing that this package
# is intentionally as messed up as it is
Name:           skelcd-fallbackrepo
%else
Name:           skelcd-fallbackrepo-%{theme}
%endif
AutoReqProv:    off
Summary:        Packages for %theme to include in fallback repository
License:        MIT
Group:          Metapackages
Url:            https://github.com/yast/skelcd-fallbackrepo
Version:        1.1
Release:        0
Provides:       skelcd-fallbackrepo = %version-%release
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description -n skelcd-fallbackrepo-%{theme}
Packages to include in fallback repository for %theme. The fallback repository is
part of the installation system.

%prep

%build

%install
mkdir -p %{buildroot}/var/lib/fallback-repo
for i in skelcd-control-%{skelcd_control} %{prod_release}-release ; do
  cp /.build.binaries/$i.rpm %{buildroot}/var/lib/fallback-repo
done

%files -n skelcd-fallbackrepo-%{theme}
/var/lib/fallback-repo

%changelog
