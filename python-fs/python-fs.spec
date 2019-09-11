#
# spec file for package python-fs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 LISA GmbH, Bingen, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fs
Version:        2.4.8
Release:        0
Summary:        Python's filesystem abstraction layer
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/PyFilesystem/pyfilesystem2
Source:         https://files.pythonhosted.org/packages/source/f/fs/fs-%{version}.tar.gz
# PATCH-FIX-UPSTREAM more-relaxed-requirements.patch sebix+novell.com@sebix.at -- Weaken the version dependencies
Patch0:         more-relaxed-requirements.patch
BuildRequires:  %{python_module appdirs >= 1.4.3}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyftpdlib}
BuildRequires:  %{python_module pysendfile}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module scandir >= 1.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module typing >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-backports.os >= 0.1
BuildRequires:  python-rpm-macros
Requires:       python-appdirs >= 1.4.3
Requires:       python-psutil
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-six >= 1.10.0
Requires:       python-typing >= 3.6
Recommends:     python-pyftpdlib
%ifpython2
Requires:       python-backports.os
%endif
%if %{python_version_nodots} < 34
Requires:       python-enum34 >= 1.1.6
Recommends:     python-pysendfile
%endif
%if %{python3_version_nodots} < 35
Recommends:     python-scandir >= 1.5
%endif
BuildArch:      noarch

%python_subpackages

%description
PyFilesystem is an abstraction layer for filesystems. In the same way that
Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You can
write platform-independent code to work with local files, that also works with
any of the supported filesystems (zip, ftp, S3 etc.).

%prep
%setup -q -n fs-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec  setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
