#
# spec file for package python-jinja2-fsloader
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


Name:           python-jinja2-fsloader
Version:        0.3.0
Release:        0
Summary:        Jinja2 template loader using PyFilesystem2
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/althonos/jinja2-fsloader/
Source:         https://files.pythonhosted.org/packages/source/j/jinja2-fsloader/jinja2-fsloader-%{version}.zip
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 39.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-Jinja2 >= 2.0
Requires:       python-fs >= 2.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.0}
BuildRequires:  %{python_module contexter >= 0.1.4}
BuildRequires:  %{python_module fs >= 2.1.0}
# /SECTION
%python_subpackages

%description
This library allows using PyFilesystem2 as a backend to load
templates into Jinja2. You can take advantage of the whole fs
ecosystem, which already implements drivers for FTP, SSH, SMB, S3,
WebDAV servers, ZIP and Tar archives and others.

%prep
%setup -q -n jinja2-fsloader-%{version}
sed -i 's/,<[0-9.]*$//' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pyunittest discover -v

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/jinja2[-_]fsloader
%{python_sitelib}/jinja2[-_]fsloader-%{version}*-info

%changelog
