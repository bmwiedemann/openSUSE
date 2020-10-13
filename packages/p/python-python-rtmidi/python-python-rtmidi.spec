#
# spec file for package python-python-rtmidi
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
Name:           python-python-rtmidi
Version:        1.4.5
Release:        0
Summary:        Python binding for the RtMidi C++ library
License:        MIT
Group:          Development/Languages/Python
URL:            https://chrisarndt.de/projects/python-rtmidi/
Source:         https://files.pythonhosted.org/packages/source/p/python-rtmidi/python-rtmidi-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
%python_subpackages

%description
RtMidi is a set of C++ classes which provides an API for realtime
MIDI I/O across Linux (ALSA & JACK), macOS (CoreMIDI & JACK),
and Windows (MultiMedia System) operating systems.

python-rtmidi is a Python binding for RtMidi implemented using
Cython and provides a thin wrapper around the RtMidi C++ interface.
The API is basically the same as the C++ one but with the naming
scheme of classes, methods and parameters adapted to the Python
PEP-8 conventions and requirements of the Python package naming
structure.

%package doc
Summary:        HTML documentation and examples for python-rtmidi
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Contains HTML documentation and examples for python-rtmidi.

%prep
%setup -q -n python-rtmidi-%{version}
sed -i 's,/usr/bin/env python,/usr/bin/%{python_for_executables},' examples/*.py examples/*/*.py

%build
%python_build

# docs
rm docs/rtmidi.rst
rm docs/modules.rst
%{python_for_executables} ./setup.py build_ext --inplace
sphinx-apidoc -o docs/ rtmidi rtmidi/release.py
cat docs/api.rst.inc >> docs/rtmidi.rst
%make_build -C docs html
rm docs/_build/html/.buildinfo docs/_build/html/objects.inv

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# not running tests since they require working JACK/ALSA,
# which cannot be provided on OBS workers

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitearch}/*

%files doc
%doc docs/_build/html examples

%changelog
