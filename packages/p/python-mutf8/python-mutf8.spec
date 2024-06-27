#
# spec file for package python-mutf8
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-mutf8
Version:        1.0.6
Release:        0
Summary:        Python/C encoders/decoders for MUTF-8/CESU-8
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/TkTech/mutf8
Source:         https://github.com/TkTech/mutf8/archive/refs/tags/v%{version}.tar.gz#/mutf8-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Pure-python and optional C encoders/decoders for MUTF-8/CESU-8.

%prep
%autosetup -n mutf8-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -v

%files %{python_files}
%license LICENCE
%doc README.md
%{python_sitearch}/mutf8
%{python_sitearch}/mutf8-%{version}-py%{python_version}.egg-info

%changelog
