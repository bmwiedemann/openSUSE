#
# spec file for package drbd-formula
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
%define fname drbd
%define fdir %{_datadir}/salt-formulas
Name:           drbd-formula
Version:        0.3.0
Release:        0
Summary:        DRBD deployment salt formula
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/SUSE/%{name}
Source0:        %{name}-%{version}.tar.gz
Requires:       drbd-utils
Requires:       salt-shaptools
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# On SLE/Leap 15-SP1 and TW requires the new salt-formula configuration location.
%if ! (0%{?sle_version:1} && 0%{?sle_version} < 150100)
Requires:       salt-standalone-formulas-configuration
%endif


%description
DRBD deployment salt formula
Available on SUSE manager 4.0

%prep
%setup -q

%build

%install
# before SUMA 4.0/15-SP1, install on the standard Salt Location.
%if 0%{?sle_version:1} && 0%{?sle_version} < 150100
mkdir -p %{buildroot}/srv/salt/
cp -R %{fname} %{buildroot}/srv/salt
cp -R templates/* %{buildroot}/srv/salt/%{fname}/templates/
%else
# On SUMA 4.0/15-SP1, a single shared directory will be used.
mkdir -p %{buildroot}%{fdir}/states/%{fname}
mkdir -p %{buildroot}%{fdir}/metadata/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states
cp -R templates/* %{buildroot}%{fdir}/states/%{fname}/templates/
cp -R form.yml metadata.yml pillar.example README.md %{buildroot}%{fdir}/metadata/%{fname}
%endif

%if 0%{?sle_version:1} && 0%{?sle_version} < 150100
%files
# %license macro is not available on older releases
%if 0%{?sle_version} <= 120300
%doc README.md LICENSE
%else
%doc README.md
%license LICENSE
%endif
/srv/salt/%{fname}
%dir %attr(0755, root, salt) /srv/salt
%else
%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{fdir}
%dir %{fdir}/states
%dir %{fdir}/metadata
%{fdir}/states/%{fname}
%{fdir}/metadata/%{fname}
%dir %attr(0750, root, salt) %{fdir}
%dir %attr(0750, root, salt) %{fdir}/states
%dir %attr(0750, root, salt) %{fdir}/metadata
%endif

%changelog
