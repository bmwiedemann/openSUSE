#
# spec file for package rpm-config-SUSE
#
# Copyright (c) 2022 SUSE LLC
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


Name:           rpm-config-SUSE
Version:        20220926
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
%if 0%{?usrmerged}
    -e 's/@usrmerged@/%{?usrmerged}/' \
%else
    -e '/@usrmerged@/d' \
%endif
%if 0%{?is_opensuse}
    -e '/@sle_version@%{?sle_version:nomatch}/d' \
    -e 's/@sle_version@/%{?sle_version}%{!?sle_version:0}/' \
%else
    -e '/@sle_version@/d' \
%endif
  < suse_macros.in > suse_macros

%if 0%{?is_opensuse}
cat <<EOF > macros.d/macros.opensuse
# trim binary changelogs to include roughly 3 years
# maxnum,cuttime,minnum
%%_binarychangelogtrim 0,$(date -d "Jan 1 UTC 3 years ago" +%s),10
EOF
%endif

cat <<EOF > macros.d/macros.sbat
# Common SBAT values for secure boot
# https://github.com/rhboot/shim/blob/main/SBAT.md

%if 0%{?is_opensuse}
%%sbat_distro          opensuse
%%sbat_distro_summary  The openSUSE Project
%else
%%sbat_distro          sle
%%sbat_distro_summary  SUSE Linux Enterprise
%endif
%%sbat_distro_url      mailto:security@suse.de
EOF

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
