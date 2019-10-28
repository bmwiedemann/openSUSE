#
# spec file for package vulkan-doc
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


Name:           vulkan-doc
Version:        1.1.126
Release:        0
Summary:        Formal documentation of the Vulkan API
License:        CC-BY-SA-4.0 AND Apache-2.0
Group:          Documentation/HTML
URL:            https://github.com/KhronosGroup/
Source:         https://github.com/KhronosGroup/Vulkan-Docs/archive/v%version.tar.gz
BuildRequires:  make
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  rubygem(asciidoctor) >= 1.5.8
BuildArch:      noarch

%description
This package contains the formal documentation of the Vulkan API,
including:

 * The Vulkan API Specification
 * Specification of Vulkan extensions
 * API reference ("manual") pages

%package -n python3-spec_tools
Summary:        Build tools for the Vulkan layer validation ICD
License:        Apache-2.0
Group:          Development/Tools/Other
BuildArch:      noarch

%description -n python3-spec_tools
Build scripts for use by the Vulkan layer validation ICD build stage.

%prep
%autosetup -n Vulkan-Docs-%version

%build
QUIET="" ./makeAllExts manhtmlpages %{?_smp_mflags}

%install
b="%buildroot"
mkdir -p "$b/%python3_sitelib" "$b/%_docdir/%name"
cp -a out/katex out/man "$b/%_docdir/%name/"
cp -a scripts/spec_tools "$b/%python3_sitelib/"

%files
%_docdir/%name/

%files -n python3-spec_tools
%python3_sitelib/
%license COPYING.md

%changelog
