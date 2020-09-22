#
# spec file for package eyeD3
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


Name:           eyeD3
Version:        0.9.5
Release:        0
Summary:        Audio files and ID3 Manipulation Tool
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://eyed3.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/e/eyeD3/eyeD3-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-scipy
BuildRequires:  python3-setuptools
BuildArch:      noarch

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

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%license LICENSE
%doc AUTHORS.rst
%doc README.rst
%doc CONTRIBUTING.rst
%doc HISTORY.rst
%doc docs
%doc examples
%{_bindir}/eyeD3
%{python3_sitelib}/eyed3
%{python3_sitelib}/eyeD3*

%changelog
