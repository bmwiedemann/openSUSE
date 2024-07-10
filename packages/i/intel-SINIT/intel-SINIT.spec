#
# spec file for package intel-SINIT
#
# Copyright (c) 2020 SUSE LLC
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


Name:           intel-SINIT
BuildRequires:  fdupes
URL:            http://software.intel.com/en-us/articles/intel-trusted-execution-technology/
Summary:        Intel SINIT AC (Secure Inititalization Authenticated Code) modules
License:        SUSE-Firmware
Group:          Development/Tools/Other
Version:        2.3
Release:        0
BuildRequires:  unzip
# https://secure-software.intel.com/en-us/system/files/article/183305/2nd-gen-i5-i7-sinit-51.zip
Source0:        2nd-gen-i5-i7-sinit-51.zip
# https://secure-software.intel.com/en-us/system/files/article/183305/3rd-gen-i5-i7-racm-sinit-67_1.zip
Source1:        3rd-gen-i5-i7-racm-sinit-67_1.zip
# https://secure-software.intel.com/en-us/system/files/article/183305/3rd-gen-i5-i7-sinit-67.zip
Source2:        3rd-gen-i5-i7-sinit-67.zip
# https://secure-software.intel.com/en-us/system/files/article/183305/4th-gen-i5-i7-sinit-75.zip
Source3:        4th-gen-i5-i7-sinit-75.zip
# https://secure-software.intel.com/en-us/system/files/article/183305/gm45-gs45-pm45-sinit-51.zip
Source4:        gm45-gs45-pm45-sinit-51.zip
# https://secure-software.intel.com/en-us/system/files/30/c4/i5-i7-dual-sinit-51.zip
Source5:        i5-i7-dual-sinit-51.zip
# https://secure-software.intel.com/en-us/system/files/1e/dc/i7-quad-sinit-51.zip
Source6:        i7-quad-sinit-51.zip
Source7:        q45-q43-sinit-51.zip
# https://secure-software.intel.com/en-us/system/files/article/183305/xeon-5600-3500-sinit-v1.1.zip
Source8:        xeon-5600-3500-sinit-v1.1.zip
# https://secure-software.intel.com/en-us/system/files/e8/00/xeon-e7-8800-4800-2800-sinit-v1.1.zip
Source9:        xeon-e7-8800-4800-2800-sinit-v1.1.zip
# https://secure-software.intel.com/en-us/system/files/article/183305/q35-sinit-51.zip
Source10:       q35-sinit-51.zip
Source11:       SINIT-guide.txt
# https://software.intel.com/system/files/managed/7b/2b/5th_gen_i5_i7-SINIT_79.zip
Source12:       5th_gen_i5_i7-SINIT_79.zip
# https://software.intel.com/system/files/managed/70/be/6th_gen_i5_i7-SINIT_71.zip
Source13:       6th_gen_i5_i7-SINIT_71.zip
# https://software.intel.com/system/files/managed/dc/a9/7th_gen_i5_i7-SINIT_74.zip
Source14:       7th_gen_i5_i7-SINIT_74.zip
# https://software.intel.com/protected-download/267276/183305
Source15:       6th_7th_gen_i5_i7-SINIT_79.zip
# https://software.intel.com/content/dam/develop/external/us/en/protected/6th_7th_gen_i5_i7-SINIT_79.zip
Source16:       8th_9th_gen_i5_i7-SINIT_81.zip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
intel-SINIT contains the binary modules required to utilize
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM. The SINIT modules are digitally
signed by INTEL and perfors the initial steps during a trusted boot. Among
these initial steps are measurements of the BIOS/firmware and system settings
like ACPI tables.

A specific SINIT file tailored to your INTEL processor needs to be used.
This package contains them all for your convenience.

%prep
%setup -c -n intel-SINIT
#unzip %{S:0}
unzip %{S:1}
unzip %{S:2}
unzip %{S:3}
unzip %{S:4}
unzip %{S:5}
unzip %{S:6}
unzip %{S:7}
unzip %{S:12}
unzip %{S:13}
unzip %{S:14}

mkdir 6th_7th_gen_i5_i7-SINIT_79
pushd 6th_7th_gen_i5_i7-SINIT_79
unzip %{S:15}
popd

mkdir 8th_9th_gen_i5_i7-SINIT_81
pushd 8th_9th_gen_i5_i7-SINIT_81
unzip %{S:16}
popd

mkdir xeon-5600-3500-sinit
pushd xeon-5600-3500-sinit
	unzip %{S:8}
popd

mkdir xeon-e7-8800-4800-2800-sinit
pushd xeon-e7-8800-4800-2800-sinit
	unzip %{S:9}
popd

unzip %{S:10}
chmod 644 */*
cp %{SOURCE11} .

find

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/sinit

mv */*.[Bb][Ii][nN] $RPM_BUILD_ROOT/usr/lib/sinit
chmod 644 $RPM_BUILD_ROOT/usr/lib/sinit/*.BIN

%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%doc i7_QUAD-SINIT_51 2nd_gen_i5_i7-SINIT_51 GM45_GS45_PM45-SINIT_51 3rd_gen_i5_i7-SINIT_67 xeon-5600-3500-sinit xeon-e7-8800-4800-2800-sinit
%doc i5_i7_DUAL-SINIT_51 3rd_gen_i5_i7_RACM-SINIT_67 4th_gen_i5_i7-SINIT_75 5th_gen_i5_i7-SINIT_79 6th_gen_i5_i7-SINIT_71 7th_gen_i5_i7-SINIT_74 Q45_Q43-SINIT_51 Q35-SINIT_51
%doc 6th_7th_gen_i5_i7-SINIT_79 8th_9th_gen_i5_i7-SINIT_81
%doc SINIT-guide.txt
%dir /usr/lib/sinit
/usr/lib/sinit/*

%changelog
