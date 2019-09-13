#
# spec file for package branding-upstream
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           branding-upstream
Version:        12.3
Release:        0
Provides:       branding
Conflicts:      otherproviders(branding)
Source:         %{name}-COPYING
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Summary:        SUSE Brand File Supplementing Upstream Look and Feel
License:        MIT
Group:          System/Fhs

%description
This package contains the file /etc/SUSE-brand, and its name is used as
a trigger for installation of look and feel and branding of packages as
it was defined by upstream developers.

WARNING: If you decide to install this package instead of the default
branding package, you will lose vendor customization of your
distribution.



%prep
%setup -q -T -c
cp -a %{S:0} COPYING

%build
cat >SUSE-brand <<EOF
upstream
VERSION = %{version}
CO-BRANDS = openSUSE SLED SLES SLE
EOF

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp SUSE-brand $RPM_BUILD_ROOT%{_sysconfdir}/

%files
%defattr(-,root,root)
%doc COPYING
%{_sysconfdir}/SUSE-brand

%changelog
