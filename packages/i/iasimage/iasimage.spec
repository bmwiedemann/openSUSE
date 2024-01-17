#
# spec file for package iasimage
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           iasimage
Version:        0.0.2+git20190410.7799ac7
Release:        0
Summary:        Utility for creating Intel Automotive Service (IAS) images
License:        BSD-3-Clause
Group:          System/Boot
Url:            https://github.com/intel/iasimage
Source:         %{name}-%{version}.tar.xz
Patch0:         env-script-interpreter.patch
# for running tests due to install target (see Makefile)
BuildRequires:  python3-cryptography >= 2.2.2
BuildRequires:  openssl
Requires:       python3-cryptography >= 2.2.2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
iasimage is a utility program for creating Intel Automotive Service (IAS)
images, a binary file format understood by bootloaders to load and initialize
Operating Systems or Hypervisors.

%prep
%setup -q
%patch0 -p0

%build

%install
ln -s /usr/bin/python3 python
export PATH=.:$PATH
%make_install INSTALL_ROOT=%{buildroot} BINDIR=%{_bindir}

%check
# already run in make install

%files
%defattr(-,root,root)
%{_bindir}/iasimage
%attr(0644, root, root) %doc README.md LICENSE

%changelog
