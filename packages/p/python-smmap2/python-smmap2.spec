#
# spec file for package python-smmap2
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
Name:           python-smmap2
Version:        2.0.5
Release:        0
Summary:        A pure python implementation of a sliding window memory map manager
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/Byron/smmap
Source:         https://files.pythonhosted.org/packages/source/s/smmap2/smmap2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage >= 3.4}
BuildRequires:  %{python_module nosexcover}
BuildRequires:  %{python_module nose}
# /SECTION
Conflicts:      python-smmap
BuildArch:      noarch

%python_subpackages

%description
Smmap wraps an interface around mmap and tracks the mapped files as
well as the amount of clients who use it. If the system runs out of
resources, or if a memory limit is reached, it will automatically
unload unused maps to allow continued operation.

To allow processing large files even on 32 bit systems, it allows
only portions of the file to be mapped. Once the user reads beyond
the mapped region, smmap will automatically map the next required
region, unloading unused regions using a LRU algorithm.

The interface also works around the missing offset parameter in python
implementations up to python 2.5.

Although the library can be used most efficiently with its native
interface, a Buffer implementation is provided to hide these details
behind a simple string-like interface.

For performance critical 64 bit applications, a simplified version of
memory mapping is provided which always maps the whole file, but
still provides the benefit of unloading unused mappings on demand.

%prep
%setup -q -n smmap2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
