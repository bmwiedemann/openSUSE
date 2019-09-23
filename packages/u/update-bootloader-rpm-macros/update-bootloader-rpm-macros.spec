#
# spec file for package update-bootloader-rpm-macros
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           update-bootloader-rpm-macros
Version:        0
Release:        0
Summary:        RPM macros for update-bootloader
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://en.opensuse.org/openSUSE:Update_Bootloader_RPM_Macros
Source0:        macros.update-bootloader
BuildArch:      noarch

%description
This package provides rpm macros for bootloader update in rpm scripts

%prep

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}

%files
%defattr(-,root,root)
%{_rpmmacrodir}/macros.update-bootloader

%changelog
