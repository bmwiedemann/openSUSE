#
# spec file for package pd-mapper
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


Name:           pd-mapper
Version:        1.0~git20230901.10997ba
Release:        0
Summary:        Qualcomm Protection Domain mapper
License:        BSD-3-Clause
Group:          System/Daemons
URL:            https://github.com/andersson/pd-mapper
BuildRequires:  qrtr-devel
BuildRequires:  xz-devel
Requires:       qrtr
Source0:        pd-mapper-%{version}.tar.xz
ExclusiveArch:  aarch64
Supplements:    modalias(of:Npmic-glinkT*Cqcom,sc8280xp-pmic-glinkCqcom,pmic-glink)

%description
Qualcomm protection domain mapper service, which is required by userspace
applications to access remote processors [Wifi, modem, sensors, battery, etc]
on Qualcomm SoCs using the QRTR protocol.

%prep
%autosetup

%build
%make_build  prefix="%{_prefix}"

%install
%make_install  prefix="%{_prefix}"

%pre
%service_add_pre pd-mapper.service

%preun
%service_del_preun pd-mapper.service

%post
%service_add_post pd-mapper.service

%postun
%service_del_postun pd-mapper.service

%files
%{_bindir}/pd-mapper
%{_unitdir}/pd-mapper.service

%changelog
