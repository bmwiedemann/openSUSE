#
# spec file for package python-construct
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
Name:           python-construct
Version:        2.9.45
Release:        0
Summary:        A declarative parser/builder for binary data
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/construct/construct
Source:         https://github.com/construct/construct/archive/v%{version}.tar.gz
Patch0:         split_debug.patch
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
Requires:       python-arrow
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildRequires:  python2-enum34
%ifpython2
Requires:       python-enum34
%endif
BuildArch:      noarch
%python_subpackages

%description
Construct is a declarative parser (and builder) for binary data.

Instead of writing imperative code to parse a piece of data, a data
structure that describes the data is declared. As this data structure is not
code, it can be used in one direction to parse data into Pythonic objects,
and in the other direction to convert ("build") objects into binary data.

%prep
%setup -q -n construct-%{version}
%patch0 -p1

# remove gallery tests that require in place stuff
rm -rf tests/gallery
rm -rf tests/deprecated_gallery

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/construct
%{python_sitelib}/construct-%{version}-py%{python_version}.egg-info

%changelog
