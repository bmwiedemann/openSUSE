#
# spec file for package container-build-checks
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


Name:           container-build-checks
Version:        1682595397.5ce6d2f
Release:        0
Summary:        Scripts to validate built container images
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/container-build-checks
Source0:        %{name}-%{version}.tar.xz
Source1:        openSUSE.conf
Source2:        SUSE.conf
Requires:       %{name}-vendor
BuildArch:      noarch

%package vendor-openSUSE
Summary:        openSUSE configuration for %{name}
Group:          Development/Tools/Building
Requires:       %{name} = %{version}
Provides:       %{name}-vendor
Conflicts:      %{name}-vendor

%description vendor-openSUSE
openSUSE configuration for %{name}

%package vendor-SUSE
Summary:        SUSE configuration for %{name}
Group:          Development/Tools/Building
Requires:       %{name} = %{version}
Provides:       %{name}-vendor
Conflicts:      %{name}-vendor

%description vendor-SUSE
SUSE configuration for %{name}

%package strict
Summary:        Strict configuration for %{name}
Group:          Development/Tools/Building

%description strict
Strict configuration for %{name}

%description
This tool checks that built container images conform to the openSUSE container
image policies (https://en.opensuse.org/Building_derived_containers).

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/container-build-checks/
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/container-build-checks/openSUSE.conf
install -m0644 %{SOURCE2} %{buildroot}%{_datadir}/container-build-checks/SUSE.conf
echo -e "[General]\nFatalWarnings=true" > %{buildroot}%{_datadir}/container-build-checks/strict.conf

%files
#%doc README
%license LICENSE
%dir %{_datadir}/container-build-checks
%dir %{_prefix}/lib/build/
%dir %{_prefix}/lib/build/post-build-checks/
%{_prefix}/lib/build/post-build-checks/container-build-checks

%files vendor-openSUSE
%{_datadir}/container-build-checks/openSUSE.conf

%files vendor-SUSE
%{_datadir}/container-build-checks/SUSE.conf

%files strict
%{_datadir}/container-build-checks/strict.conf

%changelog
