#
# spec file for package kernel-firmware-qcom
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} < 1550
%define _firmwaredir /lib/firmware
%endif
%define __ksyms_path ^%{_firmwaredir}
%define git_version b055b3e245423cbdce0a9f9e7b7768495bc01dc0

Name:           kernel-firmware-qcom
Version:        20251106
Release:        0
Summary:        Kernel firmware files for Qualcomm device drivers
License:        GPL-2.0-or-later AND SUSE-Firmware
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/kernel-firmware-tools/archive/refs/tags/20251111.tar.gz#/kernel-firmware-tools-20251111.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
Source11:       post
BuildRequires:  suse-module-tools
Requires(post): %{_bindir}/mkdir
Requires(post): %{_bindir}/touch
Requires(postun): %{_bindir}/mkdir
Requires(postun): %{_bindir}/touch
Requires(post): dracut >= 049
Conflicts:      kernel < 5.3
Conflicts:      kernel-firmware-uncompressed
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
Conflicts:      (filesystem without may-perform-usrmerge)
%endif
Supplements:    modalias(mhi:QAIC_TIMESYNC_PERIODIC)
Supplements:    modalias(of:N*T*Cqcom%2Cmdp4)
Supplements:    modalias(of:N*T*Cqcom%2Cmdp4C*)
Supplements:    modalias(of:N*T*Cqcom%2Cmdp5)
Supplements:    modalias(of:N*T*Cqcom%2Cmdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Cmdss)
Supplements:    modalias(of:N*T*Cqcom%2CmdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmdss_mdp)
Supplements:    modalias(of:N*T*Cqcom%2Cmdss_mdpC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-wpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cmilos-wpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8226-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8226-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8226-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8226-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8909-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8909-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8916-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8916-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8917-mdp5)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8917-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8926-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8926-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8937-mdp5)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8937-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8953-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8953-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8953-mdp5)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8953-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8953-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8953-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8974-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8974-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8974-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8974-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-mdp5)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-slpi-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8996-slpi-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cmsm8998-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cq6v5-pil)
Supplements:    modalias(of:N*T*Cqcom%2Cq6v5-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcm2290-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Cqcm2290-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcm2290-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Cqcm2290-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs404-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs404-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs404-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs404-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs404-wcss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cqcs404-wcss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-cdsp0-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-cdsp0-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-cdsp1-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-cdsp1-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-gpdsp0-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-gpdsp0-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-gpdsp1-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-gpdsp1-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csa8775p-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csar2130p-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csar2130p-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csar2130p-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csar2130p-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csar2130p-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csar2130p-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Csc7180-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-wpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc7280-wpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc8180x-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-nsp0-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-nsp0-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-nsp1-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csc8280xp-nsp1-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm630-mdp5)
Supplements:    modalias(of:N*T*Cqcom%2Csdm630-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm660-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csdm660-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm660-mdp5)
Supplements:    modalias(of:N*T*Cqcom%2Csdm660-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm660-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Csdm660-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm670-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csdm670-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm670-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csdm670-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-mss-pil)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csdm845-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdx55-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csdx55-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csdx75-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csdx75-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6115-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6125-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm6125-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6125-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm6125-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6150-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm6150-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6150-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm6150-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6350-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm6375-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm7150-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm7150-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm7150-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm7150-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8150-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8250-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8350-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8450-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8550-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8650-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-mdssC*)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom%2Csm8750-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-dpu)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-dpuC*)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-mdss)
Supplements:    modalias(of:N*T*Cqcom%2Cx1e80100-mdssC*)
Supplements:    modalias(pci:v000017CBd0000A080sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000017CBd0000A100sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000017CBd0000A110sv*sd*bc*sc*i*)

%description
This package contains kernel firmware files for Qualcomm device drivers.

%prep
%autosetup -p1
tar xf %{S:1} --strip-components=1
# strip down WHENCE for the topic
scripts/strip-topic-whence.sh qcom < WHENCE > WHENCE.new
mv WHENCE.new WHENCE

%build
# nothing to do

%install
./copy-firmware.sh -v --xz -j1 %{buildroot}%{_firmwaredir}
scripts/install-licenses.sh qcom %{buildroot}%{_licensedir}/%{name}
install -c -D -m 0644 WHENCE %{buildroot}%{_licensedir}/%{name}/WHENCE
install -c -D -m 0644 README.md %{buildroot}%{_docdir}/%{name}/README.md

%pretrans -p <lua>
path = "%{_firmwaredir}/qcom/LENOVO/21BX"
st = posix.stat(path)
if st and st.type == "directory" then
  path2 = path .. ".rpmmoved"
  if not os.rename(path, path2) then
    print("Cannot rename to " .. path2)
    os.exit(1)
  end
end

%posttrans
if test -d %{_firmwaredir}/qcom/LENOVO/21BX.rpmmoved; then
  rm -rf %{_firmwaredir}/qcom/LENOVO/21BX.rpmmoved
fi

%files
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}
%{_firmwaredir}

%changelog
