#
# spec file for package systemd-default-settings
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


Name:           systemd-default-settings
URL:            https://github.com/openSUSE/systemd-default-settings
Version:        0.4
Release:        0
Summary:        Customization of systemd default settings for SUSE distributions
License:        GPL-2.0-or-later
Group:          System/Base
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-branding = %{version}-%{release}

%description
This package overrides some of the upstream default settings which are
better suited for openSUSE or SLE distributions.

This package should not be installed alone but is supposed to be
pulled in by the branding package instead.

%package branding-SLE
Summary:        Specific customization of systemd defaults settings for SLE
Group:          System/Base
Requires:       %{name} = %{version}-%{release}
Supplements:    packageand(%{name}:branding-SLE)
Provides:       %{name}-branding = %{version}-%{release}
Conflicts:      otherproviders(%{name}-branding)

%description branding-SLE
This package overrides some of the upstream default settings to make
them better suited for SLE distributions.

%package branding-openSUSE
Summary:        Specific customization of systemd defaults settings for openSUSE
Group:          System/Base
Requires:       %{name} = %{version}-%{release}
Supplements:    packageand(%{name}:branding-openSUSE)
Provides:       %{name}-branding = %{version}-%{release}
Conflicts:      otherproviders(%{name}-branding)

%description branding-openSUSE
This package overrides some of the upstream default settings to make
them better suited for openSUSE distributions.

%package branding-upstream
Summary:        Restore upstream systemd defaults settings
Group:          System/Base
Provides:       %{name}-branding = %{version}-%{release}
Conflicts:      %{name}
Conflicts:      otherproviders(%{name}-branding)

%description branding-upstream
Installing this package restores some of the upstream default settings
by uninstalling all drop-ins shipped by %{name} and its branding sub
package.

%prep
%setup -q

%build

%install
%make_install

find %{buildroot} -name \*.d -type d -printf "%%%%dir /%%P\n" >SUSE.list
find %{buildroot} -name 20-defaults-SUSE.conf -printf "/%%P\n" >>SUSE.list
find %{buildroot} -name 25-defaults-SLE.conf -printf "/%%P\n" >SLE.list
find %{buildroot} -name 25-defaults-openSUSE.conf -printf "/%%P\n" >openSUSE.list

%files -f SUSE.list
%defattr(-,root,root)

%files branding-SLE -f SLE.list
%defattr(-,root,root)

%files branding-openSUSE -f openSUSE.list
%defattr(-,root,root)

%files branding-upstream
%defattr(-,root,root)

%changelog
