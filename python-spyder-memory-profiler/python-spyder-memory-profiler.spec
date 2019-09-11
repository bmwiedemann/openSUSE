#
# spec file for package python-spyder-memory-profiler
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
%define         X_display         ":98"
Name:           python-spyder-memory-profiler
Version:        0.1.2
Release:        0
Summary:        Memory profiler plugin for the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-memory-profiler
Source:         https://files.pythonhosted.org/packages/source/s/spyder_memory_profiler/spyder_memory_profiler-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module memory_profiler}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-mock
BuildRequires:  spyder >= 3
BuildRequires:  spyder-lang >= 3
BuildRequires:  spyder3 >= 3
BuildRequires:  spyder3-lang >= 3
BuildRequires:  xauth
BuildRequires:  xorg-x11-server
# /SECTION
%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python memory profiler.
It allows seeing the memory usage for every line.

%package     -n spyder-memory-profiler
Summary:        Memory profiler plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       python-memory_profiler
Requires:       spyder >= 3
Provides:       python-spyder-memory-profiler = %{version}
Provides:       python2-spyder-memory-profiler = %{version}

%description -n spyder-memory-profiler
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python memory profiler.
It allows seeing the memory usage for every line.

%package     -n spyder3-memory-profiler
Summary:        Memory profiler plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       python3-memory_profiler
Requires:       spyder3 >= 3
Provides:       python3-spyder-memory-profiler = %{version}

%description -n spyder3-memory-profiler
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python memory profiler.
It allows seeing the memory usage for every line.

%prep
%setup -q -n spyder_memory_profiler-%{version}
sed -i -e '/^#!\//, 1d' spyder_memory_profiler/example/*.py
sed -i -e '/^#!\//, 1d' spyder_memory_profiler/example/subdir/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export QT_HASH_SEED=0
export DISPLAY=%{X_display}
export PYTHONDONTWRITEBYTECODE=1
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10
%pytest spyder_memory_profiler

%files -n spyder-memory-profiler
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python2_sitelib}/*

%files -n spyder3-memory-profiler
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
