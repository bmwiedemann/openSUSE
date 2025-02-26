#
# spec file for package python-ioctl-opt
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-ioctl-opt
Version:        1.3
Release:        0
Summary:        Pythonified linux asm-generic/ioctl.h
License:        GPL-2.0-only
URL:            https://github.com/vpelletier/python-ioctl-opt
Source:         https://pypi.org/packages/source/i/ioctl-opt/ioctl-opt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Functions to compute fnctl.ioctl's opt argument.

%prep
%autosetup -p1 -n ioctl-opt-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/ioctl_opt
%{python_sitelib}/ioctl_opt-%{version}-*.egg-info

%changelog
