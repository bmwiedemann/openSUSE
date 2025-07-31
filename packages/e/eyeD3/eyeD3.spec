#
# spec file for package eyeD3
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


Name:           eyeD3
Version:        0.9.8
Release:        0
Summary:        Audio files and ID3 Manipulation Tool
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://eyed3.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/e/eyeD3/eyed3-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module chardet >= 5.2.0}
BuildRequires:  %{python_module colorama >= 0.4.6}
BuildRequires:  %{python_module deprecation >= 2.1.0}
BuildRequires:  %{python_module factory_boy >= 3.3.3}
BuildRequires:  %{python_module filetype >= 1.2.0}
BuildRequires:  %{python_module idna >= 2.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.32.4}
BuildRequires:  %{python_module toml >= 0.10.2}
BuildRequires:  %{python_module wheel}
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
Requires:       python-chardet >= 5.2.0
Requires:       python-colorama >= 0.4.6
Requires:       python-deprecation >= 2.1.0
Requires:       python-filetype >= 1.2.0
Requires:       python-idna >= 2.10
Requires:       python-packaging >= 20.8
Requires:       python-pyparsing >= 2.4.7
Requires:       python-requests >= 2.32.4
Requires:       python-toml >= 0.10.2
Requires:       python-urllib3 >= 2.5.0
Recommends:     python-grako
Recommends:     python-pillow
# for plugins
Recommends:     python-pylast
Recommends:     python-requests
Recommends:     python-ruamel.yaml

%description -n python-eyed3
eyeD3 is a Python tool for working with audio files, specifically MP3
files containing ID3 metadata (i.e. song info).

%prep
%autosetup -p1 -n eyed3-%{version}
# currently broken
rm eyed3/plugins/mimetype.py

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
#%doc docs
#%doc examples
%{_bindir}/eyeD3

%files %{python_files eyed3}
%{python_sitelib}/eyed3
%{python_sitelib}/eyed3-%{version}.dist-info

%changelog
