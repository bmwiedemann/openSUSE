#
# spec file for package python-runthis-sphinxext
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-runthis-sphinxext
Version:        0.0.3
Release:        0
Summary:        Provides a sphinx code-block for rendering RunThis blocks
License:        BSD-3-Clause
URL:            https://github.com/regro/runthis-sphinxext
# pypi tarball does not contain docs and license
#Source:         https://files.pythonhosted.org/packages/source/r/runthis-sphinxext/runthis-sphinxext-%%{version}.tar.gz
Source:         https://github.com/regro/runthis-sphinxext/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        runthis-client-0.0.3.min.js
Source2:        sha256-0.0.3.txt
Source99:       download_client.sh
# PATCH-FIX-OPENSUSE no_download_setup.patch -- do not download files during setup
Patch0:         no_download_setup.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This provides a sphinx extension that adds RunThis code blocks,
which display a highligthed code-block statically, but with a
"RunThis" button above them. When the button is clicked, the code
block is replaced by a terminal session that has executed that
code.

%prep
%setup -q -n runthis-sphinxext-%{version}
cp %{SOURCE1} runthis/
cp %{SOURCE2} .
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%doc README.md AUTHORS.md
%license LICENSE

%changelog
