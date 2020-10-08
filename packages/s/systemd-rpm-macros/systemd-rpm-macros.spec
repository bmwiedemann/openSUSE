#
# spec file for package systemd-rpm-macros
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


Name:           systemd-rpm-macros
Version:        4.1
Release:        0
Summary:        RPM macros for systemd
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            http://en.opensuse.org/openSUSE:Systemd_packaging_guidelines
Source0:        macros.systemd
Requires:       coreutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#!BuildIgnore:  util-linux
#!BuildIgnore:  %{name}

%description
Starting with openSUSE 12.1, several RPM macros must be used to package systemd
services files. This package provides these macros.

%prep

%build

%install
install -Dm644 %{S:0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.systemd
UNITDIR="$(sed -n 's/.*_unitdir[[:blank:]]*//p' %{S:0})"
for i in $UNITDIR `dirname $UNITDIR`; do
   mkdir -p %{buildroot}$i
   echo $i >> unitdir
done

%files -f unitdir
%defattr(-,root,root)
%{_rpmconfigdir}/macros.d/macros.systemd

%changelog
