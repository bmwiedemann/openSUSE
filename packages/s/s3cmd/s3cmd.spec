#
# spec file for package s3cmd
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
Name:           s3cmd
Version:        2.4.0
Release:        0
License:        GPL-2.0-only
URL:            http://s3tools.org/s3cmd
Summary:        Command line tool for managing Amazon S3 and CloudFront services
Group:          System/Management
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-python-dateutil

# Use python-magic for SLES12_SP5
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
Requires:       python-magic
%else
Requires:       python3-magic
%endif

BuildArch:      noarch

%description
S3cmd (`s3cmd`) is a free command line tool and client for uploading, retrieving
and managing data in Amazon S3 and other cloud storage service providers that use
the S3 protocol, such as Ceph, Google Cloud Storage or DreamHost DreamObjects. It is
best suited for power users who are familiar with command line programs.

%prep
%setup -q

%build
export S3CMD_PACKAGING=1
%pyproject_wheel

%install
export S3CMD_PACKAGING=1
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%{python3_sitelib}/%{name}-%{version}.dist-info
%{python3_sitelib}/S3/
/usr/bin/%{name}

%changelog
