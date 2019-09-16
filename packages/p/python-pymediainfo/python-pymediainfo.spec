#
# spec file for package python-pymediainfo
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pymediainfo
Version:        4.0
Release:        0
Summary:        Python wrapper for the mediainfo library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sbraz/pymediainfo
Source0:        https://files.pythonhosted.org/packages/source/p/pymediainfo/pymediainfo-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  libmediainfo0
Requires:       libmediainfo0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module is a Python wrapper for the mediainfo library.

%prep
%setup -q -n pymediainfo-%{version}
rm -rf pymediainfo.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{_bindir}/py.test-%{$python_version} -v \
  -k 'not MediaInfoURLTest and not MediaInfoLibraryTest'
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
