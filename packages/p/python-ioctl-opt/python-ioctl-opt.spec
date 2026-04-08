#
# spec file for package python-ioctl-opt
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.3.1
Release:        0
Summary:        Pythonified linux asm-generic/ioctl.h
License:        LGPL-2.1-or-later
URL:            https://github.com/vpelletier/python-ioctl-opt
Source:         https://github.com/vpelletier/python-ioctl-opt/archive/refs/tags/%{version}.tar.gz#/ioctl-opt-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Functions to compute fnctl.ioctl's opt argument.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license COPYING.LESSER
%{python_sitelib}/ioctl_opt
%{python_sitelib}/ioctl_opt-%{version}.dist-info

%changelog
