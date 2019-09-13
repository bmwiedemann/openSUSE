#
# spec file for package python-cachey
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
Name:           python-cachey
Version:        0.1.1
Release:        0
Summary:        A Python cache mindful of computation/storage costs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/mrocklin/cachey/
Source:         https://files.pythonhosted.org/packages/source/c/cachey/cachey-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_cache_clear.patch - fix unit test error
Patch0:         fix_cache_clear.patch
BuildRequires:  %{python_module HeapDict}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-HeapDict
BuildArch:      noarch
%python_subpackages

%description
Cachey tries to hold on to values that have the following characteristics

1. Expensive to recompute (in seconds)
2. Cheap to store (in bytes)
3. Frequently used
4. Recenty used

It accomplishes this by adding the following to each items score on each access

    score += compute_time / num_bytes * (1 + eps) ** tick_time

For some small value of epsilon (which determines the memory halflife). This
has units of inverse bandwidth, has exponential decay of old results and
roughly linear amplification of repeated results.

%prep
%setup -q -n cachey-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
