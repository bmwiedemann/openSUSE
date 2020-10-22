#
# spec file for package rpm-config-SUSE
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.g60
Release:        0
Summary:        SUSE specific RPM configuration files
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/rpm-config-SUSE
Source:         %{name}-%{version}.tar.xz

# RPM owns the directories we need
Requires:       rpm

BuildArch:      noarch
#!BuildIgnore:  rpm-config-SUSE

%description
This package contains the RPM configuration data for the SUSE Linux
distribution family.

%prep
%setup -q

%build
# Set up the SUSE Linux version macros
sed -e 's/@suse_version@/%{?suse_version}%{!?suse_version:0}/' \
    -e 's/@sles_version@/%{?sles_version}%{!?sles_version:0}/' \
    -e 's/@ul_version@/%{?ul_version}%{!?ul_version:0}/' \
    -e '/@is_opensuse@%{?is_opensuse:nomatch}/d' \
    -e 's/@is_opensuse@/%{?is_opensuse}%{!?is_opensuse:0}/' \
    -e '/@leap_version@%{?leap_version:nomatch}/d' \
    -e 's/@leap_version@/%{?leap_version}%{!?leap_version:0}/' \
%if 0%{?is_opensuse}
    -e '/@sle_version@%{?sle_version:nomatch}/d' \
    -e 's/@sle_version@/%{?sle_version}%{!?sle_version:0}/' \
%else
    -e '/@sle_version@/d' \
%endif
  < suse_macros.in > suse_macros

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
