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
%define git_version aaae2fb60f75b07d9c249ebe668524f7ddf51243

Name:           kernel-firmware-qcom
Version:        20250206
Release:        0
Summary:        Kernel firmware files for Qualcomm device drivers
License:        SUSE-Firmware AND GPL-2.0-or-later
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        %{name}-%{version}.tar.xz
# URL:          https://github.com/openSUSE/kernel-firmware-tools/
Source1:        kernel-firmware-tools-20250211.tar.xz
Source2:        %{name}-rpmlintrc
Source3:        git_id
Source10:       aliases
Source11:       post
BuildRequires:  suse-module-tools
Requires(post): %{_bindir}/mkdir
Requires(post): %{_bindir}/touch
Requires(postun):%{_bindir}/mkdir
Requires(postun):%{_bindir}/touch
Requires(post): dracut >= 049
Conflicts:      kernel < 5.3
Conflicts:      kernel-firmware-uncompressed
BuildArch:      noarch
%if 0%{?suse_version} >= 1550
# make sure we have post-usrmerge filesystem package on TW
Conflicts:      filesystem < 84
%endif
Supplements:    modalias(of:N*T*Cqcom,mdp4)
Supplements:    modalias(of:N*T*Cqcom,mdp4C*)
Supplements:    modalias(of:N*T*Cqcom,mdp5)
Supplements:    modalias(of:N*T*Cqcom,mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,mdss)
Supplements:    modalias(of:N*T*Cqcom,mdssC*)
Supplements:    modalias(of:N*T*Cqcom,mdss_mdp)
Supplements:    modalias(of:N*T*Cqcom,mdss_mdpC*)
Supplements:    modalias(of:N*T*Cqcom,msm8917-mdp5)
Supplements:    modalias(of:N*T*Cqcom,msm8917-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,msm8937-mdp5)
Supplements:    modalias(of:N*T*Cqcom,msm8937-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,msm8953-mdp5)
Supplements:    modalias(of:N*T*Cqcom,msm8953-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,msm8996-mdp5)
Supplements:    modalias(of:N*T*Cqcom,msm8996-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,msm8998-dpu)
Supplements:    modalias(of:N*T*Cqcom,msm8998-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,msm8998-mdss)
Supplements:    modalias(of:N*T*Cqcom,msm8998-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,qcm2290-dpu)
Supplements:    modalias(of:N*T*Cqcom,qcm2290-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,qcm2290-mdss)
Supplements:    modalias(of:N*T*Cqcom,qcm2290-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-dpu)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-mdss)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sc7180-dpu)
Supplements:    modalias(of:N*T*Cqcom,sc7180-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sc7180-mdss)
Supplements:    modalias(of:N*T*Cqcom,sc7180-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-dpu)
Supplements:    modalias(of:N*T*Cqcom,sc7280-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-mdss)
Supplements:    modalias(of:N*T*Cqcom,sc7280-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-dpu)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-mdss)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-dpu)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-mdss)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sdm630-mdp5)
Supplements:    modalias(of:N*T*Cqcom,sdm630-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,sdm660-mdp5)
Supplements:    modalias(of:N*T*Cqcom,sdm660-mdp5C*)
Supplements:    modalias(of:N*T*Cqcom,sdm670-dpu)
Supplements:    modalias(of:N*T*Cqcom,sdm670-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sdm670-mdss)
Supplements:    modalias(of:N*T*Cqcom,sdm670-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sdm845-dpu)
Supplements:    modalias(of:N*T*Cqcom,sdm845-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sdm845-mdss)
Supplements:    modalias(of:N*T*Cqcom,sdm845-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm6115-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm6115-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm6115-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm6115-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm6125-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm6125-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm6125-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm6125-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm6350-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm6350-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm6350-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm6350-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm6375-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm6375-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm6375-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm6375-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm7150-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm7150-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm7150-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm7150-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm8150-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm8150-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm8150-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm8150-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm8250-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm8250-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm8250-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm8250-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm8350-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm8350-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm8350-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm8350-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm8450-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm8450-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm8450-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm8450-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm8550-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm8550-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm8550-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm8550-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,sm8650-dpu)
Supplements:    modalias(of:N*T*Cqcom,sm8650-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,sm8650-mdss)
Supplements:    modalias(of:N*T*Cqcom,sm8650-mdssC*)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-dpu)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-dpuC*)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-mdss)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-mdssC*)
Supplements:    modalias(mhi:QAIC_TIMESYNC_PERIODIC)
Supplements:    modalias(pci:v000017CBd0000A080sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v000017CBd0000A100sv*sd*bc*sc*i*)
Supplements:    modalias(of:N*T*Cqcom,msm8909-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8909-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8916-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8916-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8953-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8953-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8974-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8974-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8996-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8996-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8998-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8998-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,q6v5-pil)
Supplements:    modalias(of:N*T*Cqcom,q6v5-pilC*)
Supplements:    modalias(of:N*T*Cqcom,sc7180-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,sc7180-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,sc7280-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,sdm660-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,sdm660-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,sdm845-mss-pil)
Supplements:    modalias(of:N*T*Cqcom,sdm845-mss-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8226-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8226-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8953-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8953-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8974-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8974-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8996-adsp-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8996-adsp-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8996-slpi-pil)
Supplements:    modalias(of:N*T*Cqcom,msm8996-slpi-pilC*)
Supplements:    modalias(of:N*T*Cqcom,msm8998-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,msm8998-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,msm8998-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom,msm8998-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom,qcs404-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,qcs404-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,qcs404-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,qcs404-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,qcs404-wcss-pas)
Supplements:    modalias(of:N*T*Cqcom,qcs404-wcss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-cdsp0-pas)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-cdsp0-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-cdsp1-pas)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-cdsp1-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-gpdsp0-pas)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-gpdsp0-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-gpdsp1-pas)
Supplements:    modalias(of:N*T*Cqcom,sa8775p-gpdsp1-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sar2130p-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sar2130p-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc7180-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sc7180-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc7180-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sc7180-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sc7280-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sc7280-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sc7280-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc7280-wpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sc7280-wpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sc8180x-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-nsp0-pas)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-nsp0-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-nsp1-pas)
Supplements:    modalias(of:N*T*Cqcom,sc8280xp-nsp1-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sdm660-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sdm660-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sdm845-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sdm845-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sdm845-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sdm845-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sdm845-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom,sdm845-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sdx55-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sdx55-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sdx75-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sdx75-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6115-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6115-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6115-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6115-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6115-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6115-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6350-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6350-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6350-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6350-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6350-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6350-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6375-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6375-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6375-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6375-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm6375-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm6375-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8150-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8150-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8150-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8150-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8150-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8150-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8150-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8150-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8250-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8250-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8250-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8250-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8250-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8250-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8350-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8350-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8350-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8350-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8350-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8350-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8350-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8350-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8450-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8450-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8450-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8450-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8450-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8450-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8450-slpi-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8450-slpi-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8550-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8550-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8550-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8550-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8550-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8550-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8650-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8650-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8650-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8650-cdsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,sm8650-mpss-pas)
Supplements:    modalias(of:N*T*Cqcom,sm8650-mpss-pasC*)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-adsp-pas)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-adsp-pasC*)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-cdsp-pas)
Supplements:    modalias(of:N*T*Cqcom,x1e80100-cdsp-pasC*)

%description
This package contains kernel firmware files for Qualcomm device drivers.


%prep
%autosetup -a1 -p1
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

%pre
# ugly workaround for changing qcom/LENOVO/21BX to a symlink (bsc#1204103)
if [ ! -L %{_firmwaredir}/qcom/LENOVO/21BX ]; then
  if [ -d %{_firmwaredir}/qcom/LENOVO/21BX ]; then
    mv %{_firmwaredir}/qcom/LENOVO/21BX %{_firmwaredir}/qcom/LENOVO/21BX.xxxold
  fi
fi

%post
# ugly workaround (bsc#1204103)
if [ -d %{_firmwaredir}/qcom/LENOVO/21BX.xxxold ]; then
  mv %{_firmwaredir}/qcom/LENOVO/21BX %{_firmwaredir}/qcom/LENOVO/21BX.xxxnew
  mv %{_firmwaredir}/qcom/LENOVO/21BX.xxxold %{_firmwaredir}/qcom/LENOVO/21BX
else
%{?regenerate_initrd_post}
fi

%postun
%{?regenerate_initrd_post}

%posttrans
# ugly workaround (bsc#1204103)
if [ -L %{_firmwaredir}/qcom/LENOVO/21BX.xxxnew ]; then
  rm -rf %{_firmwaredir}/qcom/LENOVO/21BX
  mv %{_firmwaredir}/qcom/LENOVO/21BX.xxxnew %{_firmwaredir}/qcom/LENOVO/21BX
fi
%{?regenerate_initrd_posttrans}

%files
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}
%{_firmwaredir}

%changelog
