#
# spec file for package eyeD3
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


Name:           eyeD3
Version:        0.9.9
Release:        0
Summary:        Audio files and ID3 Manipulation Tool
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://eyed3.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/e/eyeD3/eyed3-%{version}.tar.gz
#Source1:       https://eyed3.nicfit.net/releases/eyeD3-test-data.tgz -- unversioned, could change with releases, download manually!
Source1:        eyeD3-test-data.tgz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module deprecation >= 2.1.0}
BuildRequires:  %{python_module filetype >= 1.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.3.5}
BuildRequires:  %{python_module factory_boy >= 3.3.3}
# /SECTION
# SECTION optional requirements for plugins
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module Pillow >= 11.3.0}
BuildRequires:  %{python_module pylast >= 5.5.0}
BuildRequires:  %{python_module requests >= 2.32.4}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
# %%primary_python not available in Leap yet
Requires:       %(echo %{python_module eyed3} | perl -pe 's{.* }{}g')
%define python_subpackage_only 1
%python_subpackages

%description
eyeD3 is a Python tool for working with audio files, specifically MP3
files containing ID3 metadata (i.e. song info).

Features:
- Python package for writing application and/or plugins.
- Command-line tool driver script that supports plugins. viewer/editor
  interface.
- Easy editing/viewing of audio metadata from the command-line, using the
  ‘classic’ plugin.
- Support for ID3 versions 1.x, 2.2 (read-only), 2.3, and 2.4.
- Support for the MP3 audio format exposing details such as play time,
  bit rate, sampling frequency, etc.
- Abstract design allowing future support for different audio formats and
  metadata containers.

%package -n python-eyed3
Summary:        Component library of eyeD3, an ID3 tag manipulation tool
Group:          Development/Languages/Python
Requires:       python-deprecation >= 2.1.0
Requires:       python-filetype >= 1.2.0
# for plugins
Recommends:     python-PyYAML
Recommends:     python-Pillow
Recommends:     python-pylast
Recommends:     python-requests

%description -n python-eyed3
eyeD3 is a Python tool for working with audio files, specifically MP3
files containing ID3 metadata (i.e. song info).

%prep
%autosetup -p1 -n eyed3-%{version} -b1
# currently broken
rm eyed3/plugins/mimetype.py
# See Makefile
ln -s $PWD/../eyeD3-test-data tests/data

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files
%license LICENSE
%doc AUTHORS.rst
%doc README.rst
%doc CONTRIBUTING.rst
%doc HISTORY.rst
#%%doc docs
#%%doc examples
%{_bindir}/eyeD3

%files %{python_files eyed3}
%{python_sitelib}/eyed3
%{python_sitelib}/eyed3-%{version}.dist-info

%changelog
