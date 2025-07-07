#
# spec file for package fuse-oscfs
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


%define pythons python3
Name:           fuse-oscfs
Version:        0.9.1
Release:        0
Summary:        A FUSE file system for accessing Open Build Service instances
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/mgerstner/oscfs
Source:         oscfs-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       osc
Requires:       python3-fusepy
BuildArch:      noarch
Provides:       python2-oscfs = %version-%release
Obsoletes:      python2-oscfs < %version-%release

%description
oscfs is a FUSE-based user space file system for accessing Open
Build Service (OBS) instances. It is based on the osc (openSUSE Commander)
Python package for interfacing with OBS. At the moment, it provides read-only
access for inspecting packages and their metadata.

%prep
%autosetup -p1 -n oscfs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes -s %{buildroot}%{python3_sitelib}/oscfs

%files
%defattr(-,root,root)
%doc README.md NEWS.rst
%license LICENSE.txt
%{python3_sitelib}/oscfs
%{python3_sitelib}/oscfs-%{version}.dist-info
%{_bindir}/oscfs

%changelog
