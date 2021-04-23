#
# spec file for package python-spyder-line-profiler
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


# not a singlespec package: Spyder is available for the primary interpreter only
Name:           python-spyder-line-profiler
Version:        0.2.1
Release:        0
Summary:        Line profiler plugin for the Spyder IDE
License:        MIT
URL:            https://github.com/spyder-ide/spyder-line-profiler
Source:         https://files.pythonhosted.org/packages/source/s/spyder_line_profiler/spyder_line_profiler-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-line_profiler
BuildRequires:  python3-setuptools
BuildRequires:  python-rpm-macros
BuildRequires:  spyder >= 4
Requires:       python-line_profiler
Requires:       spyder >= 4
Provides:       python3-spyder-line-profiler = %{version}-%{release}
Provides:       python3-spyder_line_profiler = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-pytest
BuildRequires:  xdpyinfo
# /SECTION

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates the Python line profiler.
It allows seeing the time spent for every line.

%package -n spyder-line-profiler
Summary:        Line profiler plugin for the Spyder IDE
Provides:       spyder3-line-profiler = %{version}-%{release}
Obsoletes:      spyder3-line-profiler < %{version}-%{release}

%description -n spyder-line-profiler
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
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONDONTWRITEBYTECODE=1
pytest-%{python_bin_suffix} -v

%files -n spyder-line-profiler
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python3_sitelib}/spyder_line_profiler
%{python3_sitelib}/spyder_line_profiler-%{version}*-info

%changelog
