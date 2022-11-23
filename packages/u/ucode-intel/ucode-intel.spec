#
# spec file for package ucode-intel
#
# Copyright (c) 2022 SUSE LLC
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


%if %{undefined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif
Name:           ucode-intel
Version:        20221108
Release:        0
Summary:        Microcode Updates for Intel x86/x86-64 CPUs
License:        SUSE-Firmware
Group:          Hardware/Other
BuildRequires:  suse-module-tools
#License is: Intel Software License Agreement
URL:            https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files
Source0:        https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/archive/microcode-%version.tar.gz
Source1:        ucode-intel-rpmlintrc
Supplements:    modalias(x86cpu:vendor%3A0000%3Afamily%3A*%3Amodel%3A*%3Afeature%3A*)
# new method ... note that only 1 : might be present, otherwise libzypp misinterprets it.
Supplements:    modalias(cpu:type%3Ax86*ven0000*)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): coreutils
Requires(postun): coreutils
ExclusiveArch:  %ix86 x86_64

%description
This package contains the microcode update blobs for Intel x86 and x86-64 CPUs.

%prep
%setup -q -n Intel-Linux-Processor-Microcode-Data-Files-microcode-%version/

%build
#it is closed source.. nothing to build.

%install
mkdir -p %{buildroot}%{_firmwaredir}/intel-ucode
cp intel-ucode/* %{buildroot}%{_firmwaredir}/intel-ucode
cd intel-ucode-with-caveats
for microcode in *;do
    cp $microcode %{buildroot}%{_firmwaredir}/intel-ucode/$microcode
done

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%defattr(-,root,root)
%license license
%doc releasenote.md
%{_firmwaredir}/intel-ucode/

%changelog
