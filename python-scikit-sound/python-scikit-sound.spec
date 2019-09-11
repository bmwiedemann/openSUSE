#
# spec file for package python-scikit-sound
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-scikit-sound
Version:        0.2.3
Release:        0
Summary:        Python utilities for working with sound signals
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://work.thaslwanter.at/sksound/html
Source:         https://files.pythonhosted.org/packages/source/s/scikit-sound/scikit-sound-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module docutils >= 0.3}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pygame}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tk}
BuildRequires:  ffmpeg
BuildRequires:  xvfb-run
# /SECTION
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-docutils >= 0.3
Requires:       python-pygame
Requires:       python-scipy
Recommends:     ffmpeg
Recommends:     python-matplotlib
Recommends:     python-tk
BuildArch:      noarch

%python_subpackages

%description
Scikit-sound contains functions for working with sound

%prep
%setup -q -n scikit-sound-%{version}
sed -i 's/\r$//' CHANGES.txt README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
