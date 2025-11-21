#
# spec file for package blender
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2019-2025 LISA GmbH, Bingen, Germany.
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


Name:           blender
Version:        5.0.0
Release:        0
Summary:        Package to pull in the latest blender for you
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/3D Editors
URL:            https://www.blender.org/
Source1:        README.SUSE
Requires:       blender-implementation
Recommends:     blender-implementation >= %{version}
Provides:       blender-wrapper = %{version}-%{release}
BuildArch:      noarch

%description
This is a wrapper package to pull in the versioned packages of blender.

This package by defaults pulls in the latest version for you.

%package lang
Summary:        Package to pull in the latest blender for you
Requires:       (blender-4.5-lang if blender-4.5)
Requires:       (blender-5.0-lang if blender-5.0)
Provides:       blender-wrapper-lang = %{version}-%{release}

%description lang
This is a wrapper package to pull in the versioned packages of blender.

This package by defaulang pulls in the latest lang version for you.

%package demo
Summary:        Package to pull in the latest blender for you
Requires:       (blender-4.5-demo if blender-4.5)
Requires:       (blender-5.0-demo if blender-5.0)
Provides:       blender-wrapper-demo = %{version}-%{release}

%description demo
This is a wrapper package to pull in the versioned packages of blender.

This package by defaudemo pulls in the latest demo version for you.

%package lts
Summary:        Package to pull in the latest blender for you
Requires:       blender-implementation-lts
Recommends:     blender-implementation-lts >= %{version}
Provides:       blender-wrapper-lts = %{version}-%{release}

%description lts
This is a wrapper package to pull in the versioned packages of blender.

This package by defaults pulls in the latest lts version for you.

%prep
cp %{SOURCE1} .

%files
%doc README.SUSE

%files lts
%doc README.SUSE

%files demo
%doc README.SUSE

%files lang
%doc README.SUSE

%changelog
