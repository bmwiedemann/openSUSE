#
# spec file for package fuse-oscfs
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fuse-oscfs
Version:        0.70
Release:        0
Summary:        A FUSE file system for accessing Open Build Service instances
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            https://github.com/mgerstner/oscfs
Source:         https://github.com/mgerstner/oscfs/archive/%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       osc
Requires:       python3-fusepy
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       python2-oscfs = %version-%release
Obsoletes:      python2-oscfs < %version-%release

%description
oscfs is a FUSE-based user space file system for accessing Open
Build Service (OBS) instances. It is based on the osc (openSUSE Commander)
Python package for interfacing with OBS. At the moment, it provides read-only
access for inspecting packages and their metadata.

%prep
%setup -q -n oscfs-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README.md NEWS.rst
%license LICENSE.txt
%{python3_sitelib}/*
%{_bindir}/oscfs

%changelog
