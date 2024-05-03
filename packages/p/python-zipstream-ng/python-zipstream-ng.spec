#
# spec file for package python-zipstream-ng
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


Name:            python-zipstream-ng
Version:         1.7.1
Release:         0
Summary:         Modern and easy to use streamable zip file generator
License:         LGPL-3.0
URL:             https://github.com/pR0Ps/zipstream-ng
Source:          https://files.pythonhosted.org/packages/source/z/zipstream-ng/zipstream-ng-%{version}.tar.gz
BuildRequires:   python-rpm-macros
BuildRequires:   %{python_module setuptools}
BuildRequires:   %{python_module pytest}
BuildRequires:   fdupes
Requires(post):  update-alternatives
Requires(preun): update-alternatives
BuildArch:       noarch
Conflicts:       python-zipstream
%python_subpackages

%description
A modern and easy to use streamable zip file generator.
It can package and stream many files and folders into a zip on the fly
without needing temporary files or excessive memory.

It can also calculate the final size of the zip file before streaming it.

Features:
 * Generates zip data on the fly as it's requested.
 * Can calculate the total size of the resulting zip file before generation even begins.
 * Low memory usage: Since the zip is generated as it's requested,
   very little has to be kept in memory (peak usage of less than 20MB is typical, even for TBs of files).
 * Flexible API: Typical use cases are simple, complicated ones are possible.
 * Supports zipping data from files, bytes, strings, and any other iterable objects.
 * Keeps track of the date of the most recently modified file added to the zip file.
 * Threadsafe: Won't mangle data if multiple threads concurrently add data to the same stream.
 * Includes a clone of Python's http.server module with zip support added. Try python -m zipstream.server.
 * Automatically uses Zip64 extensions, but only if they are required.
 * No external dependencies.

%prep
%autosetup -n zipstream-ng-%{version}

# Remove shebangs for sitelib
find . -type f -name "*.py" -exec sed -i '/^#!.*env python.*/d' {} ';'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/zipserver

%check
%pytest

%post
%python_install_alternative zipserver

%postun
%python_uninstall_alternative zipserver

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/zipserver
%{python_sitelib}/zipstream
%{python_sitelib}/zipstream_ng-%{version}*

%changelog
