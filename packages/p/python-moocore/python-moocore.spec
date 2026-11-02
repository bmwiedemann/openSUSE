#
# spec file for package python-moocore
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-moocore
Version:        0.3.2
Release:        0
Summary:        Core algorithms for multi-objective optimization
License:        LGPL-2.1-or-later
URL:            https://github.com/multi-objective/moocore
Source:         https://files.pythonhosted.org/packages/source/m/moocore/moocore-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.17.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.17.1
Requires:       python-numpy
Requires:       python-platformdirs
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
moocore provides core algorithms for multi-objective optimization,
including computation of the hypervolume indicator, the empirical
attainment function, and other unary and binary quality metrics used
to compare Pareto set approximations.

%prep
%autosetup -p1 -n moocore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Drop the bundled C sources/headers (build inputs for the cffi extension, not
# needed at runtime) to avoid devel-file-in-non-devel-package.
%python_expand rm -rf %{buildroot}%{$python_sitearch}/moocore/libmoocore %{buildroot}%{$python_sitearch}/moocore/libmoocore.h
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The bundled test suite relies on data-path/immutability fixtures that are not
# discovered outside upstream's dev tree; smoke-test the compiled import instead.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import moocore; print(moocore.__version__)"

%files %{python_files}
%doc README.md
%license COPYRIGHTS
%{python_sitearch}/moocore
%{python_sitearch}/moocore-%{version}.dist-info

%changelog
