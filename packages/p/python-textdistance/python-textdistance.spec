#
# spec file for package python-textdistance
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


Name:           python-textdistance
Version:        4.6.2
Release:        0
Summary:        Compute distance between the two texts
License:        MIT
URL:            https://github.com/life4/textdistance
Source:         https://github.com/life4/textdistance/archive/refs/tags/%{version}.tar.gz#/textdistance-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE hypothesis-profile-conftest.patch -- add hypothesis profile for slow OBS executions, code@bnavigator.de
Patch1:         hypothesis-profile-conftest.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-distance
Recommends:     python-jellyfish
Recommends:     python-numpy
Recommends:     python-python-Levenshtein
Recommends:     python-pyxDamerauLevenshtein
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Compute distance between sequences. 30+ algorithms, pure python
implementation, common interface, optional external libs usage.

%prep
%autosetup -p1 -n textdistance-%{version}
chmod a-x README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we don't have all external libraries to test with
%pytest -m "not external" --hypothesis-profile obs

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/textdistance
%{python_sitelib}/textdistance-%{version}*-info

%changelog
