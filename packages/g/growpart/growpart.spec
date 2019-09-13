#
# spec file for package growpart
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define base_version 0.30
Name:           growpart
Version:        %{base_version}
Release:        0
Summary:        Grow a partition
License:        GPL-3.0-only
Group:          System/Management
Url:            http://launchpad.net/cloud-utils
Source0:        cloud-utils-%{base_version}.tar.gz
Source1:        rootgrow
Source2:        rootgrow.service
Patch:          licenseGPLv3.patch
Requires:       util-linux
%if 0%{?suse_version} && 0%{?suse_version} > 1220
Requires:       gptfdisk
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Grow a partition. This is predominantly useful in the cloud when an instance
is started with a larger root partition than the image size. The root
partition can be expanded to take up the additional size.

%if 0%{?suse_version} && 0%{?suse_version} > 1220
%package rootgrow
Version:        1.0.0
Release:        0
Summary:        Resize root partition
Group:          System/Management
Requires:       growpart
Requires:       python3
Requires:       systemd
# pkg-config is needed to find correct systemd unit dir
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(systemd)

%description rootgrow
Provides as script and service togrow the root partition
%endif

%prep
%setup -q -n cloud-utils-%{base_version}
%patch -p1

%build

%install
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_sbindir}
cp bin/growpart %{buildroot}/%{_sbindir}
cp man/growpart.1 %{buildroot}/%{_mandir}/man1
%if 0%{?suse_version} && 0%{?suse_version} > 1220
mkdir -p %{buildroot}/usr/lib/systemd/system
cp %SOURCE1 %{buildroot}/%{_sbindir}
cp %SOURCE2 %{buildroot}/usr/lib/systemd/system
chmod 755 %{buildroot}/%{_sbindir}/rootgrow
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%license LICENSE-GPLv3
%{_sbindir}/growpart
%{_mandir}/man1/*

%if 0%{?suse_version} && 0%{?suse_version} > 1220
%files rootgrow
%defattr(-,root,root,-)
%{_sbindir}/rootgrow
/usr/lib/systemd/system/rootgrow.service
%endif

%changelog
