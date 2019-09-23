#
# spec file for package habootstrap-formula
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
%define fname cluster
%define fdir  %{_datadir}/salt-formulas

Name:           habootstrap-formula
Version:        0.2.3
Group:          System/Packages
Release:        0
Summary:        HA cluster (crmsh) deployment salt formula

License:        Apache-2.0
Url:            https://github.com/SUSE/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       salt-shaptools

# On SLE/Leap 15-SP1 and TW requires the new salt-formula configuration location.
%if ! (0%{?sle_version:1} && 0%{?sle_version} < 150100)
Requires:       salt-standalone-formulas-configuration
%endif

%description
HA cluster salt deployment formula. This formula is capable to perform
the HA cluster bootstrap actions (init, join, remove) using standalone salt
or via SUSE Manager formulas with forms, available on SUSE Manager 4.0.

%prep
%setup -q

%build

%install

# before SUMA 4.0/15-SP1, install on the standard Salt Location.
%if 0%{?sle_version:1} && 0%{?sle_version} < 150100

mkdir -p %{buildroot}/srv/salt/
cp -R %{fname} %{buildroot}/srv/salt

%else

# On SUMA 4.0/15-SP1, a single shared directory will be used.
mkdir -p %{buildroot}%{fdir}/states/%{fname}
mkdir -p %{buildroot}%{fdir}/metadata/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states
cp -R form.yml %{buildroot}%{fdir}/metadata/%{fname}
if [ -f metadata.yml ]
then
  cp -R metadata.yml %{buildroot}%{fdir}/metadata/%{fname}
fi

%endif

%if 0%{?sle_version:1} && 0%{?sle_version} < 150100

%files
%defattr(-,root,root,-)
%if 0%{?sle_version} < 120300
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
