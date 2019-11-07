#
# spec file for package python-spyder-line-profiler
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
%define skip_python2 1
Name:           python-spyder-line-profiler
Version:        0.1.1
Release:        0
Summary:        Line profiler plugin for the Spyder IDE
License:        MIT
URL:            https://github.com/spyder-ide/spyder-line-profiler
Source:         https://files.pythonhosted.org/packages/source/s/spyder_line_profiler/spyder_line_profiler-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python line profiler.
It allows seeing the time spent for every line.

%package -n spyder3-line-profiler
Summary:        Line profiler plugin for the Spyder IDE
Requires:       python3-line_profiler
Requires:       spyder3 >= 3

%description -n spyder3-line-profiler
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python line profiler.
It allows seeing the time spent for every line.

%prep
%setup -q -n spyder_line_profiler-%{version}

# fix rpmlint non-executable-script
sed -i -e '/^#!\//, 1d' spyder_line_profiler/example/profiling_test_script.py
sed -i -e '/^#!\//, 1d' spyder_line_profiler/example/subdir/profiling_test_script2.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files -n spyder3-line-profiler
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
