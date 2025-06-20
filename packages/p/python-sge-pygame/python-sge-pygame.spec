#
# spec file for package python-sge-pygame
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-sge-pygame
Version:        1.7.1
Release:        0
Summary:        A 2-D game engine for Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://python-sge.github.io
Source:         https://files.pythonhosted.org/packages/source/s/sge/sge-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygame >= 1.9.1
Requires:       python-six >= 1.4.0
Requires:       python-uniseg
BuildArch:      noarch
%python_subpackages

%description
The SGE Game Engine is a general-purpose 2-D game engine. It takes
care of several details, such as window size management, collision
detection, parallax scrolling, image transformation.

This implementation of the SGE uses Pygame as a backend.

%prep
%setup -q -n sge-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README README.pygame WHATSNEW WHATSNEW.pygame
%license sge/COPYING sge/COPYING.LESSER
%{python_sitelib}/sge
%{python_sitelib}/sge-%{version}*-info

%changelog
