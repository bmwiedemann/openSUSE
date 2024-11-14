#
# spec file for package rpm-config-SUSE
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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


# ignore the explicit bash requires from the kernel mod scripts
%define __requires_exclude ^/bin/bash$
Name:           rpm-config-SUSE
Version:        20241031
Release:        0
Summary:        SUSE specific RPM configuration files
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/openSUSE/rpm-config-SUSE
Source:         %{name}-%{version}.tar.zst
BuildRequires:  zstd
#!BuildIgnore:  rpm-config-SUSE
# RPM owns the directories we need
Requires:       rpm
BuildArch:      noarch

%description
This package contains the RPM configuration data for the SUSE and
openSUSE distribution families.

%prep
%setup -q

%build
# Set up the SUSE Linux version macros
sed -e 's/@suse_version@/%{?suse_version}%{!?suse_version:0}/' \
    -e 's/@sles_version@/%{?sles_version}%{!?sles_version:0}/' \
    -e 's/@ul_version@/%{?ul_version}%{!?ul_version:0}/' \
    -e '/@is_opensuse@%{?is_opensuse:nomatch}/d' \
    -e 's/@is_opensuse@/%{?is_opensuse}%{!?is_opensuse:0}/' \
%if 0%{?is_opensuse}
    -e '/@sle_version@%{?sle_version:nomatch}/d' \
    -e 's/@sle_version@/%{?sle_version}%{!?sle_version:0}/' \
%else
    -e '/@sle_version@/d' \
%endif
  < suse_macros.in > suse_macros

%if 0%{?is_opensuse}
# use latest build date of BuildRequires as reference and go to January 1st three years back - the + 6 * 3600 is to match exactly the previous value of 2020-01-01 00:00 as leap-years cause some hours of offset
trimdate=$(rpm -qa --qf %{BUILDTIME}\\n |sort -n|tail -1)
trimdate=$(( (trimdate / 31557600 - 3) * 31557600 + 6 * 3600 ))
cat <<EOF > macros.d/macros.opensuse
# trim binary changelogs to include roughly 3 years
# maxnum,cuttime,minnum
%%_binarychangelogtrim 0,$trimdate,10
EOF
%endif

%install
# Install SUSE vendor macros and rpmrc
mkdir -p %{buildroot}%{_rpmconfigdir}/suse
cp -a suse_macros %{buildroot}%{_rpmconfigdir}/suse/macros

# Install vendor dependency generators
cp -a fileattrs %{buildroot}%{_rpmconfigdir}
cp -a scripts/* %{buildroot}%{_rpmconfigdir}
cp -a macros.d %{buildroot}%{_rpmconfigdir}

%files
%license COPYING
%doc README.md
%{_rpmconfigdir}/suse/
%{_rpmconfigdir}/macros.d/macros.*
%{_rpmconfigdir}/fileattrs/*
%{_rpmconfigdir}/brp-suse
%{_rpmconfigdir}/firmware.prov
%{_rpmconfigdir}/sysvinitdeps.sh
%{_rpmconfigdir}/locale.prov
# kmod deps
%{_rpmconfigdir}/find-provides.ksyms
%{_rpmconfigdir}/find-requires.ksyms
%{_rpmconfigdir}/find-supplements.ksyms

%changelog
