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
Name:		pd-mapper
Version:	1.0_107104b20b
Release:	0
Summary:	Qualcomm Protection Domain mapper
License:	BSD-3-Clause
Group:		System/Daemons
URL:		https://github.com/andersson/pd-mapper
BuildRequires:	qrtr qrtr-devel
Source0:	pd-mapper-%{version}.tar.xz
Source1:	pd-mapper.service
ExclusiveArch:  aarch64
Supplements:	modalias(of:Npmic-glinkT*Cqcom,sc8280xp-pmic-glinkCqcom,pmic-glink)
%define pdmdir	%{_sbindir}
%define pdmsrv	%{_unitdir}
%define fwdir	/lib/firmware/qcom/sc8280xp/LENOVO/21BX
%define fwbkup	%{fwdir}/fw_backup

%description
Qualcomm protection domain mapper service, which is required by userspace
applications to access remote processors [Wifi, modem, sensors, battery ..
,etc] on Qualcomm SoCs using the QRTR protocol.

%prep
%autosetup

%build
%make_build

%install
mkdir -p %{buildroot}%{pdmdir}
strip pd-mapper
install -m 744 pd-mapper %{buildroot}%{pdmdir}
mkdir -p %{buildroot}%{pdmsrv}
install -m 644 %{_sourcedir}/pd-mapper.service %{buildroot}%{pdmsrv}

%pre
%service_add_pre pd-mapper.service

%preun
%service_del_preun pd-mapper.service

%post
%service_add_post pd-mapper.service
  fw_blobs="qcadsp8280.mbn qccdsp8280.mbn"
  for i in $fw_blobs; do
    file="%{fwdir}/$i.xz"
      if [ -f $file ]; then
        [ ! -d %{fwbkup} ] && mkdir -p %{fwbkup}

        echo "Backup and uncompress $i.xz .."
        cp -a $file %{fwbkup}/
        unxz $file
      fi
  done
  echo "Kernel needs to reload uncompressed remoteproc firmware. Please reboot system."

%postun
%service_del_postun pd-mapper.service
  fw_blobs="qcadsp8280.mbn qccdsp8280.mbn"
  for i in $fw_blobs; do
    file="%{fwdir}/$i"
    backup_file="%{fwbkup}/$i.xz"
      if [ -f $file ]  && [ -f $backup_file ]; then
        echo "Delete $i and rollback $i.xz .."
        rm -f $file
        mv $backup_file %{fwdir}/ 
      fi
  done

  if [ -d "%{fwbkup}" ]; then rm -rf %{fwbkup}; fi

%files
%defattr(-,root,root)
%{pdmdir}/pd-mapper
%{pdmsrv}/pd-mapper.service

%changelog
