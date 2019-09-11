#
# spec file for package o2locktop
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


%define name o2locktop
%define unmangled_version 1.0.10
%define release 1
%if 0%{?suse_version} >= 1500
%define pyname python3
%else
%define pyname python
%endif

Summary:        o2locktop is a top-like OCFS2 DLM lock monitor
License:        GPL-2.0-or-later
Group:          Development/Libraries
Name:           %{name}
Version:        1.0.10+git.1564463799.6f331ba
Release:        0%{release}
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         %{_prefix}
BuildArch:      noarch
Url:            https://github.com/ganghe/o2locktop

BuildRequires:  %{pyname}
BuildRequires:  %{pyname}-setuptools
Requires:       %{pyname}

#%if 0%{?suse_version} <= 1140
BuildRequires:  -post-build-checks
#%endif

%description
o2locktop is a top-like OCFS2 DLM lock monitor, it displays DLM lock usages via querying OCFS2 file system statistics from the specified nodes. 
You can utilize o2locktop to detect the hot files/directories, whose DLM locks are frequently referenced among the cluster.
You can get the maximal wait time per DLM lock, this helps you identify which hot files/directories should be decoupled for improving file access performance.
%prep
%setup -n %{name}-%{version}

%build
%{pyname} setup.py build

%install
%{pyname} setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%if 0%{?suse_version} >= 1200
%license COPYING
%else
%doc COPYING
%endif
%doc README.md DESIGN.md

%changelog
