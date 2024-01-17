#
# spec file for package python-noiseprotocol
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-noiseprotocol
Version:        0.3.1
Release:        0
Summary:        Implementation of Noise Protocol Framework
License:        MIT
URL:            https://github.com/plizonczyk/noiseprotocol
Source:         https://github.com/plizonczyk/noiseprotocol/archive/refs/tags/v0.3.1.tar.gz#/noiseprotocol-%{version}.tar.gz 
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires:       python-cryptography
BuildArch:      noarch
%python_subpackages

%description
A Python 3 implementation of Noise Protocol Framework. Compatible with revisions 32 and 33.

%prep
%setup -q -n noiseprotocol-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/noise
%{python_sitelib}/noiseprotocol-%{version}*-info
%{python_sitelib}/examples

%changelog
