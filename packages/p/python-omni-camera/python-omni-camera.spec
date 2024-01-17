#
# spec file for package python-omni-camera
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


Name:           python-omni-camera
Version:        0.6.0
Release:        0
Summary:        A library for querying and capturing from cameras
License:        MIT
URL:            https://github.com/IntQuant/Camerata 
Source:         https://files.pythonhosted.org/packages/source/o/omni-camera/omni_camera-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module maturin}
BuildRequires:  fdupes
BuildRequires:  clang 
Suggests:       python-pilow
ExclusiveArch:  %{rust_tier1_arches}
%python_subpackages

%description
A library for querying and capturing from cameras, based on nokhwa crate.

%prep
%autosetup -a1 -p1 -n omni_camera-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitearch}/omni_camera
%{python_sitearch}/omni_camera-%{version}.dist-info

%changelog
