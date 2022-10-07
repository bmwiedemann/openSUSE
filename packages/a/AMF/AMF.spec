#
# spec file for package AMF
#
# Copyright (c) 2022 SUSE LLC
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


Name:           AMF
Version:        1.4.26
Release:        0
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
Source:         %{name}-%{version}.tar
BuildArch:      noarch

%description
A lightweight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed-source
AMDGPU-Pro driver.

%package        devel
Summary:        Development files for %{name}
Suggests:       AMF-docs

%description    devel
A lightweight, portable multimedia framework that abstracts away most of the 
platform and API-specific details. %{name} is supported on the closed-source           
AMDGPU-Pro driver.

The %{name}-devel package contains header files for developing
applications that use %{name}.

%package docs
Summary:        Additional Documentation for the Advanced Media Framework (AMF) SDK
Group:          Documentation/Other

%description docs
This package contains additional documentation provided for the
Advanced Media Framework (AMF) SDK.

%prep
%setup -q

%build

%install
install -dm755 %{buildroot}%{_includedir}/%{name}/components
install -dm755 %{buildroot}%{_includedir}/%{name}/core
install -Dm644 amf/public/include/components/*.h %{buildroot}%{_includedir}/%{name}/components
install -Dm644 amf/public/include/core/*.h %{buildroot}%{_includedir}/%{name}/core

%files devel
%license LICENSE.txt
%doc amf/doc/README.md amf/doc/Readme.txt
%{_includedir}/%{name}/

%files docs
%doc amf/doc/*

%changelog
