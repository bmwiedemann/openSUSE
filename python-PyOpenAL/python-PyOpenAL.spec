#
# spec file for package python-PyOpenAL
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
Name:           python-PyOpenAL
Version:        0.7.7a1
Release:        0
Summary:        Python bindings for OpenAL
License:        SUSE-Public-Domain
Group:          Development/Languages/Python
URL:            https://github.com/Zuzu-Typ/PyOpenAL
Source:         https://files.pythonhosted.org/packages/source/P/PyOpenAL/PyOpenAL-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       config(openal-soft)
Recommends:     python-PyOgg
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
# /SECTION
%python_subpackages

%description
PyOpenAL provides OpenAL bindings for Python as well as an interface
to them.

It also provides a way to play WAVE and, if PyOgg is
installed, OGG Vorbis, OGG Opus and FLAC files.

%prep
%setup -q -n PyOpenAL-%{version}
dos2unix README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license COPYING LICENSE
%{python_sitelib}/*

%changelog
