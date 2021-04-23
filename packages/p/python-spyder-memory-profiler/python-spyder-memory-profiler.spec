#
# spec file for package python-spyder-memory-profiler
#
# Copyright (c) 2021 SUSE LLC
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


# not a singlespec package: Spyder app is only for primary python3 interpreter
Name:           python-spyder-memory-profiler
Version:        0.2.1
Release:        0
Summary:        Memory profiler plugin for the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-memory-profiler
Source:         https://files.pythonhosted.org/packages/source/s/spyder_memory_profiler/spyder_memory_profiler-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
BuildRequires:  python3-memory_profiler
BuildRequires:  python-rpm-macros
BuildRequires:  spyder >= 4
Requires:       python-memory_profiler
Requires:       spyder >= 4
Provides:       python3-spyder-memory-profiler = %{version}-%{release}
Provides:       python3-spyder_memory_profiler = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-pytest
# /SECTION

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python memory profiler.
It allows seeing the memory usage for every line.

%package     -n spyder-memory-profiler
Summary:        Memory profiler plugin for the Spyder IDE
Group:          Development/Languages/Python
Provides:       python3-spyder-memory-profiler = %{version}
Provides:       spyder3-memory-profiler = %{version}-%{release}
Obsoletes:      spyder3-memory-profiler < %{version}-%{release}

%description -n spyder-memory-profiler
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python memory profiler.
It allows seeing the memory usage for every line.

%prep
%setup -q -n spyder_memory_profiler-%{version}
sed -i -e '/^#!\//, 1d' spyder_memory_profiler/example/*.py
sed -i -e '/^#!\//, 1d' spyder_memory_profiler/example/subdir/*.py

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%check
export QT_HASH_SEED=0
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONDONTWRITEBYTECODE=1
pytest-%{python_bin_suffix} -v

%files -n spyder-memory-profiler
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python3_sitelib}/spyder_memory_profiler
%{python3_sitelib}/spyder_memory_profiler-%{version}*-info

%changelog
