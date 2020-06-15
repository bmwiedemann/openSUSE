#
# spec file for package python-smmap
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-smmap
Version:        3.0.4
Release:        0
Summary:        A pure git implementation of a sliding window memory map manager
License:        BSD-2-Clause
URL:            https://github.com/gitpython-developers/smmap
Source:         https://files.pythonhosted.org/packages/source/s/smmap/smmap-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
When reading from many possibly large files in a fashion similar to random
access, it is usually the fastest and most efficient to use memory maps.
Although memory maps have many advantages, they represent a very limited
system resource as every map uses one file descriptor, whose amount is
limited per process. On 32 bit systems, the amount of memory you can have
mapped at a time is naturally limited to theoretical 4GB of memory, which
may not be enough for some applications.

The documentation can be found here: http://packages.python.org/smmap

%prep
%setup -q -n smmap-%{version}
dos2unix README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
