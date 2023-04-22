#
# spec file for package python-fs
#
# Copyright (c) 2023 SUSE LLC
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
%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-fs
Version:        2.4.16
Release:        0
Summary:        Python's filesystem abstraction layer
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyFilesystem/pyfilesystem2
Source:         https://files.pythonhosted.org/packages/source/f/fs/fs-%{version}.tar.gz
BuildRequires:  %{python_module appdirs >= 1.4.3}
BuildRequires:  %{python_module enum34 >= 1.1.6 if %python-base < 3.4}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyftpdlib}
BuildRequires:  %{python_module pysendfile}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module scandir >= 1.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module typing >= 3.6 if %python-base < 3.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs >= 1.4.3
Requires:       python-psutil
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-six >= 1.10.0
Recommends:     python-pyftpdlib
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-backports.os >= 0.1
BuildRequires:  python-mock
%endif
%ifpython2
Requires:       python-backports.os >= 0.1
%endif
%if %{python_version_nodots} < 34
Requires:       python-enum34 >= 1.1.6
Recommends:     python-pysendfile
%endif
%if %{python_version_nodots} < 35
Recommends:     python-scandir >= 1.5
%endif
%if %{python_version_nodots} < 36
Requires:       python-typing >= 3.6
%endif
%python_subpackages

%description
PyFilesystem is an abstraction layer for filesystems. In the same way that
Python's file-like objects provide a common way of accessing files,
PyFilesystem provides a common way of accessing entire filesystems. You can
write platform-independent code to work with local files, that also works with
any of the supported filesystems (zip, ftp, S3 etc.).

%prep
%setup -q -n fs-%{version}
sed -i -e '/install_requires/,/bdist_wheel/ s:~=:>=:g' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fs
%{python_sitelib}/fs-%{version}*-info

%changelog
